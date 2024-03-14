import pytest

from pages.login_page import LoginPage
from config.config import GetConfig as config

@pytest.fixture(scope="session", autouse=True)
def login():
    login_page = LoginPage()
    login_page.login(config.username, config.password)
    yield login_page.driver
    login_page.driver.quit()