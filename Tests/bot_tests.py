from Bot.github_bot import GitHubBot


def create_repository_test():
    repository_name = 'test-repo'
    bot = GitHubBot()
    bot.create_repository(repository_name)


def delete_repsitory_test():
    repository_name = 'test-repo'
    bot = GitHubBot()
    bot.delete_repository(repository_name)
