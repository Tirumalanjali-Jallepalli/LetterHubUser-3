import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from utilities.readproperties import Readdata
import time
from Pages.Login import Login
from Pages.Contacts_NewContact import Contacts


class Test_TC036_Contacts_HideContacts:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    def test_TC036_HideContact(self, test_setup):
        self.driver = test_setup
        self.logger.info("********** Test_TC036_Contacts_SeeHideContacts TestCase Started *********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.driver.implicitly_wait(15)
        self.lo = Login(self.driver)
        self.lo.LoginCredentials(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** Successfully Login Into LetterHUB Web-portal *********")
        self.con = Contacts(self.driver)
        self.con.clkonContactsModule()
        time.sleep(3)
        self.con.UnCheckHideContacts()
        time.sleep(5)
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        try:
            if "Hide Contacts Without an Address" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully view the Hide Contacts Without an"
                                                                        " Address", attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully view the Hide Contacts Without an Address *******")
                self.logger.info("Test_TC036_SeeHideContacts is Passed")
                time.sleep(2)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed view the Hide Contacts Without an "
                                                                        "Address", attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed view the Hide Contacts Without an Address *******")
                self.logger.info("Test_TC036_SeeHideContacts is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()

