from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import time


class ProdPage:
    def __init__(self,driver):
        self.driver=driver

    button_product_xpath="//div[@class='caption']/h4/a"
    price_xpath="//ul[@class='list-unstyled']/li/h2"
    qty_id="input-quantity"
    add2cart="button-cart"
    msg1="//div[@class='alert alert-success alert-dismissible']"
    clickOnCart_xpath="//div[@class='alert alert-success alert-dismissible']/a[2]"

    def click_on_product(self):

        self.driver.find_element(By.XPATH,self.button_product_xpath).click()
        prod_text =self.driver.find_element(By.XPATH,"//div[@class='col-sm-4']/h1").text
        self.driver.find_element(By.XPATH,"//div[@class='col-sm-4']/h1")
        self.driver.implicitly_wait(5)
        # self.driver.find_element(By.XPATH,self.price_xpath).below(self.driver.find_element(By.XPATH,"//div[@class='col-sm-4']/h1"))
        time.sleep(5)
        locate_with(By.XPATH,self.price_xpath).below({By.XPATH:"//div[@class='col-sm-4']/h1"})
        self.driver.find_element(By.ID,self.qty_id).send_keys(6)
        self.driver.find_element(By.ID,self.add2cart).click()
        message_after_adding2cart=self.driver.find_element(By.XPATH,self.msg1).text
        self.driver.find_element(By.XPATH,self.clickOnCart_xpath).click()




