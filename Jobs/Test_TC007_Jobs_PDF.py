import time
import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.Jobs_PDF import Jobpdf
from Pages.Login import login


class Test_LE007_Job:

    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():

        loc = r".\LH_Sheets\TestData.xls"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("Jobs_PDF")
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            name = sheet.cell_value(r, 0)
            ForwardEmail = sheet.cell_value(r, 2)
            UpdateAddress = sheet.cell_value(r, 3)
            text = sheet.cell_value(r, 4)
            Name1 = sheet.cell_value(r, 5)
            Company = sheet.cell_value(r, 6)
            Add1 = sheet.cell_value(r, 7)
            Add2 = sheet.cell_value(r, 8)
            City = sheet.cell_value(r, 9)
            State = sheet.cell_value(r, 10)
            Zip = int(sheet.cell_value(r, 11))
            Upload = sheet.cell_value(r, 12)

            Tuple = (name, ForwardEmail, UpdateAddress, text, Name1, Company, Add1, Add2, City, State, Zip, Upload)
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("name, ForwardEmail, UpdateAddress, text, Name1, Company, Add1, Add2, City, State, Zip, Upload", Sheet())
    def test_LE007_Job(self, test_setup, name, ForwardEmail, UpdateAddress, text, Name1, Company, Add1,
                       Add2, City, State, Zip, Upload):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(5)
        self.lgn = login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(5)
        self.job = Jobpdf(self.driver)
        self.driver.implicitly_wait(20)
        time.sleep(5)
        self.job.ClickonJobsButton(name)
        time.sleep(5)
        self.job.ChangeOfAddress(ForwardEmail, UpdateAddress)
        time.sleep(5)
        self.job.ClkonBrowseButton(Upload)
        time.sleep(10)
        self.job.SelectFromAddress(Name1, Company, Add1, Add2, City, State, Zip)
        time.sleep(5)
        self.job.ReviewAndConfirm()
        time.sleep(5)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Buy Credit" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Job Added Successfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Added Job Succesfully*******")
                self.logger.info("Test_TC007_Jobs_PDF Is Passed")
                time.sleep(5)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Job Failed to Add",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Add Job")
                self.logger.info("Test_TC007_Jobs_PDF Is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()
