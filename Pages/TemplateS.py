import random
import string
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from Locators.LOC_Templates import template
import autoit
import time


class Createtemplate:

    def __init__(self, driver):
        self.driver = driver

    def ClickonTemplateButton(self):
        self.driver.find_element(By.XPATH, template.Clkontemplate_xpath).click()

    def ClickonEditor(self):
        self.driver.find_element(By.XPATH, template.Clkoncreateonlineeditor_xpath).click()

    def ClickonSaveEditor(self):
        self.driver.find_element(By.XPATH, template.Clkonsavebtn_editor_xpath).click()

    def ClickonEyeView(self):
        self.driver.find_element(By.XPATH, template.Clkoneyeicon_xpath).click()

    def Clickon_X_Button_Eye(self):
        self.driver.find_element(By.XPATH, template.Clkonxbutton_eye_xpath).click()

    def ClickonEditIcon(self):
        self.driver.find_element(By.XPATH, template.CLkonediticon_xpath).click()

    def ClickonClone(self):
        self.driver.find_element(By.XPATH, template.Clkoncloneicon_xpath).click()

    def ClickonDownloadIcon(self):
        self.driver.find_element(By.XPATH, template.Clkondownloadicon_xpath).click()

    def ClickonDeleteIcon(self):
        self.driver.find_element(By.XPATH, template.Clkondeleteicon_xpath).click()

    def ClickonRenameButton(self):
        self.driver.find_element(By.XPATH, template.Clkonrename_xpath).click()

    def ClickonWhat_Template_Button(self):
        self.driver.find_element(By.XPATH, template.Clkonwhatistemp_xpath).click()

    def ClickonEditButton_Temp(self):
        self.driver.find_element(By.XPATH, template.CLkonediticon_xpath).click()

    def ClickonYesButton_Delete(self):
        self.driver.find_element(By.XPATH, template.Clkonyesbtn_delete_xpath).click()

    def ClickonNoButton_Delete(self):
        self.driver.find_element(By.XPATH, template.ClkonNobtn_delete_xpath).click()

    def EnterNameinRename(self):
        self.driver.find_element(By.ID, template.Entertherename_id).clear()
        self.name = ''.join(random.choice(string.ascii_lowercase) for x in range(4))
        self.driver.find_element(By.ID, template.Entertherename_id).send_keys(self.name)

    def ClickonSave_Rename(self):
        self.driver.find_element(By.XPATH, template.Clkonsave_rename_xpath).click()

    def ClickonOnlineEditor(self):
        self.driver.find_element(By.XPATH, template.Clkononlineeditor_xpath).click()

    def EnterOnlineEditor(self, text):
        action = ActionChains(self.driver)
        action.send_keys(Keys.CONTROL).send_keys(text).perform()

    def ClickonCLoseButton_SaveTemplate(self):
        self.driver.find_element(By.XPATH, template.Clkonsavetemp_xpath).click()

    def EnterTemplateName(self):
        self.driver.find_element(By.ID, template.Entertherename_id).clear()
        self.name = ''.join(random.choice(string.ascii_lowercase) for x in range(4))
        self.driver.find_element(By.ID, template.Entertherename_id).send_keys(self.name)

    def ClickonSavetheTemplate(self):
        self.driver.find_element(By.XPATH, template.Clkonsavethetemplate_xpath).click()

    def CLickonEditSaveButton(self):
        self.driver.find_element(By.XPATH, template.Clkoneditsavebutn_xpath).click()

    def Clickon_X_Button_Whatis_Template(self):
        self.driver.find_element(By.XPATH, template.Clkonxbutton_eye_xpath).click()

    def ClkonBrowseBtn(self, Upload):
        self.driver.find_element(By.XPATH, template.Clkonbrowse_xpath).click()
        autoit.win_wait_active("Open")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", Upload)
        time.sleep(2)
        autoit.send("{ENTER}")
        time.sleep(3)
