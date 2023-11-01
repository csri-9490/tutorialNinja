from selenium import  webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture
def setup(request):
    # ch_op=Options()
    # ch_op = webdriver.ChromeOptions()
    # ch_op.add_argument('--disable-gpu')
    # ch_op.add_argument('--no-sandbox')
    # ch_op.add_argument("--headless")
    # srv=Service("D:\drivers\geckodriver.exe")
    # s1 = Service(executable_path="D:\drivers\geckodriver.exe")
    # driver=webdriver.Chrome(service=srv)
    # driver=webdriver.Firefox(service=srv)
    # driver = webdriver.Chrome(service=Service("D:\\drivers\\chromedriver.exe"))
    if browser == 'chrome':
            driver = webdriver.Chrome()
    elif browser == 'firefox':
            driver = webdriver.Firefox()
    else:
            driver = webdriver.Chrome()
    # return driver
    request.cls.driver = driver


@pytest.fixture
def browser(request):
     return  request.config.getoption("--browser")