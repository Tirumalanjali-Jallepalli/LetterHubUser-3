import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Locators.LOC_Connections import Loc_Connections
from Locators.LOC_Contacts import Contact_Locators
from selenium.common.exceptions import NoSuchElementException
import autoit


class Connections:

    def __init__(self, driver):
        self.driver = driver

    def ClkOnConnectionsModule(self):
        self.driver.find_element(By.LINK_TEXT, Loc_Connections.ClkOnConnectionsModule_text).click()

    def ClkOnImportVCFBtn(self):
        self.driver.find_element(By.LINK_TEXT, Loc_Connections.ClkOnImportVCF_text).click()

    def ClkOnImportCSVBtn(self):
        self.driver.find_element(By.LINK_TEXT, Loc_Connections.ClkOnImportCSV_text).click()

    def ClkOnImportExcelBtn(self):
        self.driver.find_element(By.LINK_TEXT, Loc_Connections.ClkOnImportExcel_text).click()

    def Import_File(self, VCFPath):
        self.driver.find_element(By.XPATH, Loc_Connections.ClkOnBrowseBtn_xpath).click()
        time.sleep(3)
        autoit.win_wait_active("Open")
        autoit.control_set_text("Open", "Edit1", VCFPath)
        time.sleep(2)
        autoit.send("{ENTER}")

    def ClkOnImportCSVExcel_Save(self, AllUSActionBtn):
        if AllUSActionBtn == "Yes":
            self.driver.find_element(By.ID, Loc_Connections.ClkOnAllUSYesBtn_id).click()
            time.sleep(4)
        else:
            self.driver.find_element(By.ID, Loc_Connections.ClkOnAllUSNoBtn_id).click()
            time.sleep(4)
        msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(msg)

        if "Map atleast one column to continue." not in msg:
            self.driver.find_element(By.XPATH, Loc_Connections.ClkOnImportCSV_Save_xpath).click()
            time.sleep(2)

            if "Map atleast one column to continue." in msg:
                self.driver.find_element(By.XPATH, Loc_Connections.ClkOnFirstColNamesCheckBox_xpath).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, Loc_Connections.ClkOnMapCol_cls).click()
                time.sleep(1)
                a = self.driver.find_element(By.CLASS_NAME, Loc_Connections.MapColTextBox_cls)
                a.send_keys('First Name')
                time.sleep(1)
                a.send_keys(Keys.ENTER)
                time.sleep(2)
                self.driver.find_element(By.XPATH, Loc_Connections.ClkOnImportCSV_Save_xpath).click()
            else:
                pass





    def ClkOnImportCSVExcel_Cancel(self):
        self.driver.find_element(By.XPATH, Loc_Connections.ClkOnImportCSV_Cancel_xpath).click()

    def SelTag(self, ExistingTag):
        # # self.driver.find_element(By.XPATH, Loc_Connections.ClkOnSelTags_xpath).send_keys(ExistingTag)
        # action = ActionChains(self.driver)
        # action.send_keys(3 * Keys.TAB).send_keys(ExistingTag).perform()
        # time.sleep(3)
        # action.send_keys(Keys.ENTER)

        self.driver.find_element(By.XPATH, Loc_Connections.ClkOnSelTags_xpath).click()
        allTags = self.driver.find_elements(By.XPATH, Loc_Connections.AllExistingTags_xpath)
        for t in allTags:
            # print(t.text)
            # print(len(allTags))
            if t.text == ExistingTag:
                t.click()

    def ClkOnAddNewTag(self, NewTag):
        self.driver.find_element(By.LINK_TEXT, Loc_Connections.ClkOnAddNewTag_text).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Contact_Locators.entTag_xpath)
        action = ActionChains(self.driver)
        action.send_keys(3 * Keys.TAB).send_keys(NewTag).perform()
        time.sleep(4)
        self.driver.find_element(By.XPATH, Contact_Locators.clkonTagSavebtn_xpath).click()

    def ClkOnSaveTagBtn(self):
        self.driver.find_element(By.XPATH, Loc_Connections.ClkOnSaveTagBtn_xpath).click()

    def ClkOnSkipTagBtn(self):
        self.driver.find_element(By.XPATH, Loc_Connections.ClkOnSkipTagBtn_xpath).click()







