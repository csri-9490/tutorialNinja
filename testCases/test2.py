# from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
ch_op=webdriver.ChromeOptions()
ch_op.add_argument("--headless=new")#--headless=new
for i in range(1,3):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    driver=webdriver.Chrome(options=chrome_options)#,options=chrome_options)
    driver.get("https://www.spicejet.com/")
    open("https://www.spicejet.com/")
    driver.find_element(By.XPATH,"//div[@data-testid='to-testID-destination']/div/div[2]").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//div[@data-testid='to-testID-destination']//div[2][@class='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep']//input[@class='css-1cwyjr8 r-homxoj r-ubezar r-10paoce r-13qz1uu']").send_keys("Tirupati")
    time.sleep(5)
    # drpdown=driver.find_elements(By.XPATH,"//div[@class='css-1dbjc4n r-knv0ih r-1k1q3bj r-ql8eny r-1dqxon3']")
    # for i in drpdown:
    #     print(i.text)
    #     time.sleep(5)
        # if i.text=='Tirupati International Airport':
        #     i.click()
            # time.sleep(5)
            # driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-1awozwy r-ov7bg r-1loqt21 r-18u37iz r-1wtj0ep r-b5h31w r-rnv2vh r-5njf8e r-1otgn73']//div[@class='css-1dbjc4n r-18u37iz']").click()
    # time.sleep(5)
    driver.find_element(By.XPATH,"//div[@data-testid='undefined-month-March-2024']//div[3]//div[4][@class='css-1dbjc4n r-6koalj r-18u37iz r-d0pm55']//div[7]/div[1][@class='css-1dbjc4n r-1awozwy r-1pi2tsx r-1777fci r-13qz1uu']//div[text()='24']").click()
    driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-18u37iz r-19h5ruw r-184en5c']//div[1][@class='css-1dbjc4n']/div[1]//div[2][@class='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep']//div[@class='css-76zvg2 css-bfa6kz r-homxoj r-ubezar']").click()
    driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-14lw9ot r-z2wwpe r-1rjd0u6 r-1g94qm0 r-h3f8nf r-u8s1d r-13qz1uu r-8fdsdq']/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]").click()
    driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-18u37iz r-19h5ruw r-184en5c']//div[1][@class='css-1dbjc4n']/div[1]//div[2][@class='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep']//div[@class='css-76zvg2 css-bfa6kz r-homxoj r-ubezar']").click()
    driver.implicitly_wait(3)
    button = driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-1awozwy r-z2wwpe r-1loqt21 r-18u37iz r-1777fci r-1g94qm0 r-d9fdf6 r-1w50u8q r-ah5dr5 r-1otgn73']")
    button.click()
    time.sleep(5)
    details=driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-1habvwh r-1777fci']/div").text
    # driver.get_screenshot_as_file('fname54.png')
    print(details)
    driver.refresh()