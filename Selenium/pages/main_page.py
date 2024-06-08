import allure
from Selenium.locators.main_page_locators import CATALOG
from Selenium.pages.base_page import BasePage


class MainPage(BasePage):
    @property
    def catalog_button(self):
        return self.find(CATALOG)

    def open_catalog(self):
        """
        This method opens catalog
        """
        with allure.step("Open catalog"):
            self.catalog_button.click()
