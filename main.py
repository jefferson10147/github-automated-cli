from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


def main():
    service = Service('./chromedriver')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://www.google.com')
    driver.find_element(By.NAME, 'q').send_keys('Selenium', Keys.RETURN)
    driver.quit()


if __name__ == '__main__':
    main()
