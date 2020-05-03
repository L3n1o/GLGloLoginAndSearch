from datetime import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def closePopUp(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
            if element is not None:
                self.driver.find_element_by_id("slideSkip").click()
        except NoSuchElementException:
            print('Element not found')

    def putEmployeeName(self, emp_name, emp_surname):
        self.driver.find_element_by_id("search").clear()
        self.driver.find_element_by_id("search").send_keys(emp_name + ' ' + emp_surname)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="results"]/ul[2]')))
        if element is not None:
            element.find_element_by_xpath('//li[@data-url="https://glo.globallogic.com/users/profile/'
                                          + emp_name
                                          + '.'
                                          + emp_surname
                                          + '#"]').click()

        #self.driver.find_element_by_id("search").send_keys(Keys.RETURN)
