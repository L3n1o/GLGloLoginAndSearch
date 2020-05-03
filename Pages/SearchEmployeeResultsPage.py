from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchEmployeeResultsPage:

    def __init__(self, driver):
        self.driver = driver

    def chooseEmployee(self, emp_name, emp_surname):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'user_list')))
            self.driver.find_element_by_link_text(emp_name.capitalize() + ' ' + emp_surname.capitalize()).click()
        except NoSuchElementException:
            print('Element not found')
