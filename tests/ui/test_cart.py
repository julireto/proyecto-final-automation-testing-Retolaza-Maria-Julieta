from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.json_reader import read_users


def test_add_product_to_cart(driver):

    users = read_users()

    username = users["valid_user"]["username"]
    password = users["valid_user"]["password"]

    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack_to_cart()

    inventory_page.open_cart()

    assert "cart" in driver.current_url
