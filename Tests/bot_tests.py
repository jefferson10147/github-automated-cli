from Bot.github_bot import GitHubBot


def create_repository_test():
    repository_name = 'test-repo'
    bot = GitHubBot()
    bot.open_main_page()
    bot.maximize_window()
    bot.click_on_sigin_btn()
    bot.enter_user()
    bot.enter_password()
    bot.submit_sigin_data()
    bot.click_on_more_options_btn()
    bot.click_on_new_repository()
    bot.enter_respository_name(repository_name)
    bot.set_private_repository()
    bot.create_repository()
    bot.end_test()
