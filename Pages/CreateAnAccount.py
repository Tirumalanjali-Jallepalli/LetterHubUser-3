from selenium.webdriver.common.by import By
from Locators.LOC_Login import Locator


class CreateAccount:

    def __init__(self, driver):
        self.driver = driver

    def ClickonCreateonAccountButton(self):
        self.driver.find_element(By.XPATH, Locator.Btn_Createanaccount_Xpath).click()

    def EnterName(self, name):
        self.driver.find_element(By.ID, Locator.Enter_Name_id).send_keys(name)

    def EnterEmail(self, email):
        self.driver.find_element(By.ID, Locator.Enter_email_id).send_keys(email)

    def EnterPassword(self, password):
        self.driver.find_element(By.ID, Locator.Enter_password_id).send_keys(password)

    def ClickonCreateAccount(self):
        self.driver.find_element(By.ID, Locator.Clk_CreateAccount_id).click()



