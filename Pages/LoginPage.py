from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def getPage(self):
        self.driver.get("https://glo.globallogic.com/apps/glo/login")

    def putUsername(self, username):
        self.driver.find_element_by_id("login").clear()
        self.driver.find_element_by_id("login").send_keys(username)

    def putPassword(self, password):
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_css_selector(".btn-block[value='LOGIN']").click()
