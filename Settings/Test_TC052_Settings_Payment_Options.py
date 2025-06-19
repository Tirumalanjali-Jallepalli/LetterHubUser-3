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


class Test_TC052_PaymentOptions:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        loc = r".\LH_Sheets\TestData.xls"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("Paymentoption")
        list = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            amount1 = sheet.cell_value(r, 0)
            amount2 = sheet.cell_value(r, 1)
            amount3 = sheet.cell_value(r, 2)
            tuple = (amount1, amount2, amount3)
            list.append(tuple)
        return list

    @pytest.mark.parametrize("amount1, amount2, amount3", Sheet())
    def test_TC052_PaymentOptions(self, test_setup, amount1, amount2, amount3):
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
        self.sett.PaymentOptions()
        time.sleep(3)
        self.sett.ClickonDropDown1()
        time.sleep(2)
        self.sett.selectFromDrop1(amount1)
        time.sleep(2)
        self.sett.ClickonDrop2()
        time.sleep(2)
        self.sett.SelectFromDropDown2(amount2)
        time.sleep(2)
        self.sett.ClickonDropDown3()
        time.sleep(2)
        self.sett.SelectFromDropDown3(amount3)
        time.sleep(2)
        self.sett.ClickonSaveButton()
        time.sleep(2)
        self.logger.info("********** Succesfully Set The Payment Options*********")
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "LetterHUB" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="User Set The Payment Options Succesfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Set The Payment Options Succesfully*******")
                self.logger.info("Test_TC052_Settings_Payment_Options is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Set The Payment Options",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Set The Payment Options")
                self.logger.info("Test_TC052_Settings_Payment_Options is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


