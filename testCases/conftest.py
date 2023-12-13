from selenium import  webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.service import Service as ChromeService


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture()
def setup(request):
    global driver
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
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
            driver = webdriver.Chrome()
    elif browser_name == 'firefox':
            driver = webdriver.Firefox()
    else:
            browser_name = webdriver.Chrome()
    # return driver
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()






# @pytest.fixture
# def browser(request):
#      return  request.config.getoption("--browser")