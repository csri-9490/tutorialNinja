import time
from selenium.webdriver.common.by import By

from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.prodPage import ProdPage
from utilities import readConfigurations
from utilities.baseclass import BaseClass
from utilities.readConfigurations import read_configuration



class Teste2e_Tablets(BaseClass):
   url = readConfigurations.read_configuration('basic info', 'url')
   login_link_text = "Login"
   button_product_xpath = "//div[@class='caption']/h4/a"
   price_xpath = "//ul[@class='list-unstyled']/li/h2"
   qty_id = "input-quantity"
   add2cart = "button-cart"
   msg1 = "//div[@class='alert alert-success alert-dismissible']"
   clickOnCart_xpath = "//div[@class='alert alert-success alert-dismissible']/a[2]"

   def test_login(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.verifyLinkPresence('My Account')
       hmpg=HomePage(self.driver)
       hmpg.click_myaccount_button()
       self.driver.find_element(By.LINK_TEXT, self.login_link_text).click()
       lgpg=LoginPage(self.driver)
       lgpg.enter_email_address('reddy.csri@gmail.com')
       lgpg.enter_password('Shivaya1@')
       lgpg.click_on_login()
       time.sleep(2)
       self.driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav']/li[4]").click()
       ppg=ProdPage(self.driver)
       ppg.click_on_product()









   def checkout(self):
       pass


