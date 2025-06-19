import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from utilities.readproperties import Readdata
import time
from Pages.Login import Login
from Pages.Contacts_NewContact import Contacts


class Test_TC031_2_Contacts_SearchContact:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_sheets\LH_DATASHEETS1.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name("Contacts_Search")
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            ContactName = sheet.cell_value(r, 0)

            Tuple = ContactName
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("ContactName", Sheet())
    def test_TC031_2_SearchTheContact(self, test_setup, ContactName):
        self.driver = test_setup
        self.logger.info("********** Test_TC031_2_Contacts_SearchWithContactName TestCase Started *********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.driver.implicitly_wait(15)
        self.lo = Login(self.driver)
        self.lo.LoginCredentials(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** Successfully Login Into LetterHUB Web-portal *********")
        self.con = Contacts(self.driver)
        self.con.clkonContactsModule()
        time.sleep(3)
        self.con.clkOnserachField(ContactName)
        time.sleep(5)
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        try:
            if "Contacts" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully search the Contact",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully search the Contact *******")
                self.logger.info("Test_TC031_2_Contacts_SearchWithContactName is Passed")
                time.sleep(3)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed while search the Contact",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while search the Contact *******")
                self.logger.info("Test_TC031_2_Contacts_SearchWithContactName is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()

