import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=ASKXGp3Ljg8EH6dABnL6aM1HLjpKHkvScfbdrNUY1844RJD72ddNhfmtaMfJnK7Y7Mk-t8x3MAeqXQ&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-117284388%3A1702279901432257&theme=glif")
driver.find_element(By.XPATH,"//input[@id='identifierId']").send_keys("srikanthchelukala@gmail.com")
driver.find_element(By.XPATH,"(//span[@class='VfPpkd-vQzf8d'])[2]").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@class='whsOnd zHQkBf'])[1]").send_keys("Shivaya9@")
driver.find_element(By.XPATH,"(//span[@class='VfPpkd-vQzf8d'])[2]").click()
#
#
# driver.switch_to.window(driver.window_handles[1])
# l1=[1,3,4,5,6,7,4,7]
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)

# with open('D:\\notepad++_savedocs\\tst1.txt','r') as reader:
#     f1=reader.read()
#     print(f1)
#     d1={}
#     for i in f1:
#         if i in d1:
#             d1[i]=d1[i]+1
#         else:
#             d1[i]=1
#     print(d1)




