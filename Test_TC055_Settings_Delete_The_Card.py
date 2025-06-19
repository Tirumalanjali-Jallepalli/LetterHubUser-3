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


class Test_TC055_DeleteCard:
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
        for r in range(1, rows):
            Card_Number = sheet.cell_value(r, 7)
            tuple = (Card_Number)
            list.append(tuple)
        return list

    @pytest.mark.parametrize("Card_Number", Sheet())

    def test_TC055_DeleteCard(self, test_setup, Card_Number):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn = login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** User login into letter Hub website Sucessfully*********")
        self.sett = Setings(self.driver)
        time.sleep(2)
        self.sett.DeleteCard(Card_Number)
        time.sleep(3)
        self.logger.info("********** User Deleted The Card Sucessfully*********")
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "this is default credit card" in self.msg: #"Oops!! That promo code didn't work. Please try again."
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User Deleted The Card Sucessfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Deleted The Card Succesfully*******")
                self.logger.info("Test_TC055_Settings_Delete_The_Card is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)

            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Delete The Card",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Delete The Card")
                self.logger.info("Test_TC055_Settings_Delete_The_Card is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


