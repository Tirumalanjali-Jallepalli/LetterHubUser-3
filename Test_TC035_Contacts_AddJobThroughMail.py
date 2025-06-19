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


class Test_LE035_AddJobMail:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        loc = r".\LH_Sheets\TestData.xls"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("Textwideview")
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            name = sheet.cell_value(r, 0)
            ForwardEmail = sheet.cell_value(r, 1)
            UpdateAddress = sheet.cell_value(r, 2)
            Notes = sheet.cell_value(r, 3)
            Address = sheet.cell_value(r, 4)
            City = sheet.cell_value(r, 5)
            State = sheet.cell_value(r, 6)
            Zip = int(sheet.cell_value(r, 7))
            upload = sheet.cell_value(r, 11)

            Tuple = (name, ForwardEmail, UpdateAddress, Notes, Address, City, State, Zip, upload)
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("name, ForwardEmail, UpdateAddress, Notes, Address, City, State, Zip, upload", Sheet())
    def test_LE035_AddJobMail(self, test_setup, name, ForwardEmail, UpdateAddress, Notes, Address, City, State, Zip, upload):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn = login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.job = Jobpdf(self.driver)
        self.driver.implicitly_wait(20)
        self.job.ClickonConatcts(name)
        time.sleep(5)
        self.job.ChangeOfAddress(ForwardEmail, UpdateAddress)
        time.sleep(3)
        self.job.ClkOnOnlineEditor()
        time.sleep(10)
        self.job.CreateOnlineFormat(Notes)
        time.sleep(10)
        self.job.TextWideView(Address, City, State, Zip, upload)
        time.sleep(2)
        self.job.ClickAddButton()
        time.sleep(5)
        self.job.ReviewAndConfirm()
        time.sleep(5)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Buy Credit" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail Added Successfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Mailed Job Successfully*******")
                self.logger.info("Test_TC035_Contacts_AddJobThroughMail Is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Mail Failed to Add",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Mail Job")
                self.logger.info("Test_TC035_Contacts_AddJobThroughMail Is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


