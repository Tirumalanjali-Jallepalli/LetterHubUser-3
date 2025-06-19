import time
import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.readproperties import Readdata
from utilities.customLogger import LogGen
from Pages.Customfield import CreateCustomFields
from Pages.Login import login


class Test_LE046_CreateNewCustomField:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        loc = r".\LH_Sheets\TestData.xls"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("CreateCustomfield")
        list = []
        print(sheet.row_values(1))
        rows = sheet.nrows
        for r in range(1, rows, 1):
            fieldtype = sheet.cell_value(r, 0)
            tuple = (fieldtype)
            list.append(tuple)
        return list

    @pytest.mark.parametrize("text", Sheet())
    def test_LE046_CreateNewCustomField(self, test_setup, text):
        self.driver = test_setup
        self.logger.info("********** login into letter Hub website started*********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.lgn =login(self.driver)
        self.lgn.SetUserName(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** User Succesfully login into letter Hub website *********")
        self.custom = CreateCustomFields(self.driver)
        self.custom.ClickonCustomfield()
        time.sleep(3)
        self.custom.ClickonCreateNewField()
        time.sleep(3)
        self.custom.ClickonDropDown()
        time.sleep(3)
        self.custom.selectFromDropDown(text)
        time.sleep(3)
        self.custom.EntFieldNam()
        time.sleep(3)
        self.custom.ClickonSaveButton()
        time.sleep(5)
        self.msg = self.driver.find_element(By.TAG_NAME, "Body").text
        try:
            if "Custom Fields" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="new custom field has been added Succesfully",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("*******User new custom field has been added Succesfully*******")
                self.logger.info("Test_TC046_CustomFields_Create_New_CustomField is Passed")
                time.sleep(2)
                self.custom.ClickUserAccount()
                time.sleep(5)
                self.custom.ClickonLogOutButtton()
                time.sleep(2)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="User Failed to Add new custom field",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("User Failed to new custom field has been added")
                self.logger.info("Test_TC046_CustomFields_Create_New_CustomField is Failed")
                time.sleep(2)
                assert False
        except Exception as A:
            print(A)
        finally:
            self.driver.quit()

