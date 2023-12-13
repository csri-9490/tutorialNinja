from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.espncricinfo.com/series/ireland-emerging-players-in-west-indies-2023-24-1410093/west-indies-academy-vs-ireland-emerging-players-2nd-unofficial-test-1410335/full-scorecard")
# els=driver.find_elements(By.XPATH,"(/html[1]/body[1]/div[1]/section[1]/section[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr/td[3])")
# mns=driver.find_element(By.XPATH,"(/html[1]/body[1]/div[1]/section[1]/section[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr/td[3])[13]")
# s1=[]
# sum=0
# for i in els:
#     sum=sum+int(i.text)
# print(sum-int(mns.text))

SR=driver.find_elements(By.XPATH,"/html/body[1]/div[1]/section[1]/section[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]//td[8]")
sum1=0
for i in SR:
    sum1=sum1+float(i.text)
print(sum1)



