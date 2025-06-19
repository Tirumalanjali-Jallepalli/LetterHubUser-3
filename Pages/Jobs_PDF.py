import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Locators.LOC_Jobs import jobs
import autoit


class Jobpdf:

    def __init__(self, driver):
        self.driver = driver

    def ClickonJobsButton(self, name):

        self.driver.find_element(By.XPATH, jobs.Clkonjobsbtn_Text).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, jobs.ClkonStartNewJob_Btn_Xpath).click()
        time.sleep(3)
        self.driver.find_element(By.ID, jobs.EnterContactName_ID).send_keys(name)
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, jobs.ClkonSelectall_Linktext).click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, jobs.ClkonDeselect_Linktext).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, jobs.ClkonContactCheckBox_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, jobs.ClkOnNextButtonSelectR_xpath).click()
        time.sleep(5)

    def ClkonJobsTck(self):

        self.driver.find_element(By.XPATH, jobs.Clkonjobsbtn_Text).click()
        time.sleep(3)

    def ChangeOfAddress(self, ForwardEmail, UpdateAddress):

        AllRadioButton = self.driver.find_elements(By.XPATH, jobs.SelectTheRatioBytton_xpath)
        for R in AllRadioButton:
            if R.text == ForwardEmail:
                R.click()
                time.sleep(2)
            if R.text == UpdateAddress:
                R.click()
                time.sleep(2)
        self.driver.find_element(By.XPATH, jobs.ClkonNextButton_xpath).click()
        time.sleep(5)

    def CLickONNEXTBUTTON(self):

        self.driver.find_element(By.XPATH, jobs.CLkonNextBUtton_xpath).click()

    def ClickOnNextButton1(self):

        self.driver.find_element(By.XPATH, jobs.ClkonNextButton_xpath).click()
        time.sleep(5)

    def ClkonBrowseButton(self, Upload):

        self.driver.find_element(By.XPATH, jobs.ClkOnBrowse_xpath).click()
        time.sleep(3)
        autoit.win_wait_active("Open")
        autoit.control_set_text("Open", "Edit1", Upload)
        time.sleep(3)
        autoit.send("{ENTER}")
        time.sleep(3)
        self.driver.find_element(By.XPATH, jobs.ClkonDontSaveButton_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, jobs.ClkOnNextButtonSelectDocument_xpath).click()
        time.sleep(5)

    def ClkOnOnlineEditor(self):

        self.driver.find_element(By.XPATH, jobs.ClkonCreateLetterOnline_xpath).click()
        time.sleep(5)

    def CreateOnlineFormat(self, notes):

        action = ActionChains(self.driver)
        action.send_keys(Keys.CONTROL).send_keys(notes).perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH, jobs.ClkonNextButton_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, jobs.ClkonDontSaveButton_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, jobs.ClkonNextButton_xpath).click()
        time.sleep(5)

    def SelectPdf(self):

        self.driver.find_element(By.LINK_TEXT, jobs.ClkonPdf_Linktext).click()

    def SelectOnline(self):

        self.driver.find_element(By.XPATH, jobs.SelectTemplate_xpath).click()

    def SelectBandWORColour(self, text):

        fo = self.driver.find_elements(By.XPATH, jobs.ClkonBwC_xpath)
        for ele in fo:
            if ele.text == text:
                ele.click()
                break

    def SelectFromAddress(self, Name1, Company, Add1, Add2, City, State, Zip):

        self.driver.find_element(By.XPATH, jobs.ClkonSelFromAdd_AddNewAddress_xpath).click()
        self.driver.find_element(By.XPATH, jobs.ClkonTextonly_xpath).click()
        self.driver.find_element(By.ID, jobs.Enter_Name_Id).send_keys(Name1)
        self.driver.find_element(By.ID, jobs.Enter_company_id).send_keys(Company)
        self.driver.find_element(By.ID, jobs.Enter_Address1_id).send_keys(Add1)
        self.driver.find_element(By.ID, jobs.Enter_Address2_id).send_keys(Add2)
        self.driver.find_element(By.ID, jobs.Enter_City_id).send_keys(City)
        self.driver.find_element(By.ID, jobs.Enter_State_id).send_keys(State)
        self.driver.find_element(By.ID, jobs.Enter_Pin_ID).send_keys(Zip)
        time.sleep(2)
        self.driver.find_element(By.XPATH, jobs.ClkOnAdd_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, jobs.ClkonNextButton_xpath).click()
        time.sleep(10)

    def ImageWithText(self, Upload):

        self.driver.find_element(By.XPATH, jobs.ClkonSelFromAdd_AddNewAddress_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, jobs.ClkonImagewithText_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, jobs.ClkonBrowse_xpath).click()
        time.sleep(2)
        autoit.win_wait_active("Open")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", Upload)
        time.sleep(2)
        autoit.send("{ENTER}")
        time.sleep(3)
        self.driver.find_element(By.XPATH, jobs.ClkonDefaultaddress_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, jobs.ClkOnAdd_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, jobs.ClkonNextButton_xpath).click()
        time.sleep(5)

    def ReviewAndConfirm(self):

        self.driver.find_element(By.XPATH, jobs.ClkonPaywithCredit_xpath).click()
        time.sleep(3)

    def ReviewAndConfirm2(self):

        self.driver.find_element(By.XPATH, jobs.ClkonCertifiedmail_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, jobs.ClkonPaywithCredit_xpath).click()
        time.sleep(2)

    def ReviewAndConfirm3(self):

        self.driver.find_element(By.XPATH, jobs.ClkonOneBusinessDay_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, jobs.ClkonPostage_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, jobs.ClkonPaywithCredit_xpath).click()
        time.sleep(2)

    def TextWideView(self, Address, City, State, Zip, Upload):

        self.driver.find_element(By.XPATH, jobs.ClkonSelFromAdd_AddNewAddress_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, jobs.ClkonTextunderwideview_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, jobs.ClkonBrowse_Underwide_xpath).click()
        time.sleep(2)
        autoit.win_wait_active("Open")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", Upload)
        time.sleep(2)
        autoit.send("{ENTER}")
        time.sleep(3)
        self.driver.find_element(By.ID, jobs.EntAddress_id).send_keys(Address)
        time.sleep(2)
        self.driver.find_element(By.ID, jobs.Ent_city_id).send_keys(City)
        time.sleep(2)
        self.driver.find_element(By.ID, jobs.Ent_state_id).send_keys(State)
        time.sleep(2)
        self.driver.find_element(By.ID, jobs.Ent_zip_id).send_keys(Zip)
        time.sleep(2)

    def ClickAddButton(self):

        self.driver.find_element(By.XPATH, jobs.ClkAddButton_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, jobs.ClkonNextButton_xpath).click()
        time.sleep(5)

    def ClickonConatcts(self, name):

        self.driver.find_element(By.LINK_TEXT, jobs.ClkonContacts_Link).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, jobs.ClkonMailBtn_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.ID, jobs.EnterContactName_ID).send_keys(name)
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, jobs.ClkonSelectall_Linktext).click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, jobs.ClkonDeselect_Linktext).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, jobs.ClkonContactCheckBox_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, jobs.ClkonNextButton_xpath).click()
        time.sleep(5)

    def SelectFont(self, Size):

        self.driver.find_element(By.XPATH, jobs.ClickOnFontDropDown_xpath).click()
        time.sleep(3)
        allSizes = self.driver.find_elements(By.XPATH, jobs.Clkondrop_id)
        for s in allSizes:
            if s.text == Size:
                s.click()
                time.sleep(2)

    def clkontrack(self):

        msg = self.driver.find_element(By.TAG_NAME, "Body").text
        for m in msg:
            print(m)
            if m == "Track":
                self.driver.find_element(By.XPATH, jobs.Sltontrk).click()
                # self.driver.find_element(By.LINK_TEXT, "Track").click()
                time.sleep(3)
                break
            else:
                self.driver.find_element(By.LINK_TEXT, "Next").click()
                time.sleep(3)



    # def SelectFontsize(self, Font):
    #     self.driver.find_element(By.XPATH, jobs.ClickOnFontDropDown_xpath).click()
    #     time.sleep(3)
    #     fo = self.driver.find_elements(By.XPATH, jobs.Clkondrop_id)
    #     for ele in fo:
    #         if ele.text == Font:
    #             ele.click()
    #             break

    def SelectStyele(self, style):

        self.driver.find_element(By.XPATH, jobs.ClickOnDropDwon_xpath).click()
        time.sleep(3)
        fo = self.driver.find_elements(By.XPATH, jobs.ClkonStyle_xpath)
        for ele in fo:
            if ele.text == style:
                ele.click()
                break

    # def clkontrack(self, input):
    #     if input == "Track":
    #         self.setitem = self.driver.find_element(By.XPATH, jobs.Sltontrk)
    #
    #     else:
    #         self.setitem = self.driver.find_element(By.XPATH, jobs.CLkonNext_xpath)
    #         time.sleep(5)






