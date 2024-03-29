from selenium.webdriver.common.by import By
from Bot.base_page import BasePage

from Settings.settings import Config

class GitHubBot(BasePage):
    """
    Selenium bot's actions and locators inside the GitHub page.

    Args:
        BasePage: Father class.
    """
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
    user_icon = (
        By.CSS_SELECTOR,
        '.details-overlay.details-reset.js-feature-preview-indicator-container'
    )
    your_repositories_drop_down = (By.CSS_SELECTOR, 'a[href="/jefferson10147?tab=repositories"]')
    settings_btn = (By.ID, 'settings-tab')
    delete_respository_btn = (By.XPATH, '//summary[contains(text(), "Delete this repository")]')


    def __init__(self) -> None:
        self.username = Config.username
        self.password = Config.password
        self.driver_path = Config.driver_path
        super().__init__(self.driver_path, self.main_page_url)

    def click_on_sigin_btn(self) -> None:
        self.wait_for_element_click(*self.signin_btn)

    def enter_user(self) -> None:
        self.input_text(self.username, *self.user_field)

    def enter_password(self) -> None:
        self.input_text(self.password, *self.password_field)

    def submit_sigin_data(self) -> None:
        self.wait_for_element_click(*self.sigin_submit)

    def click_on_more_options_btn(self) -> None:
        self.wait_for_element_click(*self.more_options_btn)

    def click_on_new_repository(self) -> None:
        self.wait_for_element_click(*self.new_repository_dropdown_btn)

    def enter_respository_name(self, repository_name) -> None:
        self.input_text(repository_name, *self.input_repository_name)

    def enter_repository_description(self, description) -> None:
        self.input_text(description, *self.repository_description)

    def set_private_repository(self) -> None:
        self.wait_for_element_click(*self.private_repository_option)

    def set_public_repository(self) -> None:
        self.wait_for_element_click(*self.public_respository_option)

    def create_repository(self) -> None:
        self.wait_for_element_click(*self.create_repository_btn)

    def click_user_icon(self) -> None:
        self.wait_for_element_click(*self.user_icon)

    def click_your_repositories(self) -> None:
        self.wait_for_element_click(*self.your_repositories_drop_down)

    def open_repository_page(self, repository_name: str) -> None:
        repository_link = (
            By.CSS_SELECTOR, f'a[href="/{self.username}/{repository_name}"]')
        self.wait_for_element_click(*repository_link)

    def click_on_settings(self):
        self.wait_for_element_click(*self.settings_btn)

    def click_on_delete_repository_btn(self):
        self.wait_for_element_click(*self.delete_respository_btn)

    def enter_confirmation_input(self, repository_name):
        confirmation_input = f'{self.username}/{repository_name}'
        delete_repository_input = (
            By.CSS_SELECTOR,
            f'form[action="/{confirmation_input}/settings/delete"] p input[name="verify"]'
        )
        self.input_text(confirmation_input, *delete_repository_input)
        self.click_on_delete_repository_confirm_btn(confirmation_input)

    def click_on_delete_repository_confirm_btn(self, confirmation_input):
        delete_repository_confirm_btn = (
            By.CSS_SELECTOR, 
            f'form[action="/{confirmation_input}/settings/delete"] button.btn-danger.btn.btn-block'
        )
        self.wait_for_element_click(*delete_repository_confirm_btn)

    def start_repository(self, repository_name: str) -> None:
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
        print('The repository has been created')

    def delete_repository(self, repository_name: str) -> None:
        print(f'Deleting repository called {repository_name}...')
        self.open_main_page()
        self.maximize_window()
        self.click_on_sigin_btn()
        self.enter_user()
        self.enter_password()
        self.submit_sigin_data()
        self.click_user_icon()
        self.click_your_repositories()
        self.open_repository_page(repository_name)
        self.click_on_settings()
        self.click_on_delete_repository_btn()
        self.enter_confirmation_input(repository_name)
        print('The repository has been deleted')
