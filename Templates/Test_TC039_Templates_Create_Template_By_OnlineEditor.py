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


class Test_LE039_CreateTemplateOnlineEditor:

    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        loc = r".\LH_Sheets\TestData.xls"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("Createonlineeditor")
        list = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            Text = sheet.cell_value(r, 0)
            tuple = (Text)
            list.append(tuple)
        return list

    @pytest.mark.parametrize("Text", Sheet())
    def test_LE039_CreateTemplateOnlineEditor(self, test_setup, Text):

        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.temp = Createtemplate(self.driver)
        self.temp.ClickonTemplateButton()
        time.sleep(10)
        self.temp.ClickonOnlineEditor()
        time.sleep(10)
        self.temp.EnterOnlineEditor(Text)
        time.sleep(10)
        self.temp.ClickonSaveEditor()
        time.sleep(2)
        self.temp.EnterTemplateName()
        time.sleep(2)
        self.temp.ClickonSavetheTemplate()
        time.sleep(7)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Templates" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name=" User Created Template Succesfully By Using Online Editor",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User Created Template Succesfully*******")
                self.logger.info("Test_TC039_Templates_Create_Template_By_OnlineEditor is Passed")
                time.sleep(2)
                self.lgn.ClickUserAccount()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Create Template By Using Online Editor",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to Create Template By Using Online Editor")
                self.logger.info("Test_TC039_Templates_Create_Template_By_OnlineEditor is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()


