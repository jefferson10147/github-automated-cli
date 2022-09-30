from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
    Selenium base class with all primitive configuration and actions
    """

    def __init__(self, driver_path, url):
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        self.main_page = url

    def open_main_page(self):
        self.driver.get(self.main_page)

    def end_test(self):
        self.driver.quit()

    def maximize_window(self):
        self.driver.maximize_window()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def wait_for_element_click(self, *locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
