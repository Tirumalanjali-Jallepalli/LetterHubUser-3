class Loc_AssistedJob:

    # ####### Assisted Job #########
    clkonJobsBtn_xpath = '/html/body/div[2]/div[1]/nav/ul/li[2]/a/span'
    clkonAutoInvoiceScanner_text = 'Auto Invoice Scanner'
    MainPdfBrowse_xpath = "//label[@ngf-select='$ctrl.mainFileUpload($file, $invalidFiles)']"
    checkSaveContact_xpath = "//div[@class='text-center']/label"
    BackPdfBrowse_xpath = "//label[@ngf-select='$ctrl.backFileUpload($file, $invalidFiles)']"
    clkonNextBtn_xpath = "//div[@class='pull-right']/button"

    # ###### Enter Assisted Job ############
    clkonOk_class = 'confirm'
    entInstuctions_id = 'txtInstructions'
    entJobName_id = 'txtFileName'
    entEmailPhone_id = 'txtEmailPhone'
    checkToAddress_xpath = "//label[@ng-click='onToAddressCheck()']"
    entToAddress_id = 'txtToaddress'
    checkFromAdress_xpath = "//label[@ng-click='onFromAddressCheck()']"

    # #### Add From Address #####
    ClkOnAddNewFromAddress_text = 'Add New From Address'
    SelAddressType = "//div[@class='row']/div/button"
    ClkOnTextOnly_xpath = "//button[@data-ng-click='openAddressForm(1)']"
    ClkOnImageText_xpath = "//button[@data-ng-click='openAddressForm(2)']"
    ClkOnImageOnly_xpath = "//button[@data-ng-click='openAddressForm(3)']"
    # #### Select From Address Book #####
    SelFromAddressBook_text = 'Select From Address Book'
    SearchContactName_id = 'txtSearchText'
    CheckAddress_xpath = '//table[@class="table mb0"]//span/i'
    ClkOnAddBtn_xpath = '//div/button[@ng-click="$ctrl.addFromAddress()"]'
    ClkOnClose_xpath = '//div/button[@ng-click="$ctrl.cancel()"]'
    UseDefaultFromAddress_text = 'Use Default From Address'

    EntName_id = 'txtName'
    EntCompany_id = 'txtCompany'
    EntAddLine1_id = 'txtAddressLine1'
    EntAddLine2_id = 'txtAddressLine2'
    EntCity_id = 'txtCity'
    EntState_id = 'txtState'
    EntZip_id = 'txtZip'
    SelFontSize_id = 'ddlFontSize'
    clkonAdd_xpath = "//form[@novalidate='novalidate']//button[@type='submit']"

    # #### Upload Image #####

    ClkOnBrowseBtn_xpath = "//div[@class='input-group-btn']/div"
    CheckReturnAddress_xpath = '//label[@ng-click="onReturnAddressCheck()"]'
    ClkOnAddNewReturnAddress_text = 'Add New Return Address'
    AllCarriers_xpath = '//div[@class="carrier"]//label'
    AllPageSizes_xpath = '//div[@class="form-group mb10"]/label'
    AllReturnEnvelope_xpath = '//div[@class="form-group"]/label'
    AllPrintOptions_xpath = '//div[@class="form-group align-items-center"]/label'
    AllCheckBoxs_xpath = '//div/label[@class="cb-checkbox round"]'

    # ##### Change-Of-Address ######

    AllChangeOfAddressRadioBtns_xpath = '//span[@class="check-bo-text"]'
    CheckUpdatedAddress_xpath = '//label[@class="cb-checkbox"]//span[@class="check-bo-text"]'
    AllPaymentOptions_xpath = '//div[@class="row form-group"]//div//label'
    ChargeMyCreditCard_xpath = '/html/body/div[2]/div[2]/div[2]/div[2]/ng-form/div[14]/div/div/div/div/div[1]/label'
    SelCreditCard_id = 'creditcard'
    ClkOnSubmitTheJob_xpath = '//button[@ng-click="submitJob()"]'
    ClkOnOkBtn_xpath = '//button[@class="confirm"]'
    ClkonGenerateInvoice_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/ng-form/div[14]/div/div/div/label[3]/span"

    # #### Existing Address ##########

    ClkonExitAdd_xpath = "//a[@ng-click='openexistingFromAddressFormModal()']"
    ClkonratiBtn_xpath = "/html/body/div[1]/div/div/div[2]/ul[2]/li[1]/div/div/div/label/span"
    ClkonCloseBtn_xpath = "//i[@class='fa fa-close mr5']"
