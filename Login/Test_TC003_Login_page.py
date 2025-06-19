import time
import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.Login import login


class Test_TC003_login:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        loc = r".\LH_Sheets\TestData.xls"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("login")
        list = []
        print(sheet.row_values(1))
        rows = sheet.nrows
        for r in range(1, rows, 1):
            username = sheet.cell_value(r, 0)
            password = sheet.cell_value(r, 1)
            tuple = (username, password)
            list.append(tuple)
        return list

    @pytest.mark.parametrize("username, password", Sheet())
    def test_TC003_login(self, test_setup, username, password):
        self.driver = test_setup
        self.logger.info("********** Started Letter Hub Application *********")
        self.driver.get(self.baseurl)
        self.le =login(self.driver)
        time.sleep(3)
        self.le.SetUserName(username, password)
        self.logger.info("********** Entered the Login Details *********")
        time.sleep(3)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Dashboard" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User Logged in Successfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Logged in Successfully*******")
                self.logger.info("Test_TC003_Loginpage is Passed")
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Login",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Login")
                self.logger.info("Test_TC003_Loginpage is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


