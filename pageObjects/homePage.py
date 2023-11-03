from selenium.webdriver.common.by import By

from pageObjects.loginPage import LoginPage
from pageObjects.registrationPage import regPage
from pageObjects.searchPage import SearchPage


class HomePage:
    def __init__(self,driver):
        self.driver=driver

    search_box_field_name="search"
    button_myaccount_xpath="//li[@class='dropdown']/a/span[1]"
    search_button_xpath="//span[@class='input-group-btn']/button"
    login_link_text="Login"
    register_linktext="Register"

    def click_myaccount_button(self):
        self.driver.find_element(By.XPATH, self.button_myaccount_xpath).click()


    def select_register_option(self):
        self.driver.find_element(By.LINK_TEXT, self.register_linktext).click()
        return regPage(self.driver)

    def enter_product_into_search_box_field(self,prod_name):
        self.driver.find_element(By.NAME,self.search_box_field_name).click()
        self.driver.find_element(By.NAME,self.search_box_field_name).clear()
        self.driver.find_element(By.NAME,self.search_box_field_name).send_keys(prod_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver) #added1

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_link_text).click()
        return  LoginPage(self.driver)

    def select_login_button_drirectly(self):
        self.click_myaccount_button()
        return self.select_login_option()

    def navigate_to_register_page(self):
        self.click_myaccount_button()
        return self.select_register_option()

