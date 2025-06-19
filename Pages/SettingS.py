import string
import time
from selenium.webdriver.common.by import By
from Locators.LOC_Settings import Settings
import random
from utilities.customLogger import LogGen


class Setings:

    logger = LogGen.log()

    def __init__(self, driver):
        self.driver = driver

    def MyAccount(self, Name, compa):

        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkonmyaccount_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.ID, Settings.Entname_id).clear()
        self.driver.find_element(By.ID, Settings.Entname_id).send_keys(Name)
        time.sleep(3)
        self.driver.find_element(By.ID, Settings.Entcomp_id).clear()
        self.driver.find_element(By.ID, Settings.Entcomp_id).send_keys(compa)
        time.sleep(3)
        self.driver.find_element(By.XPATH, Settings.Clkonsave_xpath).click()

    def DefaultAddress(self, fname, compnam, Address1, Address2, city, state, zip):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.ClkonDefaultadd_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Entfname_id).clear()
        self.driver.find_element(By.ID, Settings.Entfname_id).send_keys(fname)
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Entcpmname_id).clear()
        self.driver.find_element(By.ID, Settings.Entcpmname_id).send_keys(compnam)
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Entaddname1_id).clear()
        self.driver.find_element(By.ID, Settings.Entaddname1_id).send_keys(Address1)
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Entaddnam2_id).clear()
        self.driver.find_element(By.ID, Settings.Entaddnam2_id).send_keys(Address2)
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Entcity_id).clear()
        self.driver.find_element(By.ID, Settings.Entcity_id).send_keys(city)
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Entstate_id).clear()
        self.driver.find_element(By.ID, Settings.Entstate_id).send_keys(state)
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Entzip_id).clear()
        self.driver.find_element(By.ID, Settings.Entzip_id).send_keys(zip)
        time.sleep(3)
        self.driver.find_element(By.XPATH, Settings.Clkonsave2_xpath).click()
        time.sleep(3)

    def Job_PrintPreferences(self):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.CLkonjobprefe_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkonblkadwhit_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkonclor_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.CLkonwithoutpostage_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkonwithpostage_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkonfriendlyreturnenvolope_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkonchanofadd_yes_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkonchanofadd_no_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkon_yes_chanofadd_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkon_no_changofadd).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.ClkonCheckbox_xpath).click()
        time.sleep(5)

    def PaymentOptions(self):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.Clkon_paymentoption_xpath).click()
        time.sleep(2)

    def ClickonDropDown1(self):
        self.driver.find_element(By.XPATH, Settings.Clkon_dropdown_xpath).click()
        time.sleep(2)

    def selectFromDrop1(self, amount1):
        all_amounts = self.driver.find_elements(By.XPATH, Settings.Selectfron_dropdown_xpath)

        for amt in all_amounts:
            # print(amt.text)
            if amt.text == amount1:
                amt.click()

    def ClickonDrop2(self):
        self.driver.find_element(By.XPATH, Settings.CLkondropdown2_xpath).click()
        time.sleep(2)

    def SelectFromDropDown2(self, amount2):
        all_amounts = self.driver.find_elements(By.XPATH, Settings.Selectfrom_dropdown2_xpath)

        for amt in all_amounts:
            # print(amt.text)
            if amt.text == amount2:
                amt.click()

    def ClickonDropDown3(self):
        self.driver.find_element(By.XPATH, Settings.Clkondropdown3_xpath).click()
        time.sleep(2)

    def SelectFromDropDown3(self, amount3):
        all_amounts = self.driver.find_elements(By.XPATH, Settings.Slect_dropdown3_xpath)

        for amt in all_amounts:
            # print(amt.text)
            if amt.text == amount3:
                amt.click()

    def ClickonSaveButton(self):
        self.driver.find_element(By.XPATH, Settings.Clkon_Save_xpath).click()

    def AddNewCard(self, crdnum, fnam, lnam, exp, scty):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.Clkon_paymentoption_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.Clkonaddnewcredi_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Ent_cardnum_id).send_keys(crdnum)
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Ent_fstnam_id).send_keys(fnam)
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Ent_lstnam_id).send_keys(lnam)
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Ent_expdte_id).send_keys(exp)
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Enta_secty_id).send_keys(scty)
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.CLk_sav_xpath).click()
        time.sleep(2)

    def DeleteCard(self, Card_Number):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.Clkon_paymentoption_xpath).click()
        time.sleep(2)

        card_xpath = f"{Settings.ClkOnAllExistingCards_xpath}[contains(text(), '{Card_Number}')]"
        Card = self.driver.find_element(By.XPATH, card_xpath)
        delete_button = Card.find_element(By.XPATH, Settings.Clkondlt)
        delete_button.click()
        time.sleep(3)
        print(f"Deleted card: {Card_Number}")
        # Cards = self.driver.find_elements(By.XPATH, Settings.ClkOnAllExistingCards_xpath)
        # for Card in Cards:
        #     if Card_Number in Card.text:
        #         Delete = self.driver.find_elements(By.XPATH, Settings.Clkondlt)
        #         if Delete:
        #             Delete[0].click()
        #             time.sleep(3)
        #             break
        #         elif Card_Number == Card.text:
        #             print("Default card")
        #         else:
        #             print("Card number not showing")

    def DefaultCard(self):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.Clkon_paymentoption_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.CLkondefaultbtn).click()
        time.sleep(2)

    def EnableorDisabletheEmailtoPrint(self):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.CLkon_Emladpri_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkontoggle_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkontoggle_xpath).click()
        time.sleep(5)

    def AddEmail(self, email):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.CLkon_Emladpri_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.NAME, Settings.Ent_emailnam_name).send_keys(email)
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.CLk_ademai_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkondelt_btn_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkonyesbtn_xpath).click()

    def deleteEmail(self):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.CLkon_Emladpri_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Settings.Clkondelt_btn_xpath).click()
        time.sleep(5)

    def CreateApi(self, kee, sel, nam):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.ClkonApi_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.Clkon_createAp_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Entapikeyname_id).clear()
        self.driver.find_element(By.ID, Settings.Entapikeyname_id).send_keys(kee)
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.Clkn_dropdown_xpath).click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH, Settings.Slectfrom_dropdow_xpath).send_keys(sel)
        self.se = self.driver.find_elements(By.XPATH, Settings.Slectfrom_dropdow_xpath)
        for ele in self.se:
            if ele.text == sel:
                ele.click()
                break
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.Ent_applinam_id).clear()
        self.driver.find_element(By.ID, Settings.Ent_applinam_id).send_keys(nam)
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.Clk_SAV_xpath).click()
        time.sleep(2)

    def EditApi(self):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.ClkonApi_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.Clkon_edit_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.ID, Settings.entupdate_api_id).clear()
        self.name = ''.join(random.choice(string.ascii_lowercase) for x in range(4))
        self.driver.find_element(By.ID, Settings.entupdate_api_id).send_keys(self.name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.updtsav_xpath).click()
        time.sleep(2)

    def EnaleTheApi(self):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.ClkonApi_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.Clk_enable_xpath).click()
        time.sleep(2)

    def DisableTheApi(self):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.ClkonApi_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.Clkon_disabl_xpath).click()
        time.sleep(2)

    def AboutApi(self):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.ClkonApi_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.Clkmore_abt_api_xpath).click()
        time.sleep(20)
        # window_after = self.driver.window_handles[1]
        # self.driver.switch_to.window(window_after)
        # time.sleep(2)
        # self.driver.find_element(By.ID, self.clkonedit).click()

    def SandBox(self):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.ClkonApi_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.CLkonMor_abtsandbox_xpath).click()
        time.sleep(20)

    def PromoCode(self):
        self.driver.find_element(By.XPATH, Settings.Clkonsettingsbtn_xpath).click()
        time.sleep(2)
        self.name = ''.join(random.choice(string.ascii_lowercase) for x in range(5))
        self.driver.find_element(By.ID, Settings.Ent_promo_id).send_keys(self.name)
        time.sleep(2)
        self.driver.find_element(By.XPATH, Settings.CLkon_redem_btn_xpath).click()
        time.sleep(2)


