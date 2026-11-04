from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utils.json_reader import read_users


def test_checkout_information(driver):

    users = read_users()

    username = users["valid_user"]["username"]
    password = users["valid_user"]["password"]

    first_name = users["checkout_user"]["first_name"]
    last_name = users["checkout_user"]["last_name"]
    postal_code = users["checkout_user"]["postal_code"]

    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    checkout_page.fill_checkout_information(first_name, last_name, postal_code)

    assert "checkout-step-two" in driver.current_url
