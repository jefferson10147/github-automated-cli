import argparse
import os

from Bot.github_bot import GitHubBot
from Settings.settings import Config
from Tests.bot_tests import create_repository_test


def set_up_repository(path: str, repository_name: str) -> None:
    os.chdir(path)
    os.system(f'echo "# {repository_name}" >> README.md')
    os.system('git init')
    os.system('git add README.md')
    os.system('git commit -m "first commit"')
    os.system(f'git branch -M {Config.main_branch_name}')
    os.system(f'git remote add origin {Config.github_link}{repository_name}.git')
    os.system(f'git push -u origin {Config.main_branch_name}')


def set_up_local_folder(repository_name: str) -> None:
    parent_dir = Config.local_path
    path = os.path.join(parent_dir, repository_name)
    os.mkdir(path)
    print(f'Directory {path} created')
    set_up_repository(path, repository_name)


def cli() -> None:
    parser = argparse.ArgumentParser(description='GitHub CLI tool')
    
    parser.add_argument(
        '-c', '--create', action='store_true', help='Creates a repository')
    parser.add_argument('-n', '--name', help='Repository name')
    parser.add_argument(
        '-p', '--private', action='store_true', help='Flag to make the repository private')
    parser.add_argument(
        '-l', '--local', action='store_true', help='Flag to set up the local repository')

    return parser.parse_args()


def main():
    # create_repository_test()
    args = cli()

    repository_name = args.name if args.name else 'test'

    if args.create:
        bot = GitHubBot()
        bot.create_repository(repository_name)
        
    if args.local: 
        set_up_local_folder(repository_name)


if __name__ == '__main__':
    main()
