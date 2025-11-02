import pytest
from pom.page.LoginPage import LoginPage
from pom.page.SwagLabsPage import SwagLabsPage
from time import sleep

def test_001(browser):
    lp = LoginPage(browser)
    lp.get_url("https://www.saucedemo.com/")
    lp.do_login("standard_user", "secret_sauce")

def test_002():
    1/0

def test_003(browser):
    slp = SwagLabsPage(browser)
    slp.get_url("https://www.saucedemo.com/inventory.html")
    try:
        slp.click_add_to_cart("Sauce Labs Bike Light")
    except Exception as e:
        print(e)
    sleep(5)

if __name__ == "__main__":
    pytest.main(["-v","-s"])