import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from utilities.readproperties import Readdata
import time
from Pages.Login import Login
from Pages.Invoices import Invoices
import xlrd


class Test_TC071_Invoices_ViewInvoiceDetails:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_sheets\LH_DATASHEETS1.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name('Invoices')
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            account = sheet.cell_value(r, 0)
            date = sheet.cell_value(r, 1)
            status = sheet.cell_value(r, 2)
            InvoiceName = int(sheet.cell_value(r, 3))

            Tuple = (account, date, status, InvoiceName)
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("account, date, status, InvoiceName", Sheet())
    def test_TC071_InvoiceDetails(self, test_setup, account, date, status, InvoiceName):
        self.driver = test_setup
        self.logger.info("********** Test_TC071_Invoices_ViewInvoiceDetails TestCase Started *********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.driver.implicitly_wait(10)
        self.lo = Login(self.driver)
        self.lo.LoginCredentials(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** Successfully Login Into LetterHUB Web-portal *********")
        self.invoice = Invoices(self.driver)
        time.sleep(3)
        self.invoice.ClkOnInvoicesModule()
        time.sleep(3)
        self.invoice.SelInvoiceAccount(account)
        time.sleep(3)
        self.invoice.SelInvoiceDate('Today')
        time.sleep(3)
        self.invoice.SelInvoiceDate(date)
        time.sleep(3)
        self.invoice.SelInvoiceStatus(status)
        time.sleep(3)
        self.invoice.SearchInvoices('1000')
        time.sleep(3)
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        try:
            if "Invoices" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully view the Invoice Details",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully view the Invoice Details *******")
                self.logger.info("Test_TC071_Invoices_ViewInvoiceDetails is Passed")
                time.sleep(5)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed while view the Invoice Details",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while view the Invoice Details *******")
                self.logger.info("Test_TC071_Invoices_ViewInvoiceDetails is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()
