from selenium.webdriver.common.by import By
from base_page import BasePage

from settings import Config

class GitHubBot(BasePage):
    main_page_url = 'https://github.com/'

    #locators
    signin_btn = (By.CSS_SELECTOR ,'a[href="/login"]')
    user_field = (By.ID, 'login_field')
    password_field = (By.ID, 'password')
    sigin_submit = (By.CSS_SELECTOR, '.btn.btn-primary.btn-block.js-sign-in-button')
    more_options_btn = (By.CSS_SELECTOR, '.details-overlay.details-reset summary.Header-link svg')
    new_repository_dropdown_btn = (By.CSS_SELECTOR, '.dropdown-menu.dropdown-menu-sw a[href="/new"]')
    input_repository_name = (By.ID, 'repository_name')


    def __init__(self):
        self.username = Config.username
        self.password = Config.password
        self.driver_path = Config.get_driver_path()
        super().__init__(self.driver_path ,self.main_page_url)

    def click_on_sigin_btn(self):
        self.wait_for_element_click(*self.signin_btn)

    def enter_user(self):
        self.input_text(self.username, *self.user_field)

    def enter_password(self):
        self.input_text(self.password, *self.password_field)

    def submit_sigin_data(self):
        self.wait_for_element_click(*self.sigin_submit)

    def click_on_more_options_btn(self):
        self.wait_for_element_click(*self.more_options_btn)

    def click_on_new_repository(self):
        self.wait_for_element_click(*self.new_repository_dropdown_btn)
