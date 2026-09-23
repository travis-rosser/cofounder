"""Guard covered file edits, not shell writes or concurrent session ownership."""
import json
import os
from pathlib import Path
import subprocess
import sys


def git(directory, *args):
    result = subprocess.run(
        ['git', '-C', str(directory), *args], capture_output=True, text=True
    )
    return result.returncode, result.stdout.strip()


def check(payload):
    tool_input = payload.get('tool_input', {})
    # NotebookEdit uses notebook_path; the other covered tools use file_path.
    target = tool_input.get('file_path') or tool_input.get('notebook_path')
    if not isinstance(target, str) or not target:
        raise ValueError('covered edit did not provide a target path')
    cwd = payload.get('cwd') or os.getcwd()
    target = Path(target).expanduser()
    if not target.is_absolute():
        target = Path(cwd) / target
    directory = target.resolve().parent
    # New nested files must be checked against their target repository, not process cwd.
    while not directory.exists() and directory != directory.parent:
        directory = directory.parent
    code, root = git(directory, 'rev-parse', '--show-toplevel')
    if code:
        # Outside Git, e.g. first-session setup. Ownership rules still apply.
        return None
    code, _ = git(root, 'symbolic-ref', '-q', 'HEAD')
    if code:
        return 'This checkout has detached HEAD. Create or select a task branch before editing.'
    code, enabled = git(root, 'config', '--bool', '--get', 'cofounder.parallel')
    if code not in (0, 1):
        raise ValueError('cofounder.parallel must be a Git boolean')
    if enabled != 'true':
        return None
    paths = []
    for flag in ('--git-dir', '--git-common-dir'):
        code, value = git(root, 'rev-parse', flag)
        if code:
            raise ValueError('could not identify the checkout')
        path = Path(value)
        paths.append((Path(root) / path).resolve() if not path.is_absolute() else path.resolve())
    if paths[0] == paths[1]:
        return ('Parallel mode reserves this primary checkout for integration. Edit in your '
                'own linked worktree. Disable cofounder.parallel only after concurrent writers stop.')
    return None


def main():
    try:
        message = check(json.load(sys.stdin))
    except (ValueError, TypeError, AttributeError, OSError) as error:
        message = f'Could not validate this edit: {error}. Check the hook setup before retrying.'
    if message:
        print(f'Cofounder guard: {message}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
