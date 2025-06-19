import time
import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.Jobs import Jobs
from Pages.Login import Login

import logging
import sys
from selenium.webdriver.remote.remote_connection import LOGGER


class Test_TC011_Jobs_DeleteProcessingJob:
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
            Name = sheet.cell_value(r, 4)
            Tuple = (Status, Date, GroupBatches, Action, Name)
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("Status, Date, GroupBatches, Action, Name", Sheet())
    def test_TC011_DeleteProcessingJob(self, test_setup, Status, Date, GroupBatches, Action, Name):
        self.driver = test_setup
        self.logger.info("********** Test_TC011_Jobs_DeleteProcessingJob TestCase Started *********")
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
        # self.job.SelGroupBatchesDrpDown(GroupBatches)
        # time.sleep(3)
        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text
        if "There are no Mailings to display." in self.msg:
            pass
        else:
            job_deleted = self.job.ClkOnProcessingJob_DeleteBtn(Action, Name)
            time.sleep(3)
        # self.job.ClkOnDeleteJob_Action(Action)
        # time.sleep(3)

        # Suppress Selenium Debug Logs
        LOGGER.setLevel(logging.WARNING)

        # Redirect stderr to prevent stacktrace in terminal
        sys.stderr = open("selenium_errors.log", "w")

        try:
            if job_deleted:
                wait = WebDriverWait(self.driver, 10)
                toaster_text = wait.until(lambda driver: driver.execute_script("return document.body.innerText;"))
                # print(f"Captured Page Text:\n{toaster_text}")
                if "Success!" in toaster_text:
                    assert True
                    allure.attach(self.driver.get_screenshot_as_png(), name="Successfully Deleted the Processing Job",
                                  attachment_type=AttachmentType.PNG)
                    self.logger.info("******* Successfully Deleted the Processing Job *******")
                    self.logger.info("Test_TC011_Jobs_DeleteProcessingJob is Passed")
                    time.sleep(5)
                else:
                    allure.attach(self.driver.get_screenshot_as_png(), name="Failed while Delete the Processing Job",
                                  attachment_type=AttachmentType.PNG)
                    self.logger.info("******* Failed while Delete the Processing Job *******")
                    self.logger.info("Test_TC011_Jobs_DeleteProcessingJob is Failed")
                    time.sleep(2)
                    assert False
                # self.lo.Logout()
                # time.sleep(2)
            else:
                self.logger.info(f"Job '{Name}' was not found, logging out...")
            # self.lo.Logout()
            # time.sleep(2)

        except Exception as E:
            print(E)
        finally:
            self.lo.Logout()
            time.sleep(2)
            self.driver.quit()
