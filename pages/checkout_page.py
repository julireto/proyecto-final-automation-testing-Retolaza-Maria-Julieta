from selenium.webdriver.common.by import By


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")

    LAST_NAME = (By.ID, "last-name")

    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()
