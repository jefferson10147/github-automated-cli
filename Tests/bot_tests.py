from Bot.github_bot import GitHubBot


def create_repository_test():
    repository_name = 'test-repo'
    bot = GitHubBot()
    bot.create_repository(repository_name)
