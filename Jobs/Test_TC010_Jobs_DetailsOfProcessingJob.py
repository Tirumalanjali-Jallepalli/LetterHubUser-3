import time
import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.Jobs import Jobs
from Pages.Login import Login


class Test_TC010_Jobs_DetailsOfProcessingJob:

    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_Sheets\LH_DATASHEETS1.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name("Jobs_DeleteProcessingJob")
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            Status = sheet.cell_value(r, 0)
            Date = sheet.cell_value(r, 1)
            GroupBatches = sheet.cell_value(r, 2)
            Action = sheet.cell_value(r, 3)

            Tuple = (Status, Date, GroupBatches, Action)
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("Status, Date, GroupBatches, Action", Sheet())
    def test_TC010_detailsProcessingJob(self, test_setup, Status, Date, GroupBatches, Action):
        self.driver = test_setup
        self.logger.info("********** Test_TC010_Jobs_DetailsOfProcessingJob TestCase Started *********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lo = Login(self.driver)
        self.lo.LoginCredentials(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** Successfully Login Into LetterHUB Web-portal *********")
        self.job = Jobs(self.driver)
        self.driver.implicitly_wait(10)
        self.job.ClkOnJobsModule()
        time.sleep(3)
        self.job.SelStatusDrpDown(Status)
        time.sleep(3)
        self.job.SelDateDrpDown(Date)
        time.sleep(3)
        self.job.SelGroupBatchesDrpDown(GroupBatches)
        time.sleep(3)
        self.job.ClkOnProcessingJob_DetailsBtn()
        time.sleep(3)
        self.job.ClkOnRecipient()
        time.sleep(3)
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        try:
            if "Recipient" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully View the Details of ProcessingJob",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully View the Details of ProcessingJob *******")
                self.logger.info("Test_TC010_Jobs_DetailsOfProcessingJob is Passed")
                time.sleep(5)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed while Delete the Processing Job",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while Delete the Processing Job *******")
                self.logger.info("Test_TC010_Jobs_DetailsOfProcessingJob is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()
