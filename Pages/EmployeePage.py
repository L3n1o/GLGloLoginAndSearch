from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import datetime


def calculateTotalExperience(date):
    dateStr = datetime.datetime.strptime(date, '%d-%b-%Y').strftime('%d%m%Y')
    today = datetime.date.today().strftime('%d%m%Y')

    start_date = datetime.datetime(int(dateStr[4:]), int(dateStr[2:4]), int(dateStr[:2]))
    end_date = datetime.datetime(int(today[4:]), int(today[2:4]), int(today[:2]))

    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    return str(num_months // 12) + ' Y ' + str(num_months % 12) + ' M'


class EmployeePage:

    def __init__(self, driver):
        self.driver = driver

    def employeePageCheck(self, emp_name, emp_surname):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "profile-layer")))
            if element is not None:
                title = element.find_element_by_tag_name('h2').get_attribute('title')
                if title == emp_name.capitalize() + ' ' + emp_surname.capitalize():
                    return True
                else:
                    return False
        except NoSuchElementException:
            print('Element not found')

    def checkEmployeeDateOfJoining(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "col-md-10")))
            boldInfo = element.find_elements_by_tag_name('strong')
            if re.match(r"[0-9]{2}-[A-Za-z]{3}-[0-9]{4}", boldInfo[1].text):
                if "Band" not in boldInfo[2].text:
                    return calculateTotalExperience(boldInfo[1].text) == boldInfo[2].text
                else:
                    return True
            else:
                return False
        except NoSuchElementException:
            print('Element not found')
