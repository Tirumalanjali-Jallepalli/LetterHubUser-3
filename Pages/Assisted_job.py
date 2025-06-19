import time
from selenium.webdriver.common.by import By
from Locators.LOC_AssistedJob import Loc_AssistedJob
from selenium.webdriver.support.select import Select
import autoit


class AssistedJob:
    def __init__(self, driver):
        self.driver = driver

    def clkonJobsBtn(self):
        self.driver.find_element(By.XPATH, Loc_AssistedJob.clkonJobsBtn_xpath).click()

    def clkonAutoInvoiceScannerBtn(self):
        self.driver.find_element(By.LINK_TEXT, Loc_AssistedJob.clkonAutoInvoiceScanner_text).click()

    def selMainPdf(self, mainPDF):
        self.driver.find_element(By.XPATH, Loc_AssistedJob.MainPdfBrowse_xpath).click()
        time.sleep(3)
        autoit.win_wait_active("Open")
        autoit.control_set_text("Open", "Edit1", mainPDF)
        time.sleep(2)
        autoit.send("{ENTER}")
        time.sleep(2)
        self.driver.find_element(By.XPATH, Loc_AssistedJob.checkSaveContact_xpath).click()

    def selBackPdf(self, backPDF):
        self.driver.find_element(By.XPATH, Loc_AssistedJob.BackPdfBrowse_xpath).click()
        time.sleep(3)
        autoit.win_wait_active("Open")
        autoit.control_set_text("Open", "Edit1", backPDF)
        time.sleep(2)
        autoit.send("{ENTER}")
        time.sleep(3)

    def clkonNextBtn(self):
        self.driver.find_element(By.XPATH, Loc_AssistedJob.clkonNextBtn_xpath).click()

    def clkonOkBtn(self):
        self.driver.find_element(By.CLASS_NAME, Loc_AssistedJob.clkonOk_class).click()

    def EntJobName(self, JobName):
        self.driver.find_element(By.ID, Loc_AssistedJob.entJobName_id).send_keys(JobName)

    def entInstuctions(self, instructions):
        self.driver.find_element(By.ID, Loc_AssistedJob.entInstuctions_id).send_keys(instructions)

    def entEmailPhone(self, EmailPhone):
        self.driver.find_element(By.ID, Loc_AssistedJob.entEmailPhone_id).send_keys(EmailPhone)

    def UncheckToAddress(self, ToAddress):
        self.driver.find_element(By.XPATH, Loc_AssistedJob.checkToAddress_xpath).click()
        self.driver.find_element(By.ID, Loc_AssistedJob.entToAddress_id).send_keys(ToAddress)

    def CheckFromAddress(self):
        self.driver.find_element(By.XPATH, Loc_AssistedJob.checkFromAdress_xpath).click()

    def ClkOnAddNewFromAddress(self):
        self.driver.find_element(By.LINK_TEXT, Loc_AssistedJob.ClkOnAddNewFromAddress_text).click()

    def SelAddressType(self, AddType):
        # allTypes = self.driver.find_elements(By.XPATH, Loc_AssistedJob.SelAddressType)
        # for a in allTypes:
        #     if a.text == AddType:
        #         a.click()
        if AddType == 'Text Only':
            self.driver.find_element(By.XPATH, Loc_AssistedJob.ClkOnTextOnly_xpath).click()
        elif AddType == 'Image & Text':
            self.driver.find_element(By.XPATH, Loc_AssistedJob.ClkOnImageText_xpath).click()
        else:
            self.driver.find_element(By.XPATH, Loc_AssistedJob.ClkOnImageOnly_xpath).click()

    def BrowseTheImage(self, ImagePath):
        self.driver.find_element(By.XPATH, Loc_AssistedJob.ClkOnBrowseBtn_xpath).click()
        time.sleep(3)
        autoit.win_wait_active("Open")
        autoit.control_set_text("Open", "Edit1", ImagePath)
        time.sleep(2)
        autoit.send("{ENTER}")
        time.sleep(3)

    def AddNewAddress(self, Name, CompanyName, AddLine1, AddLine2, City, State, Zip):
        self.driver.find_element(By.ID, Loc_AssistedJob.EntName_id).send_keys(Name)
        self.driver.find_element(By.ID, Loc_AssistedJob.EntCompany_id).send_keys(CompanyName)
        self.driver.find_element(By.ID, Loc_AssistedJob.EntAddLine1_id).send_keys(AddLine1)
        self.driver.find_element(By.ID, Loc_AssistedJob.EntAddLine2_id).send_keys(AddLine2)
        self.driver.find_element(By.ID, Loc_AssistedJob.EntCity_id).send_keys(City)
        self.driver.find_element(By.ID, Loc_AssistedJob.EntState_id).send_keys(State)
        self.driver.find_element(By.ID, Loc_AssistedJob.EntZip_id).send_keys(Zip)
        time.sleep(5)
        self.driver.find_element(By.XPATH, Loc_AssistedJob.clkonAdd_xpath).click()

    def TextUnderWideImage(self, AddLine1, City, State, Zip):
        self.driver.find_element(By.ID, Loc_AssistedJob.EntAddLine1_id).send_keys(AddLine1)
        self.driver.find_element(By.ID, Loc_AssistedJob.EntCity_id).send_keys(City)
        self.driver.find_element(By.ID, Loc_AssistedJob.EntState_id).send_keys(State)
        self.driver.find_element(By.ID, Loc_AssistedJob.EntZip_id).send_keys(Zip)
        time.sleep(3)
        # select = Select(self.driver.find_element(By.ID, Loc_AssistedJob.SelFontSize_id))
        # select.select_by_visible_text(FontSize)
        self.driver.find_element(By.XPATH, Loc_AssistedJob.clkonAdd_xpath).click()

    def SelFromAddressBook(self, ContactName):
        self.driver.find_element(By.LINK_TEXT, Loc_AssistedJob.SelFromAddressBook_text).click()
        time.sleep(5)
        self.driver.find_element(By.ID, Loc_AssistedJob.SearchContactName_id).send_keys(ContactName)
        self.driver.find_element(By.XPATH, Loc_AssistedJob.CheckAddress_xpath).click()
        self.driver.find_element(By.XPATH, Loc_AssistedJob.ClkOnAddBtn_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Loc_AssistedJob.clkonAdd_xpath).click()

    def ClkOnUseDefaultFromAddress(self):
        self.driver.find_element(By.LINK_TEXT, Loc_AssistedJob.UseDefaultFromAddress_text).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Loc_AssistedJob.clkonAdd_xpath).click()

    def CheckReturnAddress(self):
        self.driver.find_element(By.XPATH, Loc_AssistedJob.CheckReturnAddress_xpath).click()

    def ClkOnAddNewReturnAddress(self):
        self.driver.find_element(By.LINK_TEXT, Loc_AssistedJob.ClkOnAddNewReturnAddress_text).click()

    def SelCarrier(self, Carrier):
        allCarriers = self.driver.find_elements(By.XPATH, Loc_AssistedJob.AllCarriers_xpath)
        for c in allCarriers:
            if c.text == Carrier:
                c.click()

    def ClkOnRequiredCheckBox(self, CheckBox):
        allCheckBoxes = self.driver.find_elements(By.XPATH, Loc_AssistedJob.AllCheckBoxs_xpath)
        for c in allCheckBoxes:
            if c.text == CheckBox:
                c.click()

    def SelPageSize(self, PageSize):
        allSizes = self.driver.find_elements(By.XPATH, Loc_AssistedJob.AllPageSizes_xpath)
        for p in allSizes:
            if p.text == PageSize:
                p.click()

    def SelReturnEnvelope(self, Envelope):
        allEnvelopes = self.driver.find_elements(By.XPATH, Loc_AssistedJob.AllReturnEnvelope_xpath)
        for p in allEnvelopes:
            if p.text == Envelope:
                p.click()

    def SelPrintOptions(self, PrintOption):
        allOptions = self.driver.find_elements(By.XPATH, Loc_AssistedJob.AllPrintOptions_xpath)
        for p in allOptions:
            if p.text == PrintOption:
                p.click()

    def SelChangeOfAddressRadioBtns(self, ForwardEmail, UpdateAddress):
        allOptions = self.driver.find_elements(By.XPATH, Loc_AssistedJob.AllChangeOfAddressRadioBtns_xpath)
        for p in allOptions:
            if p.text == ForwardEmail:
                p.click()
            time.sleep(5)
            if p.text == UpdateAddress:
                p.click()
        self.driver.find_element(By.XPATH, Loc_AssistedJob.CheckUpdatedAddress_xpath).click()

    def SelPaymentOption(self, PayOption):
        allPayOptions = self.driver.find_elements(By.XPATH, Loc_AssistedJob.AllPaymentOptions_xpath)
        for p in allPayOptions:
            if p.text == PayOption:
                p.click()

    def SelChargeMyCreditCard(self, CardName):
        self.driver.find_element(By.XPATH, Loc_AssistedJob.ChargeMyCreditCard_xpath).click()
        select = Select(self.driver.find_element(By.ID, Loc_AssistedJob.SelCreditCard_id))
        select.select_by_visible_text(CardName)

    def ClkOnSubmitTheJob(self):
        self.driver.find_element(By.XPATH, Loc_AssistedJob.ClkOnSubmitTheJob_xpath).click()

    def ClkOnOkBtn(self):
        self.driver.find_element(By.XPATH, Loc_AssistedJob.ClkOnOkBtn_xpath).click()

    def ExistingAdress(self):
        self.driver.find_element(By.XPATH, Loc_AssistedJob.ClkonExitAdd_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Loc_AssistedJob.ClkonratiBtn_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Loc_AssistedJob.ClkonCloseBtn_xpath).click()
        time.sleep(5)





