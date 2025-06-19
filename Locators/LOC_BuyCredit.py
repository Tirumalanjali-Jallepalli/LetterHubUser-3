class Loc_BuyCredit:

    # ######### Buy Credits through credit cards ###########

    ClkOnBuyCreditsModule_xpath = '/html/body/div[2]/div[1]/nav/ul/li[6]/a'
    ClkOn_drp_CreditAmount_xpath = '//span[@class="k-select"]'
    select_creditamount_xpath = '//div[@class="k-list-scroller"]/ul/li'
    clkon_buycredits_xpah = '/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/button'

    # ###### Use Another Card ########

    clk_anotherCard_xpath = '/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/form/div[3]/div/div/div[1]/label/span'
    entFname_id = 'txtFirstName'
    entLname_id = 'txtLastName'
    entCardNo_id = 'txtCardNumber'
    entExpireDate = 'txtExpDate'
    entSecurityCode = 'txtSecurityCode'
    check_SaveCard_xpath = '//label[@data-ng-click="saveCard()"]'

    # ######### Usage Summary Details ###############

    ClkOnUsageSummary_text = 'Usage Summary'
    clk_date_drp_xpath = '//span[@class="k-select"]'
    select_date_drp_xpath = "//div[@class='k-list-scroller']/ul/li"
    # ###### Date in Custom Range #####
    clkCustomRange_xpath = '//*[@id="ddlFilterDateSource_listbox"]/li[2]'
    entFromDate_id = 'fromdate'
    entToDate_id = 'todate'
    clkOnOk_xpath = '/html/body/div[1]/div/div/date-range-picker-modal/div[1]/div[2]/button[1]'

    # ############# Usage Summary Download By Date ####################
    ClkOnDownloadUsageSummaryByDate_xpath = '/html/body/div[2]/div[2]/div[2]/div[2]/div/billings-component/div[1]/div[3]/div/a'

    # ############# Usage Summary View & Download ####################
    uncheck_GroupByDate_xpath = '/html/body/div[2]/div[2]/div[2]/div[2]/div/billings-component/div[1]/div[2]/div/label/span[1]/i'
    ClkOnCloseUsageSummaryView_xpath = '/html/body/div[1]/div/div/div[1]/button/span'
    clkOnDownloadSymbol_xpath = '//*[@id="download"]'
