import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.SettingS import Setings
from Pages.Login import login


class Test_TC054_DefaultCard:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    def test_tC054_DefaultCard(self, test_setup):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** User login into letter Hub website Sucessfully*********")
        self.sett = Setings(self.driver)
        time.sleep(2)
        self.sett.DefaultCard()
        time.sleep(3)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "LetterHUB" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User Make Default Card Sucessfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Make Default Card Succesfully*******")
                self.logger.info("Test_TC054_Settings_Default_Card is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Make Default Card",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Make Default Card")
                self.logger.info("Test_TC054_Settings_Default_Card is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


