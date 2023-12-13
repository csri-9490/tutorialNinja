from seleniumbase import BaseCase

class HomeTest(BaseCase):
    def test_home_page(self):
        self.open("https://www.spicejet.com/")
        self.click("//div[@data-testid='to-testID-destination']/div/div[2]")
