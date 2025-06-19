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


class Test_TC050_DefaultReturnAddress:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        loc = r".\LH_Sheets\TestData.xls"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("Default")
        list = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            fname = sheet.cell_value(r, 0)
            compnam = sheet.cell_value(r, 1)
            Address1 = sheet.cell_value(r, 2)
            Address2 = sheet.cell_value(r, 3)
            city = sheet.cell_value(r, 4)
            state = sheet.cell_value(r, 5)
            zip = int(sheet.cell_value(r, 6))
            tuple = (fname, compnam, Address1, Address2, city, state, zip)
            list.append(tuple)
        return list

    @pytest.mark.parametrize("fname, compnam, Address1, Address2, city, state, zip", Sheet())
    def test_TC050_DefaultReturnAddress(self, test_setup, fname, compnam, Address1, Address2, city, state, zip):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** login into letter Hub website Succesfully*********")
        self.sett = Setings(self.driver)
        time.sleep(2)
        self.sett.DefaultAddress(fname, compnam, Address1, Address2, city, state, zip)
        time.sleep(3)
        self.logger.info("********** Succesfully Set The Default Return Address*********")
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        print(self.msg)
        try:
            if "LetterHUB" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Your Updated Default Return Address Succesfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Updated Default Return Address Succesfully*******")
                self.logger.info("Test_TC050_Settings_Default_Return_Address is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Updated Profile Details",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Updated Default Return Address")
                self.logger.info("Test_TC050_Settings_Default_Return_Address is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


