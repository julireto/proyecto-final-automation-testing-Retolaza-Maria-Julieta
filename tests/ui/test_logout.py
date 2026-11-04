from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

from utils.json_reader import read_users


def test_logout(driver):

    users = read_users()

    username = users["valid_user"]["username"]
    password = users["valid_user"]["password"]

    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)

    inventory_page.open_menu()

    inventory_page.logout()

    assert "saucedemo.com" in driver.current_url
