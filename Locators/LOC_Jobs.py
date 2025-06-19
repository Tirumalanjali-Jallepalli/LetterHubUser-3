class jobs:

    Clkonjobsbtn_Text = "/html/body/div[2]/div[1]/nav/ul/li[2]/a"
    ClkonStartNewJob_Btn_Xpath = "//div[@class='main-content ']//button[@class='btn btn-primary btn-xs']"
    ClkonDrp1_xpath = "//span[@class='k-select']"
    ClkonEditBtn_xpath = "//a[@class='hylink text-information mr10']"
    ClkonDeleteBtn_xpath = "//u[@class='text-danger cursor-pointer']"
    ClkonDetailsBtn_xpath = "//a[@class='hylink text-information mr10']"
    ClkonContacts_Link = "Contacts"
    ClkonMailBtn_xpath = "//a[@data-ng-click='$ctrl.mailSelectedContacts()']"

    # ######################### Select Recipeints ###################

    EnterContactName_ID = "txtSearchText"
    ClkonSelectall_Linktext = "Select All"
    ClkonDeselect_Linktext = "Deselect All"
    Enter_Name_id = "txtSearchText"
    ClkonContactCheckBox_xpath = '//*[@id="scrollTable"]/tbody[5]/tr[1]/td[1]/label/span'
    ClkonNextButton_xpath = '//button[contains(text(), "Next")]'
    CLkonNextBUtton_xpath = "//button[@data-ng-click='selectFromAddressNext()']"
    ClkOnNextButtonSelectR_xpath = "//button[@data-ng-click='mailSelectedContacts()']"
    ClkOnNextButtonSelectDocument_xpath ="//button[@data-ng-click='selectFromAddressNext()']"

    # ####################### Change Of Address #####################

    SelectTheRatioBytton_xpath = '//span[@class="check-bo-text"]'
    ClkonPrevBtn1_xpath = '//button[@class="btn btn-primary"]'

    # ################## Select Document ##############################

    ClkOnBrowse_xpath = "//label[@class='btn btn-primary']"
    ClkonCreateLetterOnline_xpath = "//button[@ng-click='$ctrl.createOnlineLetter()']"
    ClkonPdf_Linktext = "PDFTemplate"
    SelectTemplate_xpath = "//a[@class='template-overflow-hidden text-capitalize']"
    ClkonPrevBtn2_xpath = '//button[@class="btn btn-primary"]'
    ClkonDontSaveButton_xpath = "//button[@class='btn btn-primary btn-sm min-width200']"

    # ##################### Preview #####################################

    ClkonPrevBtn3_xpath = '//button[@class="btn btn-primary"]'

    # ############### Select From Address ##################################

    ClkonBwC_xpath = "//span[@class='cb-inner']"
    ClkonSelFromAdd_AddNewAddress_xpath = "//a[@ng-click='$ctrl.openFromAddressFormModal()']"
    ClkonTextonly_xpath = "//button[@data-ng-click='openAddressForm(1)']"
    ClkonImagewithText_xpath = "//button[@data-ng-click='openAddressForm(2)']"
    ClkonTextUnderWideImage_xpath = "//button[@data-ng-click='openAddressForm(3)']"
    Enter_Name_Id ="txtName"
    Enter_company_id = "txtCompany"
    Enter_Address1_id = "txtAddressLine1"
    Enter_Address2_id = "txtAddressLine2"
    Enter_City_id = "txtCity"
    Enter_State_id = "txtState"
    Enter_Pin_ID = "txtZip"
    ClkOnAdd_xpath = '//button[@type="submit"]' #"//button[@ng-click='$ctrl.addFromAddress() ']"
    ClkonImageandText_Linktext = "Image & Text"
    ClkonBrowse_xpath = "//div[@class='btn btn-primary mb30']"
    ClkonDefaultaddress_xpath = "//a[@class='hylink text-information pull-right']"
    ClkonAdd_Linktext = '//button[@type="submit"]'#"Add"
    SelectImagewithText_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[6]/div/div/div[2]/" \
                                "select-from-address-component/div[3]/div[2]/div/ul/li[1]/div/div/div/span/label/span"
    ClkonPrevBtn4_xpath = '//button[@class="btn btn-primary"]'
    ClkonTextunderwideview_xpath = "//button[@data-ng-click='openAddressForm(3)']"
    ClkonBrowse_Underwide_xpath = "//div[@class='btn btn-primary mb30']"
    EntAddress_id = "txtAddressLine1"
    Ent_city_id = "txtCity"
    Ent_state_id = "txtState"
    Ent_zip_id = "txtZip"
    Clkondrop_id = "//ul[@id='ddlFontSize_listbox']/li"
    ClickOnFontDropDown_xpath = "//span[@aria-owns='ddlFontSize_listbox']"
    ClkAddButton_xpath = '//button[@type="submit"]' #"//button[@ng-click='$ctrl.addFromAddress() ']"
    Selectfromdropdown_xpath = "//select[@class='form-control input-sm ng-pristine ng-valid ng-not-empty ng-touched']" \
                               "/option"
    ClkonStyle_xpath = "//ul[@id='selectFont_listbox']/li"
    ClickOnDropDwon_xpath = "/html/body/div[1]/div/div/add-address-form-modal/div[2]/div[1]/div/div/form/div[2]/div/span/span/span[2]/span"


    # ############## Review & Confirm #############################


    ClkonFirstclassmail_Linktext = "USPS - FIRST CLASS - $0.75"
    ClkonOneBusinessDay_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[7]/div/div/div[2]" \
                                "/review-confirm-component/div/div[1]/form/div[2]/div[3]/label/span[1]/i"
    ClkonPostage_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[7]/" \
                         "div/div/div[2]/review-confirm-component/div/div[1]/form/div[2]/div[4]/div[1]/label/span/i"
    ClkonCertifiedmail_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[7]/div/div/div[2]/" \
                               "review-confirm-component/div/div[1]/form/div[2]/div[2]/div/label/span"
    ClkonPaywithCredit_xpath = "//div[@class='align-items-center']//button[@class='btn btn-primary btn-sm']"

    Sltontrk = "//a[@data-ng-click='$ctrl.GetUSPSTracking(recepient.TrackingDetailsXML)']"
    CLkonNext_xpath = "//a[@ng-click='selectPage(page + 1, $event)']"


    ##############################################################

class Loc_Jobs:

    ClkOnJobsModule_xpath = "/html/body/div[2]/div[1]/nav/ul/li[2]/a/span"
    ClkOnStatusDrpDown_xpath = '//span[@aria-owns="ddlFilterStatus_listbox"]/span/span' # '/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/span/span/span[2]/span'
    AllStatusList_xpath = '//ul[@id="ddlFilterStatus_listbox"]/li'
    ClkOnDateDrpDown_xpath = '//span[@aria-owns="ddlFilterDate_listbox"]/span/span' #'/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/sp an/span/span[2]/span'
    AllDateList_xpath = '//ul[@id="ddlFilterDate_listbox"]/li'
    ClkOnBatchDrpDown_xpath = '/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/span/span/span[2]/span'
    AllBatchList_xpath = '//ul[@id="ddlFilterGroupBatches_listbox"]/li'

    # #### Delete the Particular Draft Job #####

    ClkOnBatchName_xpath = '//div[@ng-if="!batch.BatchMailedCopyS3Key"]'
    # ClkOnDelDraftJob_xpath = '//u[@ng-click="$ctrl.deleteDraft(batch.BatchID)"]'
    ClkOnDelDraftJob_xpath ='.//following::u[@ng-click="$ctrl.deleteDraft(batch.BatchID)"]' #'//div[contains(text(), .)]/following::u[@ng-click="$ctrl.deleteDraft(batch.BatchID)"]'
    ClkOnDeleteJob_No_xpath = '//button[@tabindex="2"]' #'//div[@class="sweet-alert showSweetAlert visible"]/button[@class="cancel"]'
    ClkOnDeleteJob_Yes_xpath = '//button[@tabindex="1"]' #'//div[@class="sweet-alert showSweetAlert visible"]/button[@class="confirm"]'
    ClkOnNextBtn_xpath = '//a[@ng-click="selectPage(page + 1, $event)"]'

    # #### Delete the particular Processing Job #####
    ClkOnDelProcessingJob_xpath = './/following::u[@ng-click="$ctrl.deleteBatch(batch.BatchID)"]' #'/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/group-by-job-row-component/table/tbody[1]/tr/td[8]/u'

    # #### Details of Processing Job #####
    ClkOnDetailsOfProcessingJob_text = 'Details'
    ClkOnRecipient_text = 'Recipient'
    ClkOnRenameBtn_text = '(Rename)'
    EntUpdateJobName_id = 'txtMailingJobName'
    ClkOnRenameSaveChanges_xpath = '//button[@data-ng-click="renameJobName()"]'
    ClkOnRenameClose_xpath = '//button[@data-ng-click="//button[@data-ng-click="closeRenameJobNameModal()"]"]'


    ClonFnotDrpdown_xpath = "//span[@aria-owns='ddlFontSize_listbox']"

    Sltontrk = "//a[@data-ng-click='$ctrl.GetUSPSTracking(recepient.TrackingDetailsXML)']"
