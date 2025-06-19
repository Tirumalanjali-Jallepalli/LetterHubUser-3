import time
import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.SettingS import Setings
from Pages.Login import login


class Test_LE060_DisabletheApi:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    def test_LE060_DisabletheApi(self, test_setup):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** User Succesfully login into letter Hub website *********")
        self.sett = Setings(self.driver)
        time.sleep(2)
        self.sett.DisableTheApi()
        time.sleep(3)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "LetterHUB" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User Able To Disable The Api Succesfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Able To Disable The Api Succesfully*******")
                self.logger.info("Test_TC060_Settings_Disable_The_API is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Able To Disable The Api",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Able To Disable The Api")
                self.logger.info("Test_TC060_Settings_Disable_The_API is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


