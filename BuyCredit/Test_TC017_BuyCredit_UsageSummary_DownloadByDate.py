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


class Test_TC017_UsageSummary_DownloadByDate:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_sheets\LH_DATASHEETS1.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name("UsageSummaryDetails1")
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            category = sheet.cell_value(r, 0)
            Tuple = category
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("category", Sheet())
    def test_TC017_UsageSummary(self, test_setup, category):
        self.driver = test_setup
        self.logger.info("********** Test_TC017_BuyCredit_UsageSummary_DownloadByDate TestCase Started *********")
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
        time.sleep(2)
        # self.us.sel_customRange('05/25/2022', '06/01/2022')
        self.us.sel_dateDrp(category)
        time.sleep(5)
        self.us.ClkOnDownloadUsageSummaryByDate()
        time.sleep(2)
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        try:
            if "Download Usage Summary By Date" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully downloaded Usage summary By date",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully downloaded Usage summary By date *******")
                self.logger.info("Test_TC017_BuyCredit_UsageSummary_DownloadByDate is Passed")
                time.sleep(2)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed while downloaded Usage summary By date",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while downloaded Usage summary By date *******")
                self.logger.info("Test_TC017_BuyCredit_UsageSummary_DownloadByDate is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()




