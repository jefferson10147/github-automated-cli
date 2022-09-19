from selenium.webdriver.common.by import By
from Bot.base_page import BasePage

from Settings.settings import Config

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
    repository_description = (By.ID, 'repository_description')
    private_repository_option = (By.ID, 'repository_visibility_private')
    public_respository_option = (By.ID, 'repository_visibility_public')
    create_repository_btn = (By.CSS_SELECTOR, '.btn-primary.btn')


    def __init__(self):
        self.username = Config.username
        self.password = Config.password
        self.driver_path = Config.driver_path
        super().__init__(self.driver_path, self.main_page_url)

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

    def enter_respository_name(self, repository_name):
        self.input_text(repository_name, *self.input_repository_name)

    def enter_repository_description(self, description):
        self.input_text(description, *self.repository_description)

    def set_private_repository(self):
        self.wait_for_element_click(*self.private_repository_option)

    def set_public_repository(self):
        self.wait_for_element_click(*self.public_respository_option)

    def create_repository(self):
        self.wait_for_element_click(*self.create_repository_btn)

    def start_repository(self, repository_name):
        print(f'Creating repository called {repository_name}...')
        self.open_main_page()
        self.maximize_window()
        self.click_on_sigin_btn()
        self.enter_user()
        self.enter_password()
        self.submit_sigin_data()
        self.click_on_more_options_btn()
        self.click_on_new_repository()
        self.enter_respository_name(repository_name)
        self.set_private_repository()
        self.create_repository()
        self.end_test()
        print('The repository has been created :D')
