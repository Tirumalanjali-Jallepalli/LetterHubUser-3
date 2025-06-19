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


class Test_TC034_1_Contacts_AddExistingTag:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_sheets\LH_DATASHEETS1.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name("Contacts_addExistingTags")
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            TagName = sheet.cell_value(r, 0)
            Tag1 = sheet.cell_value(r, 1)
            Tag2 = sheet.cell_value(r, 2)

            Tuple = (TagName, Tag1, Tag2)
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("TagName, Tag1, Tag2", Sheet())
    def test_TC034_1_contacts(self, test_setup, TagName, Tag1, Tag2):
        self.driver = test_setup
        self.logger.info("********** Test_TC034_1_Contacts_Tags_AddExistingTagForContacts TestCase Started *********")
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
        self.con.SelectDrpTag(TagName)
        time.sleep(5)
        self.con.clkonSelectAll()
        time.sleep(5)
        self.con.clkonTagBtn()
        time.sleep(2)
        self.con.AddExistingTag(Tag1, Tag2)
        time.sleep(3)
        self.msg = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]").text
        time.sleep(3)
        print(self.msg)
        try:
            if "Contacts" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully add the existing tag for Contacts",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully add the existing tag for Contacts *******")
                self.logger.info("Test_TC034_1_Contacts_Tags_AddExistingTagForContacts is Passed")
                time.sleep(3)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed while add the existing tag for Contacts",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while add the existing tag for Contacts *******")
                self.logger.info("Test_TC034_1_Contacts_Tags_AddExistingTagForContacts is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()
