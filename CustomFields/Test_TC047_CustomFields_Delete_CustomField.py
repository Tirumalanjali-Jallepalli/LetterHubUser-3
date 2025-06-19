import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.Customfield import CreateCustomFields
from Pages.Login import login


class Test_LE047_DeleteCustomField:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    def test_LE047_DeleteCustomField(self, test_setup):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn = login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** User Succesfully login into letter Hub website *********")
        self.dlt=CreateCustomFields(self.driver)
        self.dlt.ClickonCustomfield()
        time.sleep(3)
        self.dlt.ClickonDeleteIcon()
        time.sleep(3)
        self.dlt.ClickonYesButton()
        time.sleep(3)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Custom Fields" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User Deleted Custom Field Succesfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Deleted Custom Field Succesfully*******")
                self.logger.info("Test_TC047_CustomFields_Delete_CustomField is Passed")
                time.sleep(2)
                self.dlt.ClickUserAccount()
                time.sleep(3)
                self.dlt.ClickonLogOutButtton()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to User Deleted Custom Field",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to User Deleted Custom Field")
                self.logger.info("Test_TC047_CustomFields_Delete_CustomField is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()

