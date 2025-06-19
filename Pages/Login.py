from selenium.webdriver.common.by import By
from Locators.LOC_Login import Locator
import time


class login:

    def __init__(self, driver):
        self.driver = driver

    def SetUserName(self, email, password):
        self.driver.find_element(By.ID, Locator.Enteremail_id).send_keys(email)
        self.driver.find_element(By.ID, Locator.Enterpassword_id).send_keys(password)
        self.driver.find_element(By.XPATH, Locator.Clickonsignin_xpath).click()

    def ClickUserAccount(self):
        self.driver.find_element(By.XPATH, Locator.ClickonUseraccount_Xpath).click()
        self.driver.find_element(By.XPATH, Locator.Clickonlogout_Xpath).click()


class Login:

    def __init__(self, driver):
        self.driver = driver

    def LoginCredentials(self, email, password):
        self.driver.find_element(By.ID, Locator.Enteremail_id).send_keys(email)
        self.driver.find_element(By.ID, Locator.Enterpassword_id).send_keys(password)
        self.driver.find_element(By.XPATH, Locator.Clickonsignin_xpath).click()
        time.sleep(1)

    def Logout(self):
        self.driver.find_element(By.XPATH, Locator.ClickonUseraccount_Xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Locator.Clickonlogout_Xpath).click()
        time.sleep(2)




