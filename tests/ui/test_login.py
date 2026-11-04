from pages.login_page import LoginPage
from utils.json_reader import read_users


def test_valid_login(driver):

    users = read_users()

    username = users["valid_user"]["username"]
    password = users["valid_user"]["password"]

    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)

    login_page.login(username, password)

    assert "inventory" in driver.current_url


def test_invalid_login(driver):

    users = read_users()

    username = users["invalid_user"]["username"]
    password = users["invalid_user"]["password"]

    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)

    login_page.login(username, password)

    assert "inventory" not in driver.current_url
