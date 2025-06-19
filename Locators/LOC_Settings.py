class Settings:

    # #################### MY ACCOUNT ####################

    Clkonsettingsbtn_xpath = "/html/body/div[2]/div[1]/nav/ul/li[11]/a/span"
    Clkonmyaccount_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/" \
                           "settings-details/div[1]/div[1]/div/a/div/div[2]/h4"
    Entname_id = "UserName"
    Entcomp_id = "CompanyName"
    Clkonsave_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/my-account/div[1]/div/form/div[4]/button"

    # ################ DEFAULT RETURN ADDRESS #######################

    ClkonDefaultadd_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/" \
                            "settings-details/div[1]/div[2]/div/a/div/div[2]/h4"
    Entfname_id = "FirstName"
    Entcpmname_id = "Company"
    Entaddname1_id = "Address1"
    Entaddnam2_id = "Address2"
    Entcity_id = "City"
    Entstate_id = "State"
    Entzip_id = "ZipCode"
    Clkonsave2_xpath = '//button[@ng-click="$ctrl.saveReturnAddress()"]' #"/html/body/div[2]/div[2]/div[2]/div[2]/div/return-address/div/div/form/div[8]/button"

    # ######################  JOB PRINT PREFERENCES ########################

    CLkonjobprefe_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/" \
                          "div/settings-details/div[1]/div[3]/div/a/div/div[2]/h4"
    Clkonblkadwhit_xpath = "//div[@class='lh-card-body pb-42 lh-card-body" \
                           "-vertical-height']/label[@class='cb-radio checked']"
    Clkonclor_xpath = "//div[@class='lh-card-body pb-42 lh-card-body-vertical-height']/label[@class='cb-radio']"
    Clkonprntboth_xpath = "//div[@class='lh-card-body pb-42 lh-card-body" \
                          "-vertical-height']/label[@class='cb-checkbox p-3 checked']"

    Clkonnone_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/job-print" \
                      "-preferences/div[1]/div[2]/div/div[2]/label[1]/span"
    CLkonwithoutpostage_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/" \
                                "div/job-print-preferences/div[1]/div[2]/div/div[2]/label[2]/span[1]"
    Clkonwithpostage_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/" \
                             "div/job-print-preferences/div[1]/div[2]/div/div[2]/label[3]/span[1]"
    Clkonfriendlyreturnenvolope_xpath = "/html/body/div[2]/div[2]/" \
                                        "div[2]/div[2]/div/job-print-preferences/div[1]" \
                                        "/div[2]/div/div[2]/label[4]/span[1]"
    Clkonchanofadd_yes_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/" \
                               "div/job-print-preferences/div[2]/div/div/div[2]/change-of-address/div/label[1]/span[1]"
    Clkonchanofadd_no_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/" \
                              "div/job-print-preferences/div[2]/div/div/div[2]/change-of-address/div/label[2]/span[1]"
    Clkon_yes_chanofadd_xpath ="/html/body/div[2]/div[2]/div[2]/div[2]/" \
                               "div/job-print-preferences/div[2]/div/div/div[2]/change-of-address/div/label[3]/span[1]"
    Clkon_no_changofadd = "/html/body/div[2]/div[2]/div[2]/div[2]/div/" \
                          "job-print-preferences/div[2]/div/div/div[2]/change-of-address/div/label[4]/span[1]"
    ClkonCheckbox_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/" \
                          "job-print-preferences/div[2]/div/div/div[2]/change-of-address/div/label[5]/span[1]/i"

    # ####################### PAYMENT OPTIONS ###############################

    Clkon_paymentoption_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]" \
                                "/div/settings-details/div[1]/div[4]/div/a/div/div[2]/h4"
    Clkoncheckbox_pay_auto_xpath = "/html/body/div[2]/div[2]/div[2]/" \
                                   "div[2]/div/payment-options/div[2]/div/label/span[1]/i"
    Clkon_dropdown_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/" \
                           "div/payment-options/div[2]/div/span[1]/span/span[2]/span"
    Selectfron_dropdown_xpath = "//div[@class='k-list-scroller']//ul[@id='AutoPayPlanID_listbox']/li"
    CLkondropdown2_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]" \
                           "/div/payment-options/div[2]/div/span[2]/span/span[2]/span"
    Selectfrom_dropdown2_xpath = "//div[@class='k-list-scroller']/ul/li"
    CLkoncheckbox_notify_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/payment-options/div[3]/div/label/span/i"
    Clkondropdown3_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/" \
                           "div/payment-options/div[3]/div/span/span/span[2]/span"
    Slect_dropdown3_xpath = "//div[@class='k-list-scroller']/ul/li"
    Clkon_Save_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/payment-options/div[1]/div[2]/button"

    Clkonaddnewcredi_xpath = "//div[@class='icon-add-credit-card-64']"
    Ent_cardnum_id = "CreditCardNumber"
    Ent_fstnam_id = "CreditCardHolderFirstName"
    Ent_lstnam_id = "CreditCardHolderLastName"
    Ent_expdte_id = "CreditCardExpiryDate"
    Enta_secty_id = "CreditCardSecurityCode"
    CLk_sav_xpath = "/html/body/div[1]/div/div/add-credit-card-modal/div[1]/div[2]/button[1]"
    Clkon_cls_xpath = "/html/body/div[1]/div/div/add-credit-card-modal/div[1]/div[2]/button[2]"

    ClkOnAllExistingCards_xpath = '//h4[@class="mt0"]'
    CLkondefaultbtn = "//a[@class='hylink text-information  mr10']"
    Clkondlt = ".//following-sibling::p/a[contains(text(), 'delete')]"
    # Clkondlt = "//h4[contains(@class,'mt0')]/following-sibling::p/a[contains(text(), 'delete')]" #'//a[@ng-click="$ctrl.deleteCreditCard(creditCard.CreditCardID,$index)"]'

    #  ###################### EMAIL TO PRINT ############################

    CLkon_Emladpri_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/" \
                           "div/settings-details/div[1]/div[5]/div/a/div/div[2]/h4"
    Clkontoggle_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/email-to-print/div[1]/div[1]/label/span/i"
    Ent_emailnam_name = "email"
    CLk_ademai_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/" \
                       "email-to-print/div[2]/div/form/div/div[1]/span/button"
    Clkondelt_btn_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/" \
                          "div/email-to-print/div[2]/div/div[3]/div[2]/ul/li[2]/a/i"
    Clkonyesbtn_xpath = "/html/body/div[4]/button[2]"
    Clkmor_infoabtEmail_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/email-to-print/div[1]/div[2]/div[2]/a"

    # ################## API SETTINGS ##################################

    ClkonApi_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/settings-details/div[1]/div[6]/div/a/div/div[2]/h4"
    Clkon_createAp_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/api-settings/div[1]/div[2]/button"
    Entapikeyname_id = "UserAPIKeyTagName"
    Clkn_dropdown_xpath = "/html/body/div[1]/div/div/add-api-key-modal/" \
                          "div[2]/div/div/form/div[2]/div/span/span/span[2]/span"
    Slectfrom_dropdow_xpath = "//ul[@class='k-list k-reset']/li"
    Ent_applinam_id = "ApplicationName"
    Clk_SAV_xpath = "/html/body/div[1]/div/div/add-api-key-modal/div[1]/div[2]/button[1]"
    CLk_Cls = "/html/body/div[1]/div/div/add-api-key-modal/div[1]/div[2]/button[2]"

    Clk_enable_xpath = "//button[@class='btn btn-default btn-outline btn-sm']"
    Clkon_edit_xpath = "//i[@class='glyphicon glyphicon-edit mr5']"
    Clkon_disabl_xpath = "//button[@class='btn btn-default btn-sm']"
    Clkmore_abt_api_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/api-settings/div[2]/div[2]/a[1]"
    CLkonMor_abtsandbox_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/api-settings/div[2]/div[2]/a[2]"
    entupdate_api_id = "UserAPIKeyTagName"
    updtsav_xpath = "/html/body/div[1]/div/div/update-api-key-modal/div[1]/div[2]/button[1]"

    Ent_promo_id = "promoCode"
    CLkon_redem_btn_xpath = "/html/body/div[2]/div[2]/div[2]/div[2]/div/settings-details/div[2]/div/form/div/div/span"










