from selenium.webdriver.common.by import By

from pageObjects.homePage import HomePage
from pageObjects.searchPage import SearchPage
from utilities import readConfigurations
from utilities.baseclass import BaseClass


class TestSearchValues(BaseClass):
    url = readConfigurations.read_configuration('basic info', 'url')
    def test_search_for_a_valid_product(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        hmpage=HomePage(self.driver)
        hmpage.enter_product_into_search_box_field("HP")
        # hmpage.click_on_search_button()
        # spage=SearchPage(self.driver) #added2 below
        spage=hmpage.click_on_search_button()
        BaseClass.sleep_time(5)
        spage.display_status_of_product()

    def test_search_for_an_invalid_product(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        hmpage = HomePage(self.driver)
        hmpage.enter_product_into_search_box_field("honda")
        # hmpage.click_on_search_button()
        # spage = SearchPage(self.driver) #added2 below
        spage=hmpage.click_on_search_button()
        expected='There is no product that matches the search criteria.'
        BaseClass.sleep_time(5)
        assert  spage.display_no_product()==expected

    def test_search_for_an_no_product_entry(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        hmpage = HomePage(self.driver)
        hmpage.enter_product_into_search_box_field("")
        # hmpage.click_on_search_button()
        # spage = SearchPage(self.driver) #added3 below
        spage=hmpage.click_on_search_button()
        expected = 'There is no product that matches the search criteria.'
        BaseClass.sleep_time(5)
        assert spage.display_no_product() == expected





