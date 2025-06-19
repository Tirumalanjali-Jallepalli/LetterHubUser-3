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


class Test_TC053_AddNewCard:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        loc = r".\LH_Sheets\TestData.xls"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("Addnewcard")
        list = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            crdnum = int(sheet.cell_value(r, 0))
            fnam = sheet.cell_value(r, 1)
            lnam = sheet.cell_value(r, 2)
            exp = int(sheet.cell_value(r, 3))
            scty = int(sheet.cell_value(r, 4))
            tuple = (crdnum, fnam, lnam, exp, scty)
            list.append(tuple)
        return list

    @pytest.mark.parametrize("crdnum, fnam, lnam, exp, scty", Sheet())
    def test_TC053_AddNewCard(self, test_setup, crdnum, fnam, lnam, exp, scty):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** login into letter Hub website Sucessfully*********")
        self.sett = Setings(self.driver)
        time.sleep(2)
        self.sett.AddNewCard(crdnum, fnam, lnam, exp, scty)
        time.sleep(3)
        self.logger.info("********** User Added NewCard Details Sucessfully*********")
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "LetterHUB" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User AddNewCard Succesfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User AddNewCard Succesfully*******")
                self.logger.info("Test_TC053_Settings_ADD_NEW_CARD is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to AddNewCard",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to AddNewCard")
                self.logger.info("Test_TC053_Settings_ADD_NEW_CARD is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


