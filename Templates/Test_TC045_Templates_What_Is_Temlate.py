import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.TemplateS import Createtemplate
from Pages.Login import login


class Test_LE045_WhatIsTemplate:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    def test_LE045_WhatIsthetemplate(self, test_setup):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.temp = Createtemplate(self.driver)
        self.temp.ClickonTemplateButton()
        time.sleep(3)
        self.temp.ClickonWhat_Template_Button()
        time.sleep(2)
        self.temp.Clickon_X_Button_Whatis_Template()
        time.sleep(3)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Templates" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="User View What Is Template",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User View What Is Template Succesfully*******")
                self.logger.info("Test_TC045_Templates_What_Is_Temlate is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="User Failed to Clone The Template ",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to View What Is Template")
                self.logger.info("Test_TC045_Templates_What_Is_Temlate is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


