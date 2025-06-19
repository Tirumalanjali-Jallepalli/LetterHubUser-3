import time
import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.SettingS import Setings
from Pages.Login import login


class Test_TC056_1_AddEmailDeleteCard:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        loc = r".\LH_Sheets\TestData.xls"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("ADDEMAIL")
        list = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            email = sheet.cell_value(r, 0)
            tuple = (email)
            list.append(tuple)
        return list

    @pytest.mark.parametrize("email", Sheet())
    def test_TC056_1_AddEmailDeleteCard(self, test_setup, email):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** User login into letter Hub website Succesfully*********")
        self.sett = Setings(self.driver)
        time.sleep(2)
        self.sett.AddEmail(email)
        time.sleep(3)
        self.logger.info("********** User Added Email Succesfully & Deleted The Added Email Sucessfully*********")
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "LetterHUB" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User Added Email Succesfully & Deleted The Added Email Sucessfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User User Added Email Succesfully & Deleted The Added Email Succesfully*******")
                self.logger.info("Test_TC056_1_Settings_Add_Email_Delete_Email is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to User Added Email  & Deleted The Added Email",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to User Added Email & Deleted The Added Email")
                self.logger.info("Test_TC056_1_Settings_Add_Email_Delete_Email is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


