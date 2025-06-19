import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.LOGOUT import logout
from Pages.Login import login


class Test_Updateaccount:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    def test_LE046_Createcustomfield(self, test_setup):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.set = logout(self.driver)
        time.sleep(10)
        self.set.Support()
        time.sleep(5)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Dashboard" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User Get Support Information Succesfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Get Support Information Succesfully*******")
                self.logger.info("Test_TC064_Support is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Get Support Information",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Get Support Information")
                self.logger.info("Test_TC064_Support is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


