import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.readproperties import Readdata
from utilities.customLogger import LogGen


class Test_LE001_Home:

    baseurl = Readdata.applicationurl()
    logger = LogGen.log()

    def test_LE001(self, test_setup):
        self.logger.info("*******Test Case Started*******")
        self.driver = test_setup
        self.driver.get(self.baseurl)
        self.logger.info("*******Letter Hub Webportal is opened*******")
        time.sleep(3)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Dashboard" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User Open LetterHub Home Page Successfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Open LetterHub Home Page Successfully*******")
                self.logger.info("Test_TC001_Home_Page is Passed")
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Open LetterHub Home Page",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Open LetterHub Home Page")
                self.logger.info("Test_TC001_Home_Page is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()



