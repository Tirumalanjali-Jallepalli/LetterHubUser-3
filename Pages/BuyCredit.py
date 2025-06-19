import time
from selenium.webdriver.common.by import By
from Locators.LOC_BuyCredit import Loc_BuyCredit


class BuyCredits:

    select_cards_xpath = "//div[@class='col-md-6 col-lg-4']/div/div/label/span/i"

    def __init__(self, driver):
        self.driver = driver

    def ClkOnBuyCreditModule(self):
        self.driver.find_element(By.XPATH, Loc_BuyCredit.ClkOnBuyCreditsModule_xpath).click()

    def Clk_creditAmt_drp(self):
        self.driver.find_element(By.XPATH, Loc_BuyCredit.ClkOn_drp_CreditAmount_xpath).click()

    def selectCreditAmt(self, amount):
        all_amounts = self.driver.find_elements(By.XPATH, Loc_BuyCredit.select_creditamount_xpath)

        for amt in all_amounts:
            # print(amt.text)
            if amt.text == amount:
                amt.click()
                time.sleep(2)
                break

    def selectCard(self):

        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div[3]/div[1]/label/span').click()
        # all_cards = self.driver.find_elements(By.ID, self.select_cards_xpath)
        # for cards in all_cards:
        #     if cards.text == card:
        #         cards.click()

        # self.driver.find_element(By.XPATH,
        #                          "//td[contains(text(), 'newite')]//following::td//a[@class='deleteitem']").click()

    def selectanotherCard(self, fname, lname, CardNo, ExpireDate, code):
        self.driver.find_element(By.XPATH, Loc_BuyCredit.clk_anotherCard_xpath).click()
        self.driver.find_element(By.ID, Loc_BuyCredit.entFname_id).send_keys(fname)
        self.driver.find_element(By.ID, Loc_BuyCredit.entLname_id).send_keys(lname)
        self.driver.find_element(By.ID, Loc_BuyCredit.entCardNo_id).send_keys(CardNo)
        self.driver.find_element(By.ID, Loc_BuyCredit.entExpireDate).send_keys(ExpireDate)
        self.driver.find_element(By.ID, Loc_BuyCredit.entSecurityCode).send_keys(code)
        time.sleep(5)
        self.driver.find_element(By.XPATH, Loc_BuyCredit.check_SaveCard_xpath).click()

    def clk_BuyCredit(self):
        self.driver.find_element(By.XPATH, Loc_BuyCredit.clkon_buycredits_xpah).click()