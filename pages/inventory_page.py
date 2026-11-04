from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")

    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")

    MENU_BUTTON = (By.ID, "react-burger-menu-btn")

    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def open_cart(self):
        self.driver.find_element(*self.SHOPPING_CART).click()

    def open_menu(self):
        self.driver.find_element(*self.MENU_BUTTON).click()

    def logout(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        ).click()
