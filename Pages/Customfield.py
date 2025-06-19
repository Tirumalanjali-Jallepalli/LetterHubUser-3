import string
import random
from selenium.webdriver.common.by import By
from Locators.LOC_CustomFields import customfields
from Locators.LOC_Login import Locator
from utilities.customLogger import LogGen


class CreateCustomFields:
    logger = LogGen.log()

    def __init__(self, driver):
        self.driver = driver

    def ClickonCustomfield(self):
        self.driver.find_element(By.XPATH, customfields.Clkoncustom_xpath).click()

    def ClickonCreateNewField(self):
        self.driver.find_element(By.XPATH, customfields.Clkoncreatenewcustom_xpath).click()

    def ClickonDropDown(self):
        self.driver.find_element(By.XPATH, customfields.clkondropdownsltfieldtype_xpath).click()

    def selectFromDropDown(self, text):
        fo = self.driver.find_elements(By.XPATH, customfields.selectfromdropdown_xpath)
        for ele in fo:
            if ele.text == text:
                ele.click()
                break

    def EntFieldNam(self):
        self.name = ''.join(random.choice(string.ascii_lowercase) for x in range(8))
        self.driver.find_element(By.ID, customfields.Entcustomfldname_id).send_keys(self.name)

    def ClickonSaveButton(self):
        self.driver.find_element(By.XPATH, customfields.Clkonsav_xpath).click()

    def ClickonClose(self):
        self.driver.find_element(By.XPATH, customfields.Clkonclose_xapth).click()

    def ClickonDeleteIcon(self):
        self.driver.find_element(By.XPATH, customfields.Clkondeleteicon_xpath).click()

    def ClickonYesButton(self):
        self.driver.find_element(By.XPATH, customfields.ClkonYespopup_xpath).click()

    def ClickUserAccount(self):
        self.driver.find_element(By.XPATH, Locator.ClickonUseraccount_Xpath).click()

    def ClickonLogOutButtton(self):
        self.driver.find_element(By.XPATH, Locator.Clickonlogout_Xpath).click()

