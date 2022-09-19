import argparse
import os

from Bot.github_bot import GitHubBot
from Settings.settings import Config
from Tests.bot_tests import create_repository_test


def set_up_local_folder(repository_name):
    parent_dir = Config.local_path
    path = os.path.join(parent_dir, repository_name)
    os.mkdir(path)
    print(f'Directory {path} created')


def cli():
    parser = argparse.ArgumentParser(description='GitHub CLI tool')
    parser.add_argument(
        '-c', '--create', action='store_true', help='Creates a repository')
    parser.add_argument('-n', '--name', help='Repository name')
    parser.add_argument(
        '-p', '--private', action='store_true', help='Flag to make the repository private')
    parser.add_argument('-l', '--local', action='store_true', help='Flag to set up the local repository')


def main():
    # create_repository_test()
    args = cli()

    if args.create:
        repository_name = args.name if args.name else 'test'
        bot = GitHubBot()
        bot.create_repository(repository_name)
        
        if args.local: 
            set_up_local_folder()


if __name__ == '__main__':
    main()
