import time
from selenium.webdriver.common.by import By
from Locators.LOC_Contacts import Contact_Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Edit_Contacts:

    def __init__(self, driver):
        self.driver = driver

    def clkonContactsModule(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonContacts_xpath).click()

    def clkOnserachField(self, conName):
        self.driver.find_element(By.ID, Contact_Locators.clkonSearchField_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.clkonSearchField_id).send_keys(conName)
        time.sleep(2)
        all_contacts = self.driver.find_elements(By.XPATH, Contact_Locators.all_ContactNames_xpath)

        for con in all_contacts:
            if con.text == conName:
                con.click()
                time.sleep(3)

    def clkonCloseBtn(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonContactClosebtn_xpath).click()
        time.sleep(2)

    def clkonEditBtn(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonEditBtn_xpath).click()

    def EditPersonContact_Details(self, FName, MName, LName, Prefix, Suffix, JobTitle, Company, Notes):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonPersonRadiobtn_xpath).click()

        self.driver.find_element(By.ID, Contact_Locators.entFirstName_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entFirstName_id).send_keys(FName)

        self.driver.find_element(By.ID, Contact_Locators.entMiddleName_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entMiddleName_id).send_keys(MName)

        self.driver.find_element(By.ID, Contact_Locators.entLastName_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entLastName_id).send_keys(LName)

        self.driver.find_element(By.ID, Contact_Locators.entPrefix_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entPrefix_id).send_keys(Prefix)

        self.driver.find_element(By.ID, Contact_Locators.entSuffix_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entSuffix_id).send_keys(Suffix)

        self.driver.find_element(By.ID, Contact_Locators.entJobTitle_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entJobTitle_id).send_keys(JobTitle)

        self.driver.find_element(By.ID, Contact_Locators.entCompany_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entCompany_id).send_keys(Company)

        self.driver.find_element(By.ID, Contact_Locators.ent_Notes_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.ent_Notes_id).send_keys(Notes)

    def EditBusinessContact_Details(self, JobTitle, Company, FName, MName, LName, Prefix, Suffix, Notes):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonBusinessRadiobtn_xpath).click()

        self.driver.find_element(By.ID, Contact_Locators.entJobTitle_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entJobTitle_id).send_keys(JobTitle)

        self.driver.find_element(By.ID, Contact_Locators.entCompany_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entCompany_id).send_keys(Company)

        self.driver.find_element(By.ID, Contact_Locators.entFirstName_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entFirstName_id).send_keys(FName)

        self.driver.find_element(By.ID, Contact_Locators.entMiddleName_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entMiddleName_id).send_keys(MName)

        self.driver.find_element(By.ID, Contact_Locators.entLastName_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entLastName_id).send_keys(LName)

        self.driver.find_element(By.ID, Contact_Locators.entPrefix_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entPrefix_id).send_keys(Prefix)

        self.driver.find_element(By.ID, Contact_Locators.entSuffix_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entSuffix_id).send_keys(Suffix)

        self.driver.find_element(By.ID, Contact_Locators.ent_Notes_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.ent_Notes_id).send_keys(Notes)
        time.sleep(3)

    def CreateNewTag(self, Newtag):
        self.driver.find_element(By.XPATH, Contact_Locators.clk_Tags_drp_xpath).click()
        allTags = self.driver.find_elements(By.XPATH, Contact_Locators.all_tags_drp_xpath)
        for tag in allTags:
            if tag.text == 'Create New Tag':
                tag.click()
        self.driver.find_element(By.ID, Contact_Locators.entNewtagName_id).send_keys(Newtag)
        self.driver.find_element(By.XPATH, Contact_Locators.clkonOkbtn_xpath).click()

    def selTag(self, Tags):
        self.driver.find_element(By.XPATH, Contact_Locators.clk_Tags_drp_xpath).click()
        allTags = self.driver.find_elements(By.XPATH, Contact_Locators.all_tags_drp_xpath)

        for tag in allTags:
            if tag.text == Tags and tag.text != 'Create New Tag':
                time.sleep(5)
                tag.click()

        self.driver.find_element(By.XPATH, Contact_Locators.clk_Tags_drp_xpath).click()

    def EditAddress(self, Category_type, AddLine1, AddLine2, city, state, zipCode, Country):
        self.driver.find_element(By.NAME, Contact_Locators.sel_addressPurpose_name).clear()
        self.driver.find_element(By.NAME, Contact_Locators.sel_addressPurpose_name).send_keys(Category_type)
        time.sleep(2)
        self.driver.find_element(By.ID, Contact_Locators.entAddLine1_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entAddLine1_id).send_keys(AddLine1)

        self.driver.find_element(By.ID, Contact_Locators.entAddLine2_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entAddLine2_id).send_keys(AddLine2)

        self.driver.find_element(By.ID, Contact_Locators.entCity_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entCity_id).send_keys(city)

        self.driver.find_element(By.ID, Contact_Locators.entState_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entState_id).send_keys(state)

        self.driver.find_element(By.ID, Contact_Locators.entZip_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entZip_id).send_keys(zipCode)

        self.driver.find_element(By.XPATH, Contact_Locators.ClkOnCountryDropdown_xpath).click()
        all_countries = self.driver.find_elements(By.XPATH, Contact_Locators.all_Country_xpath)
        for country in all_countries:
            if country.text == Country:
                country.click()
                time.sleep(2)

    def EditPhoneNo(self, phone_purpose, phoneNo):
        self.driver.find_element(By.NAME, Contact_Locators.sel_phonePurpose_name).clear()
        self.driver.find_element(By.NAME, Contact_Locators.sel_phonePurpose_name).send_keys(phone_purpose)

        self.driver.find_element(By.ID, Contact_Locators.entPhoneNo_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entPhoneNo_id).send_keys(phoneNo)

    def EditEmailAddress(self, email_purpose, email):
        self.driver.find_element(By.NAME, Contact_Locators.sel_EmailPurpose_name).clear()
        self.driver.find_element(By.NAME, Contact_Locators.sel_EmailPurpose_name).send_keys(email_purpose)

        self.driver.find_element(By.ID, Contact_Locators.entEmail_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entEmail_id).send_keys(email)

    def EditDate(self, date_purpose, date):
        self.driver.find_element(By.NAME, Contact_Locators.sel_DatePurpose_name).clear()
        self.driver.find_element(By.NAME, Contact_Locators.sel_DatePurpose_name).send_keys(date_purpose)

        self.driver.find_element(By.ID, Contact_Locators.entDate_id).send_keys(10 * Keys.BACK_SPACE)
        edit_date = self.driver.find_element(By.ID, Contact_Locators.entDate_id)
        edit_date.send_keys(date)
        time.sleep(1)
        edit_date.send_keys(Keys.ENTER)
        time.sleep(2)

    def EditUrl(self, url_purpose, url):
        self.driver.find_element(By.NAME, Contact_Locators.sel_URLPurpose_name).clear()
        self.driver.find_element(By.NAME, Contact_Locators.sel_URLPurpose_name).send_keys(url_purpose)

        self.driver.find_element(By.ID, Contact_Locators.entURL_id).clear()
        self.driver.find_element(By.ID, Contact_Locators.entURL_id).send_keys(url)

    def clkOnSaveChangesBtn(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonsavebtn_xpath).click()
        msg1 = self.driver.find_element(By.TAG_NAME, "body").text
        print(msg1)

    def clkOnCloneSaveBtn(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonClonesaveBtn_xpath).click()

    def clkOnCloseBtn(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonClosebtn_xpath).click()

    def clkOnCloneBtn(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonCloneBtn_xpath).click()

    # ####### Delete the Contact #########
    def clkOnDeleteBtn(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonDeleteBtn_xpath).click()

    def clkOnDelYesBtn(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonDelYesBtn_xpath).click()

    def clkOnDelNoBtn(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonDelNoBtn_xpath).click()

