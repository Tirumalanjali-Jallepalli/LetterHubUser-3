import time
import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.Login import Login
from Pages.Jobs import Jobs


class Test_LE007_Job:

    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_sheets\LH_DATASHEETS1.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name('Jobs_Track')
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            Status = sheet.cell_value(r, 0)
            Date = sheet.cell_value(r, 1)
            GroupBatches = sheet.cell_value(r, 2)
            address_name = sheet.cell_value(r, 3)

            Tuple = (Status, Date, GroupBatches, address_name)
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("Status, Date, GroupBatches, address_name", Sheet())
    def test_LE007_Job(self, test_setup, Status, Date, GroupBatches, address_name):
        self.driver = test_setup
        self.driver.implicitly_wait(20)
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lo = Login(self.driver)
        self.lo.LoginCredentials(self.username, self.password)
        time.sleep(5)
        self.job = Jobs(self.driver)
        self.job.ClkOnJobsModule()
        time.sleep(5)
        self.job.SelStatusDrpDown(Status)
        time.sleep(3)
        self.job.SelDateDrpDown(Date)
        time.sleep(3)
        self.job.ClkOnTrack(address_name)
        time.sleep(4)
        self.msg = self.driver.find_element(By.TAG_NAME, "body").get_attribute('textContent')
        # print(self.msg)
        try:
            if address_name in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully Track the job information",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully Track the job information *******")
                self.logger.info("Test_TC013_1_Jobs_Track_The_Job_Information.py is Passed")
                time.sleep(4)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed while Track the job information",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while Track the job information *******")
                self.logger.info("Test_TC013_1_Jobs_Track_The_Job_Information.py is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()

