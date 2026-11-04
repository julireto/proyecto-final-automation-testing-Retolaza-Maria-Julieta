from pages.login_page import LoginPage
from utils.json_reader import read_users
from utils.logger import logger


def test_valid_login(driver):

    logger.info("Inicio test_valid_login")

    users = read_users()

    username = users["valid_user"]["username"]
    password = users["valid_user"]["password"]

    driver.get("https://www.saucedemo.com")

    logger.info("Pagina abierta")

    login_page = LoginPage(driver)

    login_page.login(username, password)

    logger.info("Login correcto")

    assert "inventory" in driver.current_url

    logger.info("Fin test_valid_login")


def test_invalid_login(driver):

    logger.info("Inicio test_invalid_login")

    users = read_users()

    username = users["invalid_user"]["username"]
    password = users["invalid_user"]["password"]

    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)

    login_page.login(username, password)

    logger.info("Login invalido ejecutado")

    assert "inventory" not in driver.current_url

    logger.info("Fin test_invalid_login")
