import argparse

from Bot.github_bot import GitHubBot
from Tests.bot_tests import create_repository_test


def cli():
    parser = argparse.ArgumentParser(description='GitHub CLI tool')
    parser.add_argument(
        '-c', '--create', action='store_true', help='Creates a repository')
    parser.add_argument('-n', '--name', help='Repository name')
    parser.add_argument(
        '-p', '--private', action='store_true', help='Flag to make the repository private')


def main():
    # create_repository_test()
    args = cli()

    if args.create:
        repository_name = args.name if args.name else 'test'
        bot = GitHubBot()
        bot.create_repository(repository_name)


if __name__ == '__main__':
    main()
