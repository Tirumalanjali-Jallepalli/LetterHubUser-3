import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.SettingS import Setings
from Pages.Login import login
import xlrd


class Test_TC058_CREATEAPI:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        loc = r".\LH_Sheets\TestData.xls"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("CreateAPI")
        list = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            kee = sheet.cell_value(r, 0)
            sel = sheet.cell_value(r, 1)
            nam = sheet.cell_value(r, 2)
            tuple = (kee,sel, nam)
            list.append(tuple)
        return list

    @pytest.mark.parametrize("kee,sel, nam", Sheet())
    def test_TC058_CreateApi(self, test_setup, kee,sel, nam):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(2)
        self.logger.info("********** User Succesfully login into letter Hub website *********")
        self.sett = Setings(self.driver)
        time.sleep(3)
        self.sett.CreateApi(kee,sel, nam)
        time.sleep(2)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Templates" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User Able to Create Api Succesfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Able to Create Api Succesfully*******")
                self.logger.info("Test_TC58_Settings_Create_API Is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Create Api",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Create Api")
                self.logger.info("Test_TC58_Settings_Create_API Is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


