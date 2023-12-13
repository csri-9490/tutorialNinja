from selenium import  webdriver
from selenium.webdriver.common.by import By
import base64
import  time

encodedBytes = base64.b64encode("Shivaya1@".encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print("Encoded String : "+encodedStr)
decodedBytes = base64.b64decode(encodedStr)
decodedStr = str(decodedBytes, "utf-8")
print("Decoded String : "+decodedStr)
driver=webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
driver.find_element(By.ID, "input-email").send_keys("reddy.csri@gmail.com")
driver.find_element(By.ID, "input-password").send_keys(decodedStr)
time.sleep(5)
driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(5)