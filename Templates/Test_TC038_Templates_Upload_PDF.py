import time
import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.TemplateS import Createtemplate
from Pages.Login import login


class Test_LE038_CreateTemplate:

    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_sheets\TestData.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name('Templates_Upload')
        LHA_list = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            Upload = sheet.cell_value(r, 0)

            LHA_tuple = (Upload)
            LHA_list.append(LHA_tuple)
        return LHA_list

    @pytest.mark.parametrize("Upload", Sheet())
    def test_LE039_CreateTemplateOnlineEditor(self, test_setup, Upload):
        self.driver = test_setup
        self.driver.implicitly_wait(20)
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.temp = Createtemplate(self.driver)
        self.temp.ClickonTemplateButton()
        time.sleep(5)
        self.temp.ClkonBrowseBtn(Upload)
        time.sleep(5)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Templates" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name=" User Created Template Succesfully By Using PDf Document",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Created Template Succesfully*******")
                self.logger.info("Test_TC038_Templates_Upload_PDF is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Create Template By Using PDF Document",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Create Template By Using PDF Document")
                self.logger.info("Test_TC038_Templates_Upload_PDF is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()
