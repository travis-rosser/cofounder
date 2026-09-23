"""Run with python3 -m unittest discover -s tests -v. Uses disposable local repos."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

HOOK = Path(__file__).resolve().parents[1] / 'template/.claude/hooks/cofounder-guard.sh'


class GuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.repo = self.base / 'project'
        self.repo.mkdir()
        self.git('init', '-b', 'trunk')
        self.git('config', 'user.email', 'test@example.invalid')
        self.git('config', 'user.name', 'Test')
        (self.repo / 'file.txt').write_text('baseline\n')
        self.git('add', '.')
        self.git('commit', '-m', 'Fixture')

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.repo), *args], check=True,
                              capture_output=True, text=True)

    def guard(self, target=None, cwd=None, raw=None, key='file_path', payload_cwd=None):
        payload = {'tool_input': {key: str(target or self.repo / 'file.txt')}}
        if payload_cwd:
            payload['cwd'] = str(payload_cwd)
        result = subprocess.run(['sh', str(HOOK)], cwd=cwd or self.repo,
                                input=raw if raw is not None else json.dumps(payload),
                                capture_output=True, text=True)
        return result.returncode

    def parallel(self):
        self.git('config', '--local', 'cofounder.parallel', 'true')

    def worktree(self):
        path = self.base / 'linked'
        self.git('worktree', 'add', str(path), '-b', 'feature/linked')
        return path

    def test_solo_custom_default_branch(self):
        self.assertEqual(self.guard(), 0)

    def test_solo_feature_branch(self):
        self.git('switch', '-c', 'feature/solo')
        self.assertEqual(self.guard(), 0)

    def test_dirty_does_not_claim_another_owner(self):
        (self.repo / 'file.txt').write_text('unfinished\n')
        self.assertEqual(self.guard(), 0)

    def test_detached_primary_blocked(self):
        self.git('checkout', '--detach')
        self.assertEqual(self.guard(), 2)

    def test_unborn_branch_allowed(self):
        fresh = self.base / 'fresh'
        fresh.mkdir()
        subprocess.run(['git', '-C', str(fresh), 'init', '-b', 'main'], check=True,
                       capture_output=True)
        self.assertEqual(self.guard(fresh / 'new.txt', fresh), 0)

    def test_outside_git_allowed(self):
        self.assertEqual(self.guard(self.base / 'new.txt', self.base), 0)

    def test_parallel_primary_blocked(self):
        self.parallel()
        self.assertEqual(self.guard(), 2)

    def test_parallel_subdirectory_blocked(self):
        self.parallel()
        (self.repo / 'sub').mkdir()
        self.assertEqual(self.guard(self.repo / 'sub' / 'file.txt'), 2)

    def test_parallel_linked_allowed(self):
        linked = self.worktree()
        self.parallel()
        self.assertEqual(self.guard(linked / 'file.txt', linked), 0)

    def test_missing_target_parents_do_not_use_cwd_repo(self):
        linked = self.worktree()
        self.parallel()
        self.assertEqual(self.guard(self.repo / 'new' / 'nested' / 'file.txt', linked), 2)

    def test_relative_path_uses_payload_cwd(self):
        linked = self.worktree()
        self.parallel()
        self.assertEqual(self.guard('file.txt', linked, payload_cwd=self.repo), 2)

    def test_json_escaped_path_and_notebook(self):
        self.parallel()
        self.assertEqual(self.guard(self.repo / 'a "quoted" folder' / 'n.ipynb',
                                    key='notebook_path'), 2)

    def test_malformed_input_blocked(self):
        self.assertEqual(self.guard(raw='{'), 2)
        self.assertEqual(self.guard(raw='{}'), 2)
        self.assertEqual(self.guard(raw='null'), 2)

    def test_invalid_configuration_blocked(self):
        self.git('config', '--local', 'cofounder.parallel', 'perhaps')
        self.assertEqual(self.guard(), 2)

    def test_disable_parallel_restores_solo(self):
        self.parallel()
        self.git('config', '--local', 'cofounder.parallel', 'false')
        self.assertEqual(self.guard(), 0)

    def test_cleanup_removes_worktree_before_branch(self):
        linked = self.worktree()
        self.git('merge', 'feature/linked')
        self.git('worktree', 'remove', str(linked))
        self.git('branch', '-d', 'feature/linked')
        self.assertFalse(linked.exists())


if __name__ == '__main__':
    unittest.main()
