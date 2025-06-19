from selenium.webdriver.common.by import By
from Locators.LOC_Logout import Logout
import time


class logout:

    def __init__(self, driver):
        self.driver = driver

    def Support(self):

        self.driver.find_element(By.XPATH, Logout.CLkonuser_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Logout.Clkonsupt_xpath).click()
        time.sleep(3)


