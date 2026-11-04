from selenium.webdriver.common.by import By


class InventoryPage:

    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")

    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def open_cart(self):
        self.driver.find_element(*self.SHOPPING_CART).click()
