import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.Dashboard import Dashboard
from Pages.Login import login


class Test_LoginPage:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    def test_LE003_login(self, test_setup):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.dash = Dashboard(self.driver)
        self.dash.ClickonManageTemplate()
        time.sleep(3)
        self.dash.ClickOnDashboard()
        time.sleep(3)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Dashboard" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User able to view Dashboard",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Logged In Succesfully*******")
                self.logger.info("Test_TC006_Dashboard is Passed")
                time.sleep(2)
                self.dash.ClcikUserAccount()
                time.sleep(3)
                self.dash.ClcikonLOGOUTbtn()
                time.sleep(3)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User unable to view Dashboard",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Login")
                self.logger.info("Test_TC006_Dashboard is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()