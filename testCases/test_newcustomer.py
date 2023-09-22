from datetime import datetime

from selenium.webdriver.common.by import By

from pageObjects.homePage import HomePage
from pageObjects.registrationPage import regPage
from utilities import readConfigurations
from utilities.baseclass import BaseClass
import pytest

class TestNewCustomer(BaseClass):
    url=readConfigurations.read_configuration('basic info','url')

    # @pytest.mark.smoke
    def test_newcust_creation(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        # BaseClass.sleep_time(10)
        self.verifyLinkPresence('My Account')
        hmpage=HomePage(self.driver)
        # hmpage.click_myaccount_button()
        # self.driver.find_element(By.LINK_TEXT,"Register").click()
        # rgpage=hmpage.select_register_option()
        rgpage = hmpage.navigate_to_register_page()
        BaseClass.sleep_time(5)
        AccSuccessPage=rgpage.register_an_account("csr47","csr57",self.generate_email_with_timestamp(),3242424,"Shivaaya2@","Shivaaya2@","yes","select")
        # rgpage = regPage(self.driver) ###
        # rgpage.enter_fname_text('jason1')
        # rgpage.enter_lname_text('jason2')
        # rgpage.enter_email('csri_reddy@yahoo.com')
        # rgpage.enter_phno('435345')
        # rgpage.enter_password('Shivaya1@')
        # rgpage.confirm_password('Shivaya1@')
        # rgpage.confirm_privacypolicy()
        # AccSuccessPage=rgpage.confirm_button()
        BaseClass.sleep_time(5)
        expected_success_page="Your Account Has Been Created!"
        AccSuccessPage.retrieve_account_creation_message().__eq__(expected_success_page)


    def test_register_with_duplicate_email(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        # BaseClass.sleep_time(10)
        self.verifyLinkPresence('My Account')
        hmpage = HomePage(self.driver)
        hmpage.click_myaccount_button()
        rgpage=hmpage.select_register_option()
        BaseClass.sleep_time(5)
        # rgpage = regPage(self.driver)
        rgpage.enter_fname_text('jason1')
        rgpage.enter_lname_text('jason2')
        rgpage.enter_email('csri_reddy@yahoo.com')
        rgpage.enter_phno(323243)
        rgpage.enter_password('Shivaya1@')
        rgpage.confirm_password('Shivaya1@')
        rgpage.confirm_privacypolicy()
        rgpage.confirm_button()
        BaseClass.sleep_time(5)
        expected_text='Warning: E-Mail Address is already registered!'
        assert self.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text.__eq__(expected_text)

    def test_without_entering_any_field(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        # BaseClass.sleep_time(10)
        self.verifyLinkPresence('My Account')
        hmpage = HomePage(self.driver)
        hmpage.click_myaccount_button()
        rgpage=hmpage.select_register_option()
        BaseClass.sleep_time(5)
        # rgpage = regPage(self.driver)
        rgpage.enter_fname_text('')
        rgpage.enter_lname_text('')
        rgpage.enter_email('')
        rgpage.enter_phno('')
        rgpage.enter_password('')
        rgpage.confirm_password('')
        rgpage.confirm_privacypolicy()
        rgpage.confirm_button()
        BaseClass.sleep_time(5)
        expected_text = 'First Name must be between 1 and 32 characters!'
        assert self.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div").text.__eq__(
            expected_text)

    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "csri" + time_stamp + "@gmail.com"




