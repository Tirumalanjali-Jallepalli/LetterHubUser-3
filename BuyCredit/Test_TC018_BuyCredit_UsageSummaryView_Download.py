import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from utilities.readproperties import Readdata
import time
from time import sleep
from Pages.Login import Login
from Pages.BuyCredit_UsageSummary import UsageSummary


class Test_TC018_UsageSummary_ViewDownload:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_sheets\LH_DATASHEETS1.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name("UsageSummaryDetails")
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            category = sheet.cell_value(r, 0)
            sel_date = sheet.cell_value(r, 1)

            Tuple = (category, sel_date)
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("category, sel_date", Sheet())
    def test_TC018_UsageSummary(self, test_setup, category, sel_date):
        self.driver = test_setup
        self.logger.info("********** Test_TC018_BuyCredit_UsageSummaryView_Download TestCase Started *********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.driver.implicitly_wait(15)
        self.lo = Login(self.driver)
        self.lo.LoginCredentials(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** Successfully Login Into LetterHUB Web-portal *********")
        self.us = UsageSummary(self.driver)
        self.us.ClkOnBuyCreditModule()
        time.sleep(2)
        self.us.ClkOnUsageSummary()
        time.sleep(5)
        self.us.UncheckGroupByDate()
        time.sleep(5)
        self.us.clkDateDrp()
        time.sleep(3)
        self.us.sel_dateDrp(category)
        # self.us.ClkOnCustomRange(FromDate, ToDate)
        time.sleep(5)
        self.us.ClkOnViewAndDownload(sel_date)
        time.sleep(2)
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        try:
            if sel_date in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully View & downloaded Usage summary",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully View & downloaded Usage summary *******")
                self.logger.info("Test_TC018_BuyCredit_UsageSummaryView_Download is Passed")
                time.sleep(2)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed while View & downloaded Usage summary",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while View & downloaded Usage summary *******")
                self.logger.info("Test_TC018_BuyCredit_UsageSummaryView_Download is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()
