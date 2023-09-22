import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

@pytest.mark.usefixtures("setup")
class BaseClass:
   # def __init__(self,driver):
   #     self.driver=driver
   @staticmethod
   def sleep_time(tm):
        time.sleep(tm)


   def verifyLinkPresence(self,text):
       ele=WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text)))

