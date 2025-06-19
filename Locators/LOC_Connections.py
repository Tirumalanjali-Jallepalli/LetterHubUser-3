class Loc_Connections:

    ClkOnConnectionsModule_text = 'Connections'

    # ######### Import VCF ############
    ClkOnImportVCF_text = "Import VCF"
    ClkOnBrowseBtn_xpath = '//label[@class="btn btn-primary"]'

    # ######### Import CSV ############
    ClkOnAllUSYesBtn_id = 'lblAllUSYes'
    ClkOnAllUSNoBtn_id = 'lblAllUSNo'
    ClkOnFirstColNamesCheckBox_xpath = '//label[@data-ng-click="FirstRowColumns()"]'
    ClkOnMapCol_cls = '/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td[5]/div/span/span/span[2]/span'
    MapColTextBox_cls = 'k-textbox'

    ClkOnImportCSV_text = "Import CSV"
    ClkOnImportCSV_Save_xpath = '//button[@data-ng-click="importCSVClick()"]'
    ClkOnImportCSV_Cancel_xpath = '//button[@data-ng-click="cancelClicked()"]'

    # ######### Import VCF ############
    ClkOnImportExcel_text = "Import Excel"

    # #### Select Tag #####
    ClkOnAddNewTag_text = 'Add New Tag'
    ClkOnSelTags_xpath = '//div[@class="k-multiselect-wrap k-floatwrap"]'
    AllExistingTags_xpath = '//ul[@id="selectedTagIds_listbox"]/li'

    ClkOnSaveTagBtn_xpath = '//button[@data-ng-click="addTags()"]'
    ClkOnSkipTagBtn_xpath = '//button[@ng-click="dontAddTags()"]'


