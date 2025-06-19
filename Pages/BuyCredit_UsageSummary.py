import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Locators.LOC_BuyCredit import Loc_BuyCredit
from selenium.webdriver.common.action_chains import ActionChains
from utilities.customLogger import LogGen
from selenium.common.exceptions import NoSuchElementException


class UsageSummary:
    logger = LogGen.log()

    def __init__(self, driver):
        self.driver = driver

    def ClkOnBuyCreditModule(self):
        self.driver.find_element(By.XPATH, Loc_BuyCredit.ClkOnBuyCreditsModule_xpath).click()

    def ClkOnUsageSummary(self):
        self.driver.find_element(By.LINK_TEXT, Loc_BuyCredit.ClkOnUsageSummary_text).click()

    def clkDateDrp(self):
        self.driver.find_element(By.XPATH, Loc_BuyCredit.clk_date_drp_xpath).click()

    def ClkOnCustomRange(self, FromDate, ToDate):
        self.driver.find_element(By.XPATH, Loc_BuyCredit.clkCustomRange_xpath).click()
        self.logger.info("********** Enter From date *********")
        self.driver.find_element(By.ID, Loc_BuyCredit.entFromDate_id).send_keys(FromDate)
        time.sleep(3)
        self.driver.find_element(By.ID, Loc_BuyCredit.entFromDate_id).send_keys(Keys.TAB)
        self.logger.info("********** Enter To date *********")
        self.driver.find_element(By.ID, Loc_BuyCredit.entToDate_id).send_keys(ToDate)
        time.sleep(5)
        self.driver.find_element(By.XPATH, Loc_BuyCredit.clkOnOk_xpath).click()

    def sel_dateDrp(self, category):
        all_categories = self.driver.find_elements(By.XPATH, Loc_BuyCredit.select_date_drp_xpath)
        for d in all_categories:
            if d.text == category and d.text != 'Custom Range':
                d.click()
            # else:
            #
            #     self.driver.sel_customRange(FromDate, ToDate)

    # *********** Usage Summary Download By Date *************
    def ClkOnDownloadUsageSummaryByDate(self):
        self.driver.find_element(By.XPATH, Loc_BuyCredit.ClkOnDownloadUsageSummaryByDate_xpath).click()

    # ############# Usage Summary View & Download ####################
    def UncheckGroupByDate(self):
        self.driver.find_element(By.XPATH, Loc_BuyCredit.uncheck_GroupByDate_xpath).click()

    def ClkOnViewAndDownload(self, sel_date):
        try:
            view_download = self.driver.find_element(By.XPATH,
                                                     "//td[contains(text(), '" + sel_date + "')]//following::td//a[@class='text-information hylink']")
            view_download.click()
            time.sleep(4)
            action = ActionChains(self.driver)
            action.send_keys(12 * Keys.TAB)
            time.sleep(2)
            action.send_keys(Keys.ENTER)
            action.perform()
            time.sleep(2)
            action1 = ActionChains(self.driver)
            action1.key_down(Keys.SHIFT).send_keys(11 * Keys.TAB).key_up(Keys.SHIFT).send_keys(Keys.ENTER).perform()
            time.sleep(2)
        except NoSuchElementException:
            print("No Date found")

    def ClkOnCloseUsageSummaryView(self):
        self.driver.find_element(By.XPATH, Loc_BuyCredit.ClkOnCloseUsageSummaryView_xpath).click()

    def ClkOnDownloadSymbol(self):
        download = self.driver.find_element(By.XPATH, Loc_BuyCredit.clkOnDownloadSymbol_xpath)
        action = ActionChains(self.driver)
        action.click(download)
        action.perform()
