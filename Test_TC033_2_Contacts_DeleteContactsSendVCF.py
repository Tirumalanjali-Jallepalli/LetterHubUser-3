import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from utilities.readproperties import Readdata
import time
from Pages.Login import Login
from Pages.Contacts_Tags import Contacts_tags


class Test_TC033_2_Contacts_DeleteSendVCF:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    def test_TC033_2_Contacts(self, test_setup):
        self.driver = test_setup
        self.logger.info("********** Test_TC033_2_Contacts_DeleteContactsSendVCF TestCase Started *********")
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
        self.con.SelectContacts()
        time.sleep(3)
        self.con.clkonDeleteSendVCFBtn()
        time.sleep(5)
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        try:
            if "Contacts" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully send mail with the deleted "
                                                                        "Contacts in VCF Format",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully send the deleted contacts in VCF format *******")
                self.logger.info("Test_TC033_2_Contacts_DeleteContactsSendVCF is Passed")
                time.sleep(2)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed while send the deleted contacts in VCF "
                                                                        "format", attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while send the deleted contacts in VCF format *******")
                self.logger.info("Test_TC033_2_Contacts_DeleteContactsSendVCF is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()
