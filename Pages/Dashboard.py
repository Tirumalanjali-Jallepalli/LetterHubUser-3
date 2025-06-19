from selenium.webdriver.common.by import By
from Locators.LOC_Login import Locator


class Dashboard:

    def __init__(self, driver):
        self.driver = driver

    def ClickonManageTemplate(self):
        self.driver.find_element(By.XPATH, Locator.Clickonmantempalte_xpath).click()

    def ClickOnDashboard(self):
        self.driver.find_element(By.XPATH, Locator.ClickonDashboard_xapth).click()

    def ClcikUserAccount(self):
        self.driver.find_element(By.XPATH, Locator.ClickonUseraccount_Xpath).click()

    def ClcikonLOGOUTbtn(self):
        self.driver.find_element(By.XPATH, Locator.Clickonlogout_Xpath).click()
