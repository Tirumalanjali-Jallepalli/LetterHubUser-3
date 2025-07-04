import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from utilities.readproperties import Readdata
import time
from Pages.Login import Login
from Pages.Contacts_Tags import Contacts_tags


class Test_TC037_Contacts_CreateNewTag:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_sheets\LH_DATASHEETS1.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name("Contacts_manageTags")
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            TagName = sheet.cell_value(r, 0)

            Tuple = TagName
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("TagName", Sheet())
    def test_TC037_CreateNewTag(self, test_setup, TagName):
        self.driver = test_setup
        self.logger.info("********** Test_TC037_Contacts_CreateNewTag TestCase Started *********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.driver.implicitly_wait(20)
        self.lo = Login(self.driver)
        self.lo.LoginCredentials(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** Successfully Login Into LetterHUB Web-portal *********")
        self.con = Contacts_tags(self.driver)
        self.con.clkonContactsModule()
        time.sleep(3)
        self.con.clkonManageTags()
        time.sleep(3)
        self.con.clkonCreateNewTagBtn(TagName)
        time.sleep(5)
        self.con.DelTagName()
        time.sleep(3)
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        try:
            if "Create New Tag" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully Create New tag in Contacts",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully Create New tag in Contacts *******")
                self.logger.info("Test_TC037_Contacts_CreateNewTag is Passed")
                time.sleep(5)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed while creating new tag in Contacts",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while creating new tag in Contacts *******")
                self.logger.info("Test_TC037_Contacts_CreateNewTag is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()

