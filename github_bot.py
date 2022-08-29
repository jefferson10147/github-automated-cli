from selenium.webdriver.common.by import By
from base_page import BasePage


class GitHubBot(BasePage):
    main_page_url = 'https://github.com/'
    signin_btn = (By.CSS_SELECTOR ,'a[href="/login"]')


    def __init__(self):
        super().__init__(self.main_page_url)

    def click_on_sigin_btn(self):
        self.click(*self.signin_btn)
