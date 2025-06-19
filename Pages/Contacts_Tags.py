import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Locators.LOC_Contacts import Contact_Locators
from selenium.webdriver.common.action_chains import ActionChains


class Contacts_tags:

    def __init__(self, driver):
        self.driver = driver

    def clkonContactsModule(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonContacts_xpath).click()

    def clkonManageTags(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonManageTags_xpath).click()

    def clkonCreateNewTagBtn(self, TagName):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonCreateNewTag_x).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, Contact_Locators.entTag_xpath)
        action = ActionChains(self.driver)
        action.send_keys(3*Keys.TAB).send_keys(TagName).perform()
        self.driver.find_element(By.XPATH, Contact_Locators.clkonTagSavebtn_xpath).click()

    def ClkOnCreateNewTagClose(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonTagClosebtn_xpath).click()

    def DelTagName(self):
        self.driver.find_element(By.XPATH, "//td[contains(text(), 'Test20')]//following::td//button[@class='btn btn-danger btn-xs']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Contact_Locators.clkonDelTagYes_xpath).click()
        time.sleep(4)

    ######## Contacts_Select drp tags #######
    def SelectDrpTag(self, drpTag):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonTagsdrp_xpath).click()
        time.sleep(3)
        all_tags = self.driver.find_elements(By.XPATH, Contact_Locators.alldrptags_xpath)
        for t in all_tags:
            # print(t.text)
            if t.text == drpTag:
                t.click()
                time.sleep(2)
                break

    def clkonSelectAll(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonSelectAllBtn_xpath).click()
        time.sleep(5)

    def clkonDeselectAll(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonDeselectAllBtn_xpath).click()
        time.sleep(3)

    def SelectContacts(self):
        self.driver.find_element(By.XPATH, '//*[@id="scrollTable"]/tbody[2]/tr[1]/td[1]/label/span/i').click()
        time.sleep(3)

    def clkonDeleteSendVCFBtn(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonContacts_DeleteBtn_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.clkonDeleteSendVCF_xpath).click()
        time.sleep(3)

    def clkonDeleteOkBtn(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonContacts_DeleteBtn_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.clkonDeleteOk_xpath).click()
        time.sleep(3)

    ######Add New tag for contacts #####

    def clkonTagBtn(self):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonTagBtn_xpath).click()
        time.sleep(2)

    def ClkOnAddNewTag(self, NewTag):
        self.driver.find_element(By.XPATH, Contact_Locators.clkonAddNewTagBtn_xpath).click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, Contact_Locators.ent_tagName_xpath)
        action = ActionChains(self.driver)
        action.send_keys(2 * Keys.TAB).send_keys(NewTag).perform()
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()
        time.sleep(5)
        # self.driver.find_element(By.XPATH, Contact_Locators.clkonSaveTagBtn_xpath).click()
        # time.sleep(5)
    ######## Add the existing tag for contacts ############

    def AddExistingTag(self, tag1, tag2):
        all_tags = self.driver.find_elements(By.XPATH, Contact_Locators.selExistingTag_xpath)

        for t in all_tags:
            if t.text.strip() == tag1:
                t.click()
                time.sleep(2)
                break

        all_tags1 = self.driver.find_elements(By.XPATH, Contact_Locators.selExistingTag_xpath)

        for t1 in all_tags1:
            if t1.text.strip() == tag2:
                t1.click()
                time.sleep(2)
                break
        self.driver.find_element(By.XPATH, Contact_Locators.Uncheck_Keeptags).click()  ######UncheckKeepExistingTag
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.selTagSavebtn_xpath).click()
        time.sleep(2)






