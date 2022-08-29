from selenium.webdriver.common.by import By
from base_page import BasePage

from settings import Config

class GitHubBot(BasePage):
    main_page_url = 'https://github.com/'
    signin_btn = (By.CSS_SELECTOR ,'a[href="/login"]')
    user_field = (By.ID, 'login_field')


    def __init__(self):
        self.username = Config.username
        self.password = Config.password
        self.driver_path = Config.get_driver_path()
        super().__init__(self.driver_path ,self.main_page_url)

    def click_on_sigin_btn(self):
        self.click(*self.signin_btn)

    def enter_user(self):
        self.input_text(self.username, self.user_field)
