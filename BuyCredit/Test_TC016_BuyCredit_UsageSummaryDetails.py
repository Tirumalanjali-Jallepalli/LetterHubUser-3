import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from utilities.readproperties import Readdata
import time
from Pages.Login import Login
from Pages.BuyCredit_UsageSummary import UsageSummary


class Test_TC016_UsageSummary:

    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_sheets\LH_DATASHEETS1.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name("Sheet21")
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            # category = sheet.cell_value(r, 0)
            fromDate = sheet.cell_value(r, 0)
            toDate = sheet.cell_value(r, 1)

            Tuple = (fromDate, toDate)
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("fromDate, toDate", Sheet())
    def test_TC016_UsageSummary(self, test_setup, fromDate, toDate):
        self.driver = test_setup
        self.logger.info("********** Test_TC016_BuyCredit_UsageSummaryDetails TestCase Started *********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.driver.implicitly_wait(10)
        self.lo = Login(self.driver)
        self.lo.LoginCredentials(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** Successfully Login Into LetterHUB Web-portal *********")
        self.us = UsageSummary(self.driver)
        self.us.ClkOnBuyCreditModule()
        time.sleep(2)
        self.us.ClkOnUsageSummary()
        time.sleep(5)
        self.us.clkDateDrp()
        time.sleep(3)
        self.us.ClkOnCustomRange(fromDate, toDate)
        # self.us.sel_dateDrp(category)
        time.sleep(5)
        # self.driver.close()
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        try:
            if "Download Usage Summary By Date" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully view the Usage Summary details",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully view the Buy Credits Usage Summary details *******")
                self.logger.info("Test_TC016_BuyCredit_UsageSummaryDetails is Passed")
                time.sleep(2)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed while view the Usage Summary details",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while view the Usage Summary details *******")
                self.logger.info("Test_TC016_BuyCredit_UsageSummaryDetails is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            # self.lo.logout()
            self.driver.quit()
