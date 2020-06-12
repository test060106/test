from selenium.webdriver.common.by import By

from Selenium_1.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.driver.find_element(By.CSS_SELECTOR,"#corp_name").send_keys("hello")
        self.driver.find_element(By.CSS_SELECTOR,"#manager_name").send_keys("nihao")

