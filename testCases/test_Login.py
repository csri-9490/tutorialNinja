from utilities.baseclass import BaseClass


class TestNames(BaseClass):
    # def __init__(self, driver):
    #     self.driver=driver
    def test_logins(self,setup):
        self.driver=setup
        self.driver.get("https://tutorialsninja.com/demo/")
        BaseClass.sleep_time(5)


