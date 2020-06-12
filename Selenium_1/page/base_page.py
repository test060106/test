from selenium import webdriver


class BasePage():
    def __init__(self,driver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver
