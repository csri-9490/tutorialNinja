from selenium.webdriver.common.by import By


class AccountPage:
    def __init__(self,driver):
        self.driver=driver

    link_account_info_xpath="(// div[@ id='content'] /ul/li/a)[1]"
    product_type="//*[text()='Tablets']"

    def click_on_edit_your_account_info(self):
        self.driver.find_element(By.XPATH,self.link_account_info_xpath).click()

    def click_on_product_type(self):
        self.driver.find_element(By.XPATH,self.product_type).click()



