from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


class BasePage:

    def __init__(self, driver_path, url):
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(10)
        self.main_page = url

    def open_main_page(self):
        self.driver.get(self.main_page)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()
