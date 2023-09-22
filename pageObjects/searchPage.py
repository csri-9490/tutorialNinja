from selenium.webdriver.common.by import By
class SearchPage:
    def __init__(self,driver):
        self.driver=driver
    valid_hp_product_link_text="HP LP3065"
    no_product="//p[contains(text(),'There is no product that matches the search criter')]"


    def display_status_of_product(self):
        return  self.driver.find_element(By.LINK_TEXT,self.valid_hp_product_link_text).is_displayed()

    def display_no_product(self):
        return  self.driver.find_element(By.XPATH,self.no_product).text






