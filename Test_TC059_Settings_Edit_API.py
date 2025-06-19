import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.SettingS import Setings
from Pages.Login import login


class Test_TC059_EditApi:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    def test_TC059_EditApi(self, test_setup):
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
        self.sett.EditApi()
        time.sleep(3)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "LetterHUB" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User Edited The Api Details Succesfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Edited The Api Details Succesfully*******")
                self.logger.info("Test_TC059_Settings_Edit_API is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Edited The Api Details",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Edited The Api Details")
                self.logger.info("Test_TC059_Settings_Edit_API is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


