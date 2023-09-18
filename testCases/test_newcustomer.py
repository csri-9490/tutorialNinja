from selenium.webdriver.common.by import By

from utilities.baseclass import BaseClass


class TestNewCustomer(BaseClass):
    def test_newcust(self,setup):
        self.driver=setup
        self.driver.get("https://tutorialsninja.com/demo/")
        self.driver.maximize_window()
        # BaseClass.sleep_time(10)
        self.verifyLinkPresence('My Account')
        self.driver.find_element(By.XPATH,"//li[@class='dropdown']/a/span[1]").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        BaseClass.sleep_time(5)
        # self.driver.find_element(By.)



