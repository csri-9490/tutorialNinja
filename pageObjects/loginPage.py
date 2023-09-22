from selenium.webdriver.common.by import By

from pageObjects.accountPage import AccountPage


class LoginPage:
    def __init__(self,driver):
        self.driver=driver
    text_emailid_id="input-email"
    text_pwd_id="input-password"
    login_xpath="//input[@value='Login']"
    logout_button="Logout"
    warning_message="//div[@id='account-login']/div[1]"

    def enter_email_address(self,email):
        self.driver.find_element(By.ID, self.text_emailid_id).send_keys(email)
    def enter_password(self,pwd):
        self.driver.find_element(By.ID, self.text_pwd_id).send_keys(pwd)

    def click_on_login(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()
        return AccountPage(self.driver)

    def click_on_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_button).click()


    def  get_warning_loginfail_message(self):
         return self.driver.find_element(By.XPATH, self.warning_message).text

    def login_to_application(self,email,pwd):
        self.enter_email_address(email)
        self.enter_password(pwd)
        return  self.click_on_login()







