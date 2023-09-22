import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


class CartPage:
    def __init__(self,driver):
        self.driver=driver
    cart_product_xpath="(//td[@class='text-left']/a)[2]"
    qty_xpath="//input[@name='quantity[59299]']"
    total_xpath="//tbody//tr//td[6]"

    def cart_details(self):
        prod_name=self.driver.find_element(By.XPATH,self.cart_product_xpath).text
        qty=locate_with(By.XPATH,self.qty_xpath).to_right_of({By.XPATH:self.cart_product_xpath})
        time.sleep(5)
        total_value=locate_with(By.XPATH,self.total_xpath).to_right_of({By.XPATH:self.cart_product_xpath})
        total_value1=self.driver.find_element(By.XPATH,self.total_xpath).text
        print('prd names',prod_name)
        print('qtynumber',qty)
        print('total value',total_value1)
        time.sleep(5)



