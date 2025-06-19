class Contact_Locators:

    clkonContacts_xpath = '/html/body/div[2]/div[1]/nav/ul/li[8]/a/span'
    clkonAddNewContact_xpath = "//div[@class='form-group']/ul/li/a[text()='Add New Contact']"
    selRadiobtn_xpath = "//div[@class='col-md-12']/label"

    # ###### Add Contact Contact details #######
    clkonPersonRadiobtn_xpath = '//*[@id="rootwizard"]/div/div/div[1]/div/div/div/div[1]/div/label[1]'
    clkonBusinessRadiobtn_xpath = '//*[@id="rootwizard"]/div/div/div[1]/div/div/div/div[1]/div/label[2]'
    entFirstName_id = 'txtFirstName'
    entMiddleName_id = 'txtMiddleName'
    entLastName_id = 'txtLastName'
    entPrefix_id = 'txtPrefix'
    entSuffix_id = 'txtSuffix'
    entJobTitle_id = 'txtJobTitle'
    entCompany_id = 'txtCompany'
    ent_Notes_id = 'txtNotes'

    # ####### Select Tags #######
    clk_Tags_drp_xpath = "//div[@class='groups-multiselect groups-multiselect-contacts']/div"
    all_tags_drp_xpath = "//ul[@class='dropdown-menu dropdown-menu-form']/li/a"

    # ##### Create New tag ########
    clkonCreateNewTag_xpath = '//*[@id="rootwizard"]/div/div/div[1]/div/div/div/div[3]/div/div[1]/div/div[2]/div/div/' \
                              'ul/li[13]/a/span[2]/span'
    entNewtagName_id = 'tagName'
    clkonOkbtn_xpath = '/html/body/div[1]/div/div/div[1]/div[2]/button[1]'

    # ######## Add New Address ############
    clkonAddNewAddress_xpath = "//div[@class='pull-right']/a[@data-ng-click='addNewAddress()']"
    sel_addressPurpose_name = 'ddlAddressGroups_input'
    entAddLine1_id = 'txtAddressLine1'
    entAddLine2_id = 'txtAddressLine2'
    entCity_id = 'txtAddressCity'
    entState_id = 'txtAddressState'
    entZip_id = 'txtAddressZip'
    entCountry_name = 'selectcountry_input' #'ddlAddressCountry_input'
    ClkOnCountryDropdown_xpath = "//span[@aria-controls='ddlAddressCountry_listbox']"
    # all_Country_xpath = '//ul[@id="ddlAddressCountry_listbox"]/li'
    all_Country_xpath = '//ul/li[@role="option"]'

    # ########## Add New Phone Number ##############
    clkonAddNewPhoneNo_xpath = "//div[@class='pull-right']/a[@data-ng-click='addNewPhoneNumber()']"
    sel_phonePurpose_name = 'ddlPhoneGroups_input'
    entPhoneNo_id = 'txtPhoneNumber'

    # ########## Add New Email Address ##########
    clkonAddNewEmail_xpath = "//div[@class='pull-right']/a[@data-ng-click='addNewEmailAddress()']"
    sel_EmailPurpose_name = 'ddlEmailGroups_input'
    entEmail_id = 'txtEmailAddress'

    # ########### Add New Date #############
    clkonAddNewdate_xpath = "//div[@class='pull-right']/a[@data-ng-click='addNewDate()']"
    sel_DatePurpose_name = 'ddlDateGroups_input'
    entDate_id="txtDate"

    # ########### Add New url #############
    clkonAddNewuRL_xpath = "//div[@class='pull-right']/a[@data-ng-click='addNewUrl()']"
    sel_URLPurpose_name = 'ddlUrlGroups_input'
    ClkOnAddNewURL_xpath = '//a[@data-ng-click="addNewUrl()"]'
    entURL_id = "txturl"
    # ######## NewContactSave button ##############
    clkonsavebtn_xpath = '/html/body/div[1]/div/div/div[1]/div[2]/button[1]'

    # ############## Edit Contact ##########
    clkonEditBtn_xpath = '/html/body/div[1]/div/div/div[1]/div[2]/button[1]'
    clkonEditBTN_xpath = "//a[@data-ng-click='$ctrl.editContact(contact.ContactID)']"

    clkOnSaveChangesBtn_xpath = '/html/body/div[1]/div/div/div[1]/div[2]/button[1]'
    clkonClosebtn_xpath = '/html/body/div[1]/div/div/div[1]/div[2]/button[2]'

    # ########### Search Contact ##############
    clkonSearchField_id = 'txtSearchText'
    all_ContactNames_xpath = "//span[@data-ng-if='contact.FirstName || contact.LastName || contact.IsPerson']"
    clkonContactClosebtn_xpath = '/html/body/div[1]/div/div/div[1]/div[2]/button[2]'

    # ##### Clone the Contact ##########
    clkonCloneBtn_xpath = "//div[@class='pull-right']/a[text()='Clone']"
    clkonClonesaveBtn_xpath = '/html/body/div[1]/div/div/div[1]/div[2]/button[1]'

    # ####### Delete the contact ########
    clkonDeleteBtn_xpath = "//div[@class='pull-right']/a[text()='Delete']"
    clkonDelYesBtn_xpath = "//button[@class='confirm']"
    clkonDelNoBtn_xpath = "//button[@class='cancel']"

    # ####### Check Hide Contact ##############
    ckeckonHideContacts_xpath = "//div[@class='ptb-4-5 form-group']/label"

    # ######## Manage tags #############
    clkonManageTags_xpath = "//div[@class='form-group']/ul/li/a[text()='Manage Tags']"
    clkonCreateNewTag_x = "//button[@class='btn btn-primary btn-xs']"
    # entTag_xpath = "//input[@id='tagName']"
    entTag_xpath = '//a[@data-ng-click="$ctrl.addTag()"]'
    clkonTagSavebtn_xpath = "//div[@class='modal-header-right']/button[text()='Save']"
    clkonTagClosebtn_xpath = "/html/body/div[1]/div/div/create-new-tag/div[1]/div[2]/button[2]"

    # ######### Delete Tags in Manage tags ##########
    clkonDelTagYes_xpath = "//button[@class='confirm']"
    clkonDelTagNo_xpath = "//button[@class='cancel']"

    # ########### SelectAll ###########
    clkonSelectAllBtn_xpath = '//li/a[@data-ng-click="$ctrl.selectAllContacts()"]'

    # ########### DeselectAll ###########
    clkonDeselectAllBtn_xpath = "//ul[@class='list-inline mb0 pull-left ptb-5-5']/li/a[text()='Deselect All']"

    # ######### Delete ##########
    clkonContacts_DeleteBtn_xpath = "//ul[@class='list-inline mb0 pull-left ptb-5-5']/li/a[text()='Delete']"

    clkonDeleteSendVCF_xpath = "//button[text()='Delete & Send VCF']"
    clkonDeleteOk_xpath = "//button[text()='Delete']"

    # ######## Tag ##########
    # clkonTagBtn_xpath = "//ul[@class='list-inline mb0 pull-left ptb-5-5']/li/a[text()='Tag']"
    clkonTagBtn_xpath = '//a[@data-ng-click="$ctrl.addTag()"]'

    # ###### Select tag in drp #####
    clkonTagsdrp_xpath = "//ul[@class='list-inline mb0 pull-right']/li/div[@class='groups-multiselect-contacts fixed-width']"
    alldrptags_xpath = "//ul[@class='dropdown-menu dropdown-menu-form']/li/a/span/span"
    clkonAddNewTagBtn_xpath = "//button[@data-ng-click='addNewGroup()']"
    ent_tagName_xpath = '//*[@id="tagName"]'
    clkonSaveTagBtn_xpath = "//div[@class='pull-right']/button[text()='Save Tag']"
    clkonCancelTagBtn_xpath = "//div[@class='pull-right']/button[@data-ng-click='closeForm()']"
    selExistingTag_xpath = "//div[@data-ng-repeat='group in tagsList']/div/label/span[text()]"
    Uncheck_Keeptags = "//div[@class='col-md-12 mb-20']/label/span"
    selTagSavebtn_xpath = "//button[@data-ng-click='linkTagsToContacts()']/i"
    selTagClosebtn_xpath = "//button[@data-ng-click='closeTagsListModal()']"

    # ######## Mail ###########
    clkonMailBtn_xpath = "//ul[@class='list-inline mb0 pull-left ptb-5-5']/li/a[text()='Mail']"
