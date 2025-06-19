from selenium.webdriver.common.by import By
from Locators.LOC_Login import Locator


class Rememberme:

    def __init__(self, driver):
        self.driver = driver

    def UserName(self, email, password):
        self.driver.find_element(By.ID, Locator.Enteremail_id).send_keys(email)
        self.driver.find_element(By.ID, Locator.Enterpassword_id).send_keys(password)

    def ClklonSignIn(self):
        self.driver.find_element(By.XPATH, Locator.Clickonsignin_xpath).click()

    def ClickUserAccount(self):
        self.driver.find_element(By.XPATH, Locator.ClickonUseraccount_Xpath).click()
        self.driver.find_element(By.XPATH, Locator.Clickonlogout_Xpath).click()

    def ClickRememberMeButton(self):
        self.driver.find_element(By.XPATH, Locator.ClickonRememberme_Btn_Xpath).click()

    def ClcikUserAccount(self):
        self.driver.find_element(By.XPATH, Locator.ClickonUseraccount_Xpath).click()

    def ClcikonLOGOUTbtn(self):
        self.driver.find_element(By.XPATH, Locator.Clickonlogout_Xpath).click()

    def ClkonClickHereButton(self):
        self.driver.find_element(By.XPATH, Locator.ClickonClickhere_Xpath).click()


