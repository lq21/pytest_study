import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = None

@pytest.fixture(scope="session")
def browser():
    global driver
    if driver is None:
        #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver = webdriver.Chrome(service=Service(executable_path=r"C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"))
        driver.maximize_window()
        yield driver
        # 所有用例执行完毕退出浏览器
        driver.quit()