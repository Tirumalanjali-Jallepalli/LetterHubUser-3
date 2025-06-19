import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.TemplateS import Createtemplate
from Pages.Login import login


class Test_LE044_CloneTemplate:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    def test_LE044_Clonethetemplate(self, test_setup):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** User login into letter Hub website Sucessfully*********")
        self.temp = Createtemplate(self.driver)
        self.temp.ClickonTemplateButton()
        time.sleep(3)
        self.temp.ClickonClone()
        time.sleep(5)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Templates" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(),
                              name=" User Able To Clone The Template",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Clone The Template Succesfully*******")
                self.logger.info("Test_TC044_Templates_Clone_The_Template is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="User Failed to Clone The Template ",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Clone The Template")
                self.logger.info("Test_TC044_Templates_Clone_The_Template is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


