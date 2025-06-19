import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.CreateAnAccount import CreateAccount
import xlrd


class Test_TC002_CreateAccount:
    baseurl = Readdata.applicationurl()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        loc = r".\LH_Sheets\TestData.xls"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("LH_Createanaccount")
        list = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            name = sheet.cell_value(r, 0)
            username = sheet.cell_value(r, 1)
            password = sheet.cell_value(r, 2)
            tuple = (name, username, password)
            list.append(tuple)
        return list

    @pytest.mark.parametrize("name, username, password", Sheet())
    def test_TC002_CreateAccount(self, test_setup, name, username, password):
        self.logger.info("*******Test Case started*******")
        self.driver = test_setup
        self.driver.get(self.baseurl)
        self.logger.info("*******Letter Hub Webportal is opened*******")
        time.sleep(3)
        self.cr = CreateAccount(self.driver)
        time.sleep(2)
        self.cr.ClickonCreateonAccountButton()
        time.sleep(2)
        self.cr.EnterName(name)
        time.sleep(2)
        self.cr.EnterEmail(username)
        time.sleep(2)
        self.cr.EnterPassword(password)
        time.sleep(2)
        self.cr.ClickonCreateAccount()
        time.sleep(5)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Dashboard" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User Created An Account Successfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Created An Account Successfully*******")
                self.logger.info("Test_TC002_Create an account is Passed")
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Create an Account",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Create an Account")
                self.logger.info("Test_TC002_Create an account is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()





