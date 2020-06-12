
from selenium.webdriver.common.by import By

from Selenium_1.page.base_page import BasePage
from Selenium_1.page.register import Register


class Index(BasePage):

    def goto_register(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)


    def login(self):
        pass