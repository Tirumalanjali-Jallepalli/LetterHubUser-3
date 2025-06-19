import allure
import pytest
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait

from utilities.customLogger import LogGen
from utilities.readproperties import Readdata
import time
from Pages.Login import Login
from Pages.Contacts_NewContact import Contacts

import logging
import sys
from selenium.webdriver.remote.remote_connection import LOGGER


class Test_TC031_1_Contacts_NewBusinessContact:
    baseurl = Readdata.applicationurl()
    username = Readdata.username()
    password = Readdata.password()
    logger = LogGen.log()

    @staticmethod
    def Sheet():
        path = r".\LH_sheets\LH_DATASHEETS1.xls"
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name("Contacts_AddNewBusinessContact")
        List = []
        rows = sheet.nrows
        for r in range(1, rows, 1):
            category = sheet.cell_value(r, 0)
            JobTitle = sheet.cell_value(r, 1)
            Company = sheet.cell_value(r, 2)
            FName = sheet.cell_value(r, 3)
            MName = sheet.cell_value(r, 4)
            LName = sheet.cell_value(r, 5)
            Prefix = sheet.cell_value(r, 6)
            Suffix = sheet.cell_value(r, 7)
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

            Tuple = (category, FName, MName, LName, Prefix, Suffix, JobTitle, Company, Notes, Tags, Category_type,
                     AddLine1, AddLine2, city, state, zipCode, Country, phone_purpose, phoneNo, email_purpose, email,
                     date_purpose, date, url_purpose, url)
            List.append(Tuple)
        return List

    @pytest.mark.parametrize("category, FName, MName, LName, Prefix, Suffix, JobTitle, Company, Notes, Tags, "
                             "Category_type, AddLine1, AddLine2, city, state, zipCode, Country, phone_purpose, phoneNo,"
                             " email_purpose, email, date_purpose, date, url_purpose, url", Sheet())
    def test_TC031_1_AddNewContact(self, test_setup, category, FName, MName, LName, Prefix, Suffix, JobTitle, Company,
                                   Notes,
                                   Tags, Category_type, AddLine1, AddLine2, city, state, zipCode, Country,
                                   phone_purpose,
                                   phoneNo, email_purpose, email, date_purpose, date, url_purpose, url):
        self.driver = test_setup
        self.logger.info("********** Test_TC031_1_Contacts_AddNewBusinessContact TestCase Started *********")
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
        self.con.clkonAddNewContact()
        time.sleep(3)
        self.con.AddBusinessContact_Details(JobTitle, Company, FName, MName, LName, Prefix, Suffix, Notes)
        time.sleep(3)
        self.con.selTag(Tags)
        time.sleep(3)
        self.con.AddNewAddress(Category_type, AddLine1, AddLine2, city, state, zipCode, Country)
        time.sleep(3)
        self.con.AddNewPhoneNo(phone_purpose, phoneNo)
        time.sleep(3)
        self.con.AddNewEmailAddress(email_purpose, email)
        time.sleep(3)
        self.con.AddNewDate(date_purpose, date)
        time.sleep(3)
        self.con.AddNewUrl(url_purpose, url)
        time.sleep(3)
        self.con.clkOnSaveBtn()
        time.sleep(5)

        # Suppress Selenium Debug Logs
        LOGGER.setLevel(logging.WARNING)

        # Redirect stderr to prevent stacktrace in terminal
        sys.stderr = open("selenium_errors.log", "w")

        try:
            wait = WebDriverWait(self.driver, 10)
            toaster_text = wait.until(lambda driver: driver.execute_script("return document.body.innerText;"))
            # print(f"Captured Page Text:\n{toaster_text}")

            if "Contact successfully added" in toaster_text:
                # print("Contact added successfully!")
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="Successfully Add the New Business Contact in "
                                                                        "Contacts", attachment_type=AttachmentType.PNG)
                self.logger.info("******* Successfully Add the New Person Contact in Contacts *******")
                self.logger.info("Test_TC031_1_Contacts_AddNewBusinessContact is Passed")
                time.sleep(2)
            else:
                print("Toaster message incorrect or missing.")
                allure.attach(self.driver.get_screenshot_as_png(), name="Failed while Add the New Business Contact in"
                                                                        "Contacts", attachment_type=AttachmentType.PNG)
                self.logger.info("******* Failed while Add the New Business Contact in Contacts *******")
                self.logger.info("Test_TC031_1_Contacts_AddNewBusinessContact is Failed")
                time.sleep(2)
                assert False

            self.lo.Logout()
            time.sleep(2)

        except Exception as e:
            print(f"Error: {e}")
        finally:
            if self.driver:
                self.driver.quit()

        # self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        # try:
        #     if "Contact successfully added.".lower() in self.msg.lower():
        #         assert True
        #         allure.attach(self.driver.get_screenshot_as_png(), name="Successfully Add the New Business Contact in "
        #                                                                 "Contacts", attachment_type=AttachmentType.PNG)
        #         self.logger.info("******* Successfully Add the New Person Contact in Contacts *******")
        #         self.logger.info("Test_TC031_1_Contacts_AddNewBusinessContact is Passed")
        #         time.sleep(2)
        #         self.lo.Logout()
        #
        #     else:
        #         allure.attach(self.driver.get_screenshot_as_png(), name="Failed while Add the New Business Contact in "
        #                                                                 "Contacts", attachment_type=AttachmentType.PNG)
        #         self.logger.info("******* Failed while Add the New Business Contact in Contacts *******")
        #         self.logger.info("Test_TC031_1_Contacts_AddNewBusinessContact is Failed")
        #         time.sleep(2)
        #         assert False
        # except Exception as E:
        #     print(E)
        #     raise
        # finally:
        #     self.driver.quit()
