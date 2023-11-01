from pageObjects.cartPage import CartPage
from pageObjects.homePage import HomePage
from pageObjects.prodPage import ProdPage
from utilities import readConfigurations
from utilities.baseclass import BaseClass


class TestLoginCheckout(BaseClass):
    url = readConfigurations.read_configuration('basic info', 'url')

    def test_login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.verifyLinkPresence('My Account')
        hmpage = HomePage(self.driver)
        lpage = hmpage.select_login_button_drirectly()
        accpage = lpage.login_to_application('reddy.csri@gmail.com', 'Shivaya1@')
        accpage.clear_cart_item()
        accpage.click_on_product_type()
        ppage=ProdPage(self.driver)
        ppage.click_on_product()
        cpage=CartPage(self.driver)
        cpage.cart_details()






