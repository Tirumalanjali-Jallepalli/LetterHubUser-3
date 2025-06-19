import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.Rememberme import Rememberme


class Test_TC003_RememberMe:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    def test_TC003_RememberMe(self, test_setup):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =Rememberme(self.driver)
        self.lgn.UserName(self.username, self.password)
        time.sleep(2)
        self.remb = Rememberme(self.driver)
        self.remb.ClickRememberMeButton()
        time.sleep(3)
        self.lgn.ClklonSignIn()
        time.sleep(3)
        self.remb.ClcikUserAccount()
        time.sleep(3)
        self.remb.ClcikonLOGOUTbtn()
        time.sleep(2)
        self.remb.ClkonClickHereButton()
        time.sleep(3)
        self.lgn.ClklonSignIn()
        time.sleep(5)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Dashboard" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User Logined Succesfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Logined Succesfully*******")
                self.logger.info("Test_TC005_Remember Me is Passed")
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Create an account",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Login")
                self.logger.info("Test_TC005_RememberMe is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()