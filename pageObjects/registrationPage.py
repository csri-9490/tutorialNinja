from datetime import datetime

from selenium.webdriver.common.by import By

from pageObjects.accountSuccessPage import AccountSuccessPage
import time

class regPage:
    def __init__(self,driver):
        self.driver=driver

    yes_radio_button_xpath="(//input[@type='radio'][@value='1'])[2]"
    def enter_fname_text(self,fname):
        self.driver.find_element(By.ID,"input-firstname").send_keys(fname)
    def enter_lname_text(self,lname):
        self.driver.find_element(By.ID,"input-lastname").send_keys(lname)
    def enter_email(self,email):
        self.driver.find_element(By.ID,"input-email").send_keys(email)
        # time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        # return  "csri"+time_stamp+"@gmail.com"
    def enter_phno(self,telephone):
        self.driver.find_element(By.ID,"input-telephone").send_keys(telephone)
    def enter_password(self,password):
        self.driver.find_element(By.ID,"input-password").send_keys(password)
    def confirm_password(self,confirm_pwd):
        self.driver.find_element(By.ID,"input-confirm").send_keys(confirm_pwd)
    def confirm_privacypolicy(self):
        self.driver.find_element(By.XPATH,"//input[@name='agree']").click()
    def confirm_button(self):
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        return AccountSuccessPage(self.driver)
    def select_yes_radio_button(self):
        self.driver.find_element(By.XPATH,self.yes_radio_button_xpath).click()

    def register_an_account(self,fname,lname,email,phne,pwd,cnfrm,yes_or_no,privacy_selct):
        self.enter_fname_text(fname)
        self.enter_lname_text(lname)
        self.enter_email(email)
        self.enter_phno(phne)
        self.enter_password(pwd)
        time.sleep(5)
        self.confirm_password(cnfrm)
        time.sleep(5)
        if yes_or_no.__eq__("yes"):
            self.select_yes_radio_button()
        time.sleep(5)
        if privacy_selct.__eq__("select"):
            self.confirm_privacypolicy()
        time.sleep(5)
        return self.confirm_button()

    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "csri" + time_stamp + "@gmail.com"

