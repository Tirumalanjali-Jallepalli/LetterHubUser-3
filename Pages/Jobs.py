import time
from selenium.webdriver.common.by import By
from Locators.LOC_Jobs import Loc_Jobs
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Jobs:

    def __init__(self, driver):
        self.driver = driver

    def ClkOnJobsModule(self):
        self.driver.find_element(By.XPATH, Loc_Jobs.ClkOnJobsModule_xpath).click()

    def SelStatusDrpDown(self, Status):
        self.driver.find_element(By.XPATH, Loc_Jobs.ClkOnStatusDrpDown_xpath).click()
        time.sleep(3)
        allElements = self.driver.find_elements(By.XPATH, Loc_Jobs.AllStatusList_xpath)

        for e in allElements:
            if e.text == Status:
                e.click()
                time.sleep(2)
                break

    def SelDateDrpDown(self, Date):
        self.driver.find_element(By.XPATH, Loc_Jobs.ClkOnDateDrpDown_xpath).click()
        time.sleep(3)
        allElements = self.driver.find_elements(By.XPATH, Loc_Jobs.AllDateList_xpath)

        for e in allElements:
            if e.text == Date:
                e.click()
                time.sleep(2)
                break

    def SelGroupBatchesDrpDown(self, GroupBatches):
        self.driver.find_element(By.XPATH, Loc_Jobs.ClkOnBatchDrpDown_xpath).click()
        time.sleep(3)
        allElements = self.driver.find_elements(By.XPATH, Loc_Jobs.AllBatchList_xpath)

        for e in allElements:
            if e.text == GroupBatches:
                e.click()
                time.sleep(2)
                break

    def ClkOnDraftJob_DeleteBtn(self, Name):
        Delete_xpath = f"{Loc_Jobs.ClkOnBatchName_xpath}[contains(text(), '{Name}')]"
        Del = self.driver.find_element(By.XPATH, Delete_xpath)
        Del_link = Del.find_element(By.XPATH, Loc_Jobs.ClkOnDelDraftJob_xpath)
        Del_link.click()
        time.sleep(3)
        print(f"Deleted job: {Name}")

    def ClkOnDeleteJob_Action(self, action):
        if action == "Yes":
            self.driver.find_element(By.XPATH, Loc_Jobs.ClkOnDeleteJob_Yes_xpath).click()
            time.sleep(2)
        elif action == "No":
            self.driver.find_element(By.XPATH, Loc_Jobs.ClkOnDeleteJob_No_xpath).click()
            time.sleep(2)

    def ClkOnProcessingJob_DeleteBtn(self, action, Name):

        while True:
            wait = WebDriverWait(self.driver, 10)

            job_xpath = Loc_Jobs.ClkOnBatchName_xpath.format(Name=Name.strip())

            print(f"Looking for job: '{Name.strip()}' with XPath: {job_xpath}")

            # Wait until job element is present
            job_element = wait.until(EC.presence_of_element_located((By.XPATH, job_xpath)))

            if job_element.text.strip() == Name.strip():
                delete_button = job_element.find_element(By.XPATH, Loc_Jobs.ClkOnDelProcessingJob_xpath)
                wait.until(EC.element_to_be_clickable((By.XPATH, Loc_Jobs.ClkOnDelProcessingJob_xpath)))
                delete_button.click()
                time.sleep(3)  # Allow modal to appear

                # Click on Yes or No based on action
                if action == 'Yes':
                    self.driver.find_element(By.XPATH, Loc_Jobs.ClkOnDeleteJob_Yes_xpath).click()
                    time.sleep(3)
                else:
                    self.driver.find_element(By.XPATH, Loc_Jobs.ClkOnDeleteJob_No_xpath).click()
                    time.sleep(3)

                time.sleep(3)  # Allow time for action to process
                print(f"Deleted job: {Name} with action: {action}")

                return True  # Exit function after deleting job

            # Check if the next button is enabled for pagination
            try:
                next_button = self.driver.find_element(By.XPATH, Loc_Jobs.ClkOnNextBtn_xpath)
                if next_button.is_enabled():
                    next_button.click()
                    WebDriverWait(self.driver, 10).until(EC.staleness_of(next_button))  # Wait for the page to load
                else:
                    print("Next button disabled. No more pages to search.")
                    break  # Exit the loop if there are no more pages
            except:
                print("Next button not found or an issue occurred.")
                break  # Exit the loop if navigation is not possible

        print(f"Job '{Name}' not found in any page.")
        return False  # Return false if job was not found

        # self.driver.find_element(By.XPATH, Loc_Jobs.ClkOnDelProcessingJob_xpath).click()
        # time.sleep(2)

    def ClkOnProcessingJob_DetailsBtn(self):
        self.driver.find_element(By.LINK_TEXT, Loc_Jobs.ClkOnDetailsOfProcessingJob_text).click()
        time.sleep(2)

    def ClkOnRecipient(self):
        self.driver.find_element(By.LINK_TEXT, Loc_Jobs.ClkOnRecipient_text).click()

    def ClkOnRenameBtn(self):
        self.driver.find_element(By.LINK_TEXT, Loc_Jobs.ClkOnRenameBtn_text).click()

    def UpdateJobName(self, RenameTheJob):
        self.driver.find_element(By.ID, Loc_Jobs.EntUpdateJobName_id).clear()
        self.driver.find_element(By.ID, Loc_Jobs.EntUpdateJobName_id).send_keys(RenameTheJob)

    def RenameJobAction(self, action):
        if action == 'Save Changes':
            self.driver.find_element(By.XPATH, Loc_Jobs.ClkOnRenameSaveChanges_xpath).click()
        else:
            self.driver.find_element(By.XPATH, Loc_Jobs.ClkOnRenameClose_xpath).click()

    def ClkOnTrack(self, address_name):
        while True:
            try:
                # self.driver.find_element(By.XPATH, '//div[@title="Certified Mail"]/following::td/a[text()="Track"]').click()
                # self.driver.find_element(By.XPATH, '//td[text()="37275 St  Rt 17m M  Middle Island NY 11953"]//following::a[text()="Track"]').click()
                self.driver.find_element(By.XPATH,
                                         "//td[text()='" + address_name + "']//following-sibling::td/a[text()='Track']").click()
                time.sleep(4)
                self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/button').click()
                time.sleep(2)
                break
            except NoSuchElementException:
                # If the target name is not found, go to the next page
                try:
                    next_page_button = self.driver.find_element(By.LINK_TEXT, 'Next')
                    next_page_button.click()
                    time.sleep(2)

                except NoSuchElementException:
                    # If there are no more pages to search, exit the loop
                    print('Target name not found.')
                    break
