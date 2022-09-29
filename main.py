import argparse
import os

from Bot.github_bot import GitHubBot
from Settings.settings import Config


def set_up_repository(path: str, repository_name: str) -> None:
    """
    Initialized the git repository into the local folder.

    Args:
        path (str): The path of the local folder.
        repository_name (str): The name of the repository on GitHub
    """
    initial_git_commands = [
        f'echo "# {repository_name}" >> README.md',
        'git init',
        'git add README.md',
        'git commit -m "first commit"',
        f'git branch -M {Config.main_branch_name}', 
        f'git remote add origin {Config.github_link}{repository_name}.git',
        f'git push -u origin {Config.main_branch_name}'
    ]

    os.chdir(path)
    for command in initial_git_commands:
        os.system(command)


def set_up_local_folder(repository_name: str) -> None:
    """
    Create the local folder which contains the repository.

    Args:
        repository_name (str): The name of the repository on GitHub.
    """
    parent_dir = Config.local_path
    path = os.path.join(parent_dir, repository_name)
    os.mkdir(path)
    print(f'Directory {path} created')
    set_up_repository(path, repository_name)


def cli() -> None:
    """
    Set up the command line for the script.

    Returns:
        parser: The object with the arguments.
    """
    parser = argparse.ArgumentParser(description='GitHub CLI tool')
    
    parser.add_argument(
        '-c', '--create', action='store_true', help='Creates a repository')
    parser.add_argument('-n', '--name', help='Repository name')
    parser.add_argument(
        '-p', '--private', action='store_true', help='Flag to make the repository private')
    parser.add_argument(
        '-l', '--local', action='store_true', help='Flag to set up the local repository')
    parser.add_argument(
        '-d', '--delete', action='store_true', help='Delete any specified repository')

    return parser.parse_args()


def main():
    args = cli()

    repository_name = args.name if args.name else 'test'
    bot = GitHubBot()

    if args.create:
        bot.create_repository(repository_name)
        
    if args.local: 
        set_up_local_folder(repository_name)

    if args.delete:
        bot.delete_repository(repository_name)


if __name__ == '__main__':
    main()
