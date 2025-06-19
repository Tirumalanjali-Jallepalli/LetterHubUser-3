class Loc_Invoices:

    ClkOnInvoicesModule_text = 'Invoices'
    SearchInvoice_id = 'txtSearchInvoices'
    allInvoiceNames_xpath = '//div[@class="table-responsive"]//td/a'
    ClkOnConnectedAccountList_xpath = '/html/body//div[2]/div//span[2]/span'
    ClkOnConnectedAccountsDate_xpath = '/html/body//div[3]/div//span[2]/span'
    ClkOnConnectedAccountStatus_xpath = '/html/body//div[4]/div//span[2]/span'
    ClkOnInvoiceDetailsCloseBtn_xpath = '/html/body/div[1]/div/div/div[1]/button/span'
    CheckInvoices_xpath = '//td/a[contains(text(), "1000")]//preceding::td//label[@ng-click="selectInvoice(invoice)"]'
    # ***** Mail Selected Invoices *****
    ClkOnMailSelectedInvoices_xpath = '//button[@ng-click="mailSelectedInvocies()"]'
    ClkOnAddressReviewContinueBtn_xpath = '//button[@ng-click="$ctrl.continue()"]'
    ClkOnAddressReviewCloseBtn_xpath = '//button[@ng-click="$ctrl.cancel()"]'




