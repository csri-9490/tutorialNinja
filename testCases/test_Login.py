from datetime import datetime

import pytest
from selenium.webdriver.chromium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from utilities import readConfigurations, excelUtils
from utilities.baseclass import BaseClass
from utilities.excelUtils import exceldata
from utilities.testdata import test_data


class TestNames(BaseClass):
     url = readConfigurations.read_configuration('basic info', 'url')
     # ch_op=webdriver.ChromeOptions()
     # ch_op.add_argument("headless")
     # @pytest.mark.parametrize("email,pwd",excelUtils.get_data_from_excel(path,"testdatas"))
     @pytest.mark.parametrize("email,pwd",(['reddy.csri@gmail.com','Shivaya1@'],['reddy.csri1@gmail.com','Shivaya2@']))
     def test_logins(self,email,pwd):
        # self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.verifyLinkPresence('My Account')
        hmpage = HomePage(self.driver)
        # hmpage.click_myaccount_button() ###****###
        # hmpage.select_login_option()
        # lpage=LoginPage(self.driver)
        # lpage=hmpage.select_login_option() ###****###
        lpage=hmpage.select_login_button_drirectly()
        # lpage.enter_email_address('reddy.csri@gmail.com')
        # lpage.enter_password("Shivaya1@")
        # accpage=lpage.click_on_login()
        accpage=lpage.login_to_application(email,pwd)
        # accpage=AccountPage(self.driver) #added4 below
        accpage.click_on_edit_your_account_info()
        BaseClass.sleep_time(5)
        hmpage.click_myaccount_button()
        lpage.click_on_logout()
        BaseClass.sleep_time(5)

     def test_wrongpwd_logins(self):
        # self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        # BaseClass.sleep_time(10)
        self.verifyLinkPresence('My Account')
        hmpage = HomePage(self.driver)
        hmpage.click_myaccount_button()
        # hmpage.select_login_option()
        # lpage = LoginPage(self.driver)
        lpage=hmpage.select_login_option()
        lpage.enter_email_address('reddy.csri@gmail.com')
        lpage.enter_password("Ahivaya1@")
        lpage.click_on_login()
        expected='Warning: No match for E-Mail Address and/or Password.'
        BaseClass.sleep_time(5)
        actual=lpage.get_warning_loginfail_message()
        print('actual text name is ',actual)
        BaseClass.sleep_time(5)
        assert actual==expected
        BaseClass.sleep_time(5)

     def test_wrongemail_logins(self):
        # self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        # BaseClass.sleep_time(10)
        self.verifyLinkPresence('My Account')
        hmpage = HomePage(self.driver)
        hmpage.click_myaccount_button()
        # hmpage.select_login_option()
        lpage=hmpage.select_login_option()
        # lpage = LoginPage(self.driver) #added4 below
        lpage.enter_email_address(self.generate_email_with_timestamp())
        lpage.enter_password("Shivaya1@")
        lpage.click_on_login()
        BaseClass.sleep_time(5)
        expected = 'Warning: No match for E-Mail Address and/or Password.'
        actual=lpage.get_warning_loginfail_message()
        BaseClass.sleep_time(5)
        assert actual == expected

     def generate_email_with_timestamp(self):
        time_stamp=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "csri"+time_stamp+"@gmail.com"






