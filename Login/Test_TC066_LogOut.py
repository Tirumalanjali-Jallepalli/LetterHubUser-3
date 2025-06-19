import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.Login import login


class Test_Logout:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    def test_LE066_LogOut(self, test_setup):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(5)
        self.lgn.ClickUserAccount()
        time.sleep(2)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Signed Out" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User LogOut Succesfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User LogOut Succesfully*******")
                self.logger.info("Test_TC066_LogOut is Passed")
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to LogOut",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to LogOut")
                self.logger.info("Test_TC066_LogOut is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


