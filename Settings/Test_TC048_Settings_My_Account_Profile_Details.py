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


class Test_TC048_MyAccountDetails:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        loc = r".\LH_Sheets\TestData.xls"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("Updateaccount")
        list = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            Name = sheet.cell_value(r, 0)
            comp = sheet.cell_value(r, 1)
            tuple = (Name, comp)
            list.append(tuple)
        return list

    @pytest.mark.parametrize("Name, comp", Sheet())
    def test_TC048_MyAccountDetails(self, test_setup, Name, comp):
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
        self.sett.MyAccount(Name, comp)
        time.sleep(3)
        self.logger.info("********** Succesfully Updated The Profile Details*********")
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "LetterHUB" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Your Updated Profile Details Succesfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Updated Profile Details Succesfully*******")
                self.logger.info("Test_TC048_Settings_My_Account_Profile_Details is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Updated Profile Details",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Updated Profile Details")
                self.logger.info("Test_TC048_Settings_My_Account_Profile_Details is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


