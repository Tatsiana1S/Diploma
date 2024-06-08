import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Selenium.pages.cart_page import CartPage
from Selenium.pages.catalog_page import CatalogPage
from Selenium.pages.item_list_page import ItemListPage
from Selenium.pages.item_page import ItemPage
from Selenium.pages.main_page import MainPage


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.onliner.by/")

    return driver


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def item_page(driver):
    yield ItemPage(driver)


@pytest.fixture(autouse=True)
def cart_page(driver):
    yield CartPage(driver)


@pytest.fixture(autouse=True)
def item_list_page(driver):
    yield ItemListPage(driver)


@pytest.fixture(autouse=True)
def catalog_page(driver):
    yield CatalogPage(driver)
