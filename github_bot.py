from base_page import BasePage


class GitHubBot(BasePage):
    main_page_url = 'https://github.com/'

    def __init__(self):
        super().__init__(self.main_page_url)
