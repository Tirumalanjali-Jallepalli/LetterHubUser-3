import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from utilities.readproperties import Readdata
import time
from Pages.Login import Login
from Pages.Contacts_EditContact import Edit_Contacts


class Test_TC032_Contacts_EditContact:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_sheets\LH_DATASHEETS1.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name("Contacts_EditContact")
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            conName = sheet.cell_value(r, 0)
            FName = sheet.cell_value(r, 1)
            MName = sheet.cell_value(r, 2)
            LName = sheet.cell_value(r, 3)
            Prefix = sheet.cell_value(r, 4)
            Suffix = sheet.cell_value(r, 5)
            JobTitle = sheet.cell_value(r, 6)
            Company = sheet.cell_value(r, 7)
            Notes = sheet.cell_value(r, 8)
            Tags = sheet.cell_value(r, 9)
            Category_type = sheet.cell_value(r, 10)
            AddLine1 = sheet.cell_value(r, 11)
            AddLine2 = sheet.cell_value(r, 12)
            city = sheet.cell_value(r, 13)
            state = sheet.cell_value(r, 14)
            zipCode = int(sheet.cell_value(r, 15))
            Country = sheet.cell_value(r, 16)
            phone_purpose = sheet.cell_value(r, 17)
            phoneNo = int(sheet.cell_value(r, 18))
            email_purpose = sheet.cell_value(r, 19)
            email = sheet.cell_value(r, 20)
            date_purpose = sheet.cell_value(r, 21)
            date = int(sheet.cell_value(r, 22))
            url_purpose = sheet.cell_value(r, 23)
            url = sheet.cell_value(r, 24)

            Tuple = (conName, FName, MName, LName, Prefix, Suffix, JobTitle, Company, Notes, Tags, Category_type,
                     AddLine1, AddLine2, city, state, zipCode, Country, phone_purpose, phoneNo, email_purpose, email,
                     date_purpose, date, url_purpose, url)
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("conName, FName, MName, LName, Prefix, Suffix, JobTitle, Company, Notes, Tags, "
                             "Category_type, AddLine1, AddLine2, city, state, zipCode, Country, phone_purpose, phoneNo,"
                             " email_purpose, email, date_purpose, date, url_purpose, url", Sheet())
    def test_TC032_EditContact(self, test_setup, conName, FName, MName, LName, Prefix, Suffix, JobTitle, Company, Notes,
                           Tags, Category_type, AddLine1, AddLine2, city, state, zipCode, Country, phone_purpose,
                           phoneNo, email_purpose, email, date_purpose, date, url_purpose, url):
        self.driver = test_setup
        self.logger.info("********** Test_TC032_Contacts_EditContact TestCase Started *********")
        time.sleep(3)
        self.driver.get(self.baseurl)
        time.sleep(3)
        self.driver.implicitly_wait(15)
        self.lo = Login(self.driver)
        self.lo.LoginCredentials(self.username, self.password)
        time.sleep(3)
        self.logger.info("********** Successfully Login Into LetterHUB Web-portal *********")
        self.con = Edit_Contacts(self.driver)
        self.con.clkonContactsModule()
        time.sleep(3)
        self.con.clkOnserachField(conName)
        time.sleep(3)
        self.con.clkonEditBtn()
        time.sleep(3)
        self.con.EditAddress(Category_type, AddLine1, AddLine2, city, state, zipCode, Country)
        time.sleep(3)
        self.con.EditPhoneNo(phone_purpose, phoneNo)
        time.sleep(3)
        self.con.EditEmailAddress(email_purpose, email)
        time.sleep(3)
        self.con.EditDate(date_purpose, date)
        time.sleep(3)
        # self.con.EditUrl(url_purpose, url)
        # time.sleep(3)
        self.con.clkOnSaveChangesBtn()
        time.sleep(12)
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        try:
            if "Contacts" in self.msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully edited the Contact in Contacts",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully edited the Contact in Contacts *******")
                self.logger.info("Test_TC032_Contacts_EditContact is Passed")
                time.sleep(2)
                self.lo.Logout()
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed while edit the Contact in Contacts",
                              attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while edit the Contact in Contacts *******")
                self.logger.info("Test_TC032_Contacts_EditContact is Failed")
                time.sleep(2)
                assert False
        except Exception as E:
            print(E)
        finally:
            self.driver.quit()

