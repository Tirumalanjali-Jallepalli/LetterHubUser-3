import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Locators.LOC_Invoices import Loc_Invoices
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class Invoices:
    def __init__(self, driver):
        self.driver = driver

    def ClkOnInvoicesModule(self):
        self.driver.find_element(By.LINK_TEXT, Loc_Invoices.ClkOnInvoicesModule_text).click()

    def SearchInvoices(self, InvoiceName):
        self.driver.find_element(By.ID, Loc_Invoices.SearchInvoice_id).send_keys(InvoiceName)
        time.sleep(5)
        allInvoices = self.driver.find_elements(By.XPATH, Loc_Invoices.allInvoiceNames_xpath)
        for i in allInvoices:
            if i.text == InvoiceName:
                i.click()
                time.sleep(5)
                action = ActionChains(self.driver)
                action.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
                break
        # self.driver.find_element(By.XPATH, Loc_Invoices.ClkOnInvoiceDetailsCloseBtn_xpath).click()

    def SelInvoiceAccount(self, account):
        self.driver.find_element(By.XPATH, Loc_Invoices.ClkOnConnectedAccountList_xpath).click()
        items = self.driver.find_elements(By.TAG_NAME, 'li')
        for i in items:
            if i.text == account:
                i.click()

    def SelInvoiceDate(self, date):
        self.driver.find_element(By.XPATH, Loc_Invoices.ClkOnConnectedAccountsDate_xpath).click()
        items = self.driver.find_elements(By.TAG_NAME, 'li')
        for i in items:
            if i.text == date:
                i.click()

    def SelInvoiceStatus(self, status):
        self.driver.find_element(By.XPATH, Loc_Invoices.ClkOnConnectedAccountStatus_xpath).click()
        items = self.driver.find_elements(By.TAG_NAME, 'li')
        for i in items:
            if i.text == status:
                i.click()

    def MailSelectedInvoicesBtn(self, InvoiceName, action):
        invoice = self.driver.find_element(By.TAG_NAME, "body").text
        # print(invoice)
        try:
            if str(InvoiceName) in invoice:
                self.driver.find_element(By.XPATH, "//td/a[contains(text(), '" + str(InvoiceName) + "')]//preceding::td//label[@ng-click='selectInvoice(invoice)']").click()
                time.sleep(4)
                self.driver.find_element(By.XPATH, Loc_Invoices.ClkOnMailSelectedInvoices_xpath).click()
                time.sleep(5)
                if action == 'Continue':
                    self.driver.find_element(By.XPATH, Loc_Invoices.ClkOnAddressReviewContinueBtn_xpath).click()
                    time.sleep(5)
                else:
                    self.driver.find_element(By.XPATH, Loc_Invoices.ClkOnAddressReviewCloseBtn_xpath).click()
                    time.sleep(5)
        except NoSuchElementException:
            print("Doc Number is not found, No invoices to show.")







