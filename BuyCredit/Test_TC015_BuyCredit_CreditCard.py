import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from utilities.readproperties import Readdata
import time
from Pages.Login import Login
from Pages.BuyCredit import BuyCredits
import xlrd
from selenium.webdriver.support.ui import WebDriverWait


class Test_TC015_BuyCredit:

    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_sheets\LH_DATASHEETS1.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name('BuyCredit_CreditCard')
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            creditAmt = sheet.cell_value(r, 0)
            fname = sheet.cell_value(r, 1)
            lname = sheet.cell_value(r, 2)
            cardNo = sheet.cell_value(r, 3)
            expirydate = sheet.cell_value(r, 4)
            code = int(sheet.cell_value(r, 5))
            Tuple = (creditAmt, fname, lname, cardNo, expirydate, code)
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("creditAmt, fname, lname, cardNo, expirydate, code", Sheet())
    def test_TC015_BuyCredit(self, test_setup, creditAmt, fname, lname, cardNo, expirydate, code):
        self.driver = test_setup
        self.logger.info("********** Test_TC015_BuyCredit_CreditCard TestCase Started *********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.driver.implicitly_wait(10)
        self.lo = Login(self.driver)
        self.lo.LoginCredentials(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** Successfully Login Into LetterHUB Web-portal *********")
        self.buy = BuyCredits(self.driver)
        time.sleep(3)
        self.buy.ClkOnBuyCreditModule()
        time.sleep(2)
        self.buy.Clk_creditAmt_drp()
        time.sleep(2)
        self.buy.selectCreditAmt(creditAmt)
        time.sleep(5)
        self.buy.selectanotherCard(fname, lname, cardNo, expirydate, code)
        time.sleep(2)
        self.buy.clk_BuyCredit()
        time.sleep(8)
        # self.driver.close()
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        try:
            if "Success!" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Buy the Credits through Credit Card "
                                                                        "Successfully", attachment_type=AttachmentType.PNG)
                self.logger.info("******* Buy the Credits through Credit Card Successfully *******")
                self.logger.info("Test_TC0015_BuyCredit_CreditCard is Passed")
                time.sleep(5)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed Buy Credits through Credit Card",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed Buy Credits through Credit Card *******")
                self.logger.info("Test_TC0015_BuyCredit_CreditCard is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()
