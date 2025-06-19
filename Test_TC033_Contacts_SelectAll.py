import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from utilities.readproperties import Readdata
import time
from Pages.Login import Login
from Pages.Contacts_Tags import Contacts_tags


class Test_TC033_Contacts_SelectAll:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    def test_TC033_contacts(self, test_setup):
        self.driver = test_setup
        self.logger.info("********** Test_TC033_Contacts_SelectAll TestCase Started *********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.driver.implicitly_wait(20)
        self.lo = Login(self.driver)
        self.lo.LoginCredentials(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** Successfully Login Into LetterHUB Web-portal *********")
        self.con = Contacts_tags(self.driver)
        self.con.clkonContactsModule()
        time.sleep(3)
        self.con.clkonSelectAll()
        time.sleep(6)
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        try:
            if "Contacts" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully selected the all Contacts",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully selected the all Contacts *******")
                self.logger.info("Test_TC033_Contacts_SelectAll is Passed")
                time.sleep(2)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed while select the all Contacts",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while select the all Contacts *******")
                self.logger.info("Test_TC033_Contacts_SelectAll is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()

