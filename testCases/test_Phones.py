import time

from selenium.webdriver.common.by import By

from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from utilities import readConfigurations
from utilities.baseclass import BaseClass


class Teste2ePhones(BaseClass):
    url = readConfigurations.read_configuration('basic info', 'url')
    login_link_text = "Login"
    eml=readConfigurations.read_configuration('basic info','email')
    pwd=readConfigurations.read_configuration('basic info','pswrd')
    def test_ogin(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
        self.verifyLinkPresence('My Account')
        hmpg = HomePage(self.driver)
        hmpg.click_myaccount_button()
        self.driver.find_element(By.LINK_TEXT, self.login_link_text).click()
        lgpg = LoginPage(self.driver)
        lgpg.enter_email_address(self.eml)
        lgpg.enter_password(self.pwd)
        lgpg.click_on_login()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//*[contains(text(),'Phones & PDAs')]").click()
        ph_names=self.driver.find_elements(By.XPATH,"//div[@class='row']/div[@class='product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12']/div[1]/div[2]/div[1]/h4")
        for i in ph_names:
            print('phone names',i.text)
        ph_prices=self.driver.find_elements(By.XPATH,"//div[@class='row']/div[@class='product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12']/div[1]/div[2]/div[1]/p[2][@class='price']")
        for prices in ph_prices:
            print('phone prices',prices.text)
        # time.sleep(5)
        ph_add2cart=self.driver.find_elements(By.XPATH,"//div[@class='row']/div[@class='product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12']/div[1]/div[2]/div[2]/button[1]")
        for crt in ph_add2cart:
            crt.click()
        time.sleep(6)
        self.driver.find_element(By.XPATH,"//span[@id='cart-total']").click()
        Total=self.driver.find_element(By.XPATH,"//table[@class='table table-bordered']//tr[4]//td[2][@class='text-right']")
        Total_value=Total.text
        print('Total',Total_value)
        self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu pull-right']//li[2]//div[1]//p//a[2]").click()
        self.driver.find_element(By.XPATH,"//a[@class='btn btn-primary']").click()
        cart_wait=self.driver.find_element(By.CSS_SELECTOR,"#content h1").text
        print(cart_wait)








