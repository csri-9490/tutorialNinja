from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.espncricinfo.com/series/ireland-emerging-players-in-west-indies-2023-24-1410093/west-indies-academy-vs-ireland-emerging-players-2nd-unofficial-test-1410335/full-scorecard")
rows=driver.find_elements(By.XPATH,"//tbody/tr")
total_rows=len(rows)
cols=driver.find_elements(By.XPATH,"//tbody/tr[1]/td")
total_cols=len(cols)
# print(total_rows)
# print(total_cols)
# for i in rows:
#     print(i.text)

start_xpath="//tbody/tr["
mid_xpath="]/td["
end_xpath="]"
for row in range(1,total_rows+1):
    for col in range(1,total_cols):
        print(driver.find_element(By.XPATH,start_xpath + str(row) + mid_xpath + str(col) + end_xpath).text, end=" ")
    # print()