import time
import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.Assisted_job import AssistedJob
from Pages.Login import Login



class Test_TC014_AssistedJob:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_Sheets\LH_DATASHEETS1.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name("AssistedJob")
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            mainPDF = sheet.cell_value(r, 0)
            backPDF = sheet.cell_value(r, 1)
            JobName = sheet.cell_value(r, 2)
            EmailPhone = sheet.cell_value(r, 3)
            ToAddress = sheet.cell_value(r, 4)
            AddType = sheet.cell_value(r, 5)
            ImagePath = sheet.cell_value(r, 6)
            Carrier = sheet.cell_value(r, 7)
            PageSize = sheet.cell_value(r, 8)
            Envelope = sheet.cell_value(r, 9)
            PrintOption = sheet.cell_value(r, 10)
            ForwardEmail = sheet.cell_value(r, 11)
            UpdateAddress = sheet.cell_value(r, 12)
            PayOption = sheet.cell_value(r, 13)

            Tuple = (mainPDF, backPDF, JobName, EmailPhone, ToAddress, AddType, ImagePath, Carrier, PageSize, Envelope,
                     PrintOption, ForwardEmail, UpdateAddress, PayOption)
            List.append(Tuple)

        return List

    @pytest.mark.parametrize("mainPDF, backPDF, JobName, EmailPhone, ToAddress, AddType, ImagePath, Carrier, PageSize, "
                             "Envelope, PrintOption, ForwardEmail, UpdateAddress, PayOption", Sheet())
    def test_TC014_AssistedJob(self, test_setup, mainPDF, backPDF, JobName, EmailPhone, ToAddress, AddType, ImagePath,
                         Carrier, PageSize, Envelope, PrintOption, ForwardEmail, UpdateAddress, PayOption):
        self.driver = test_setup
        self.logger.info("********** Test_TC014_AssistedJob TestCase Started *********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lo = Login(self.driver)
        self.lo.LoginCredentials(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** Successfully Login Into LetterHUB Web-portal *********")
        self.job = AssistedJob(self.driver)
        self.driver.implicitly_wait(10)
        self.job.clkonJobsBtn()
        time.sleep(10)
        self.job.clkonAutoInvoiceScannerBtn()
        time.sleep(5)
        self.job.selMainPdf(mainPDF)
        time.sleep(3)
        self.job.selBackPdf(backPDF)
        time.sleep(3)
        self.job.clkonNextBtn()
        time.sleep(10)
        self.job.clkonOkBtn()
        time.sleep(3)
        self.job.EntJobName(JobName)
        time.sleep(2)
        self.job.entEmailPhone(EmailPhone)
        time.sleep(3)
        self.job.UncheckToAddress(ToAddress)
        time.sleep(2)
        self.job.ClkOnAddNewFromAddress()
        time.sleep(3)
        self.job.SelAddressType(AddType)
        time.sleep(3)
        self.job.BrowseTheImage(ImagePath)
        time.sleep(3)
        # self.job.AddNewAddress('xyz', 'DIT', 'baba-road', 'OKReddyBuilding', 'GNT', 'AP', '522022')
        self.job.TextUnderWideImage('OKReddyBuilding', 'GNT', 'AP', '522022')
        time.sleep(2)
        # self.job.ClkOnUseDefaultFromAddress()
        time.sleep(5)
        self.job.CheckReturnAddress()
        time.sleep(3)
        self.job.SelCarrier(Carrier)
        # time.sleep(3)
        # self.job.ClkOnRequiredCheckBox('One business day processing')
        time.sleep(3)
        self.job.SelPageSize(PageSize)
        time.sleep(3)
        self.job.SelReturnEnvelope(Envelope)
        time.sleep(3)
        self.job.SelPrintOptions(PrintOption)
        time.sleep(3)
        self.job.SelChangeOfAddressRadioBtns(ForwardEmail, UpdateAddress)
        time.sleep(3)
        self.job.SelPaymentOption(PayOption)
        time.sleep(5)
        # self.job.SelChargeMyCreditCard(CardName)
        # time.sleep(5)
        self.job.ClkOnSubmitTheJob()
        time.sleep(5)
        self.job.ClkOnOkBtn()
        time.sleep(5)
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        try:
            if "Buy Credit" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="Successfully submit the Job Through Assisted Job", attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully submit the Job Through Assisted Job *******")
                self.logger.info("Test_TC014_AssistedJob.py is Passed")
                time.sleep(2)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="Failed while submit the Job Through Assisted Job", attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while submit the Job Through Assisted Job *******")
                self.logger.info("Test_TC014_AssistedJob.py is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()
