import time

from selenium import  webdriver
from selenium.webdriver.common.by import By


def test_whatsp():

   options=webdriver.ChromeOptions()
   # options.add_argument("C:\\Users\\Srikanth Chelukala\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
   options.add_argument("headless")
   driver=webdriver.Chrome(options=options)
   # driver.get("https://web.whatsapp.com/")
   # driver = webdriver.Chrome()
   driver.get("https://www.facebook.com/")
   driver.maximize_window()
   driver.implicitly_wait(30)
   driver.find_element(By.XPATH,"//input[@id='email']").send_keys("reddy.csri@gmail.com")
   driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("shivayA@1")
   driver.find_element(By.XPATH,"//button[@name='login']").click()
   time.sleep(5)
   msg=driver.find_element(By.XPATH,"//div[@class='x1iyjqo2']/ul[1]/li[1]/div[1]/a/div[1]/div[2]//div[1]/div[1]/div[1]/div[1]/span[1]/span").text
   print(msg)
   driver.get_screenshot_as_file("sname1.png")


