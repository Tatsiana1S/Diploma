import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from Selenium.locators.item_list_page_locators import SHOP_CHECKBOX, DEVICE_STATUS_CHECKBOX, \
    FIRST_ITEM
from Selenium.pages.base_page import BasePage


class ItemListPage(BasePage):
    @property
    def device_status_checkbox(self):
        return self.find(DEVICE_STATUS_CHECKBOX)

    @property
    def shop_checkbox(self):
        return self.find(SHOP_CHECKBOX)

    @property
    def first_item(self):
        return self.find(FIRST_ITEM)

    def mark_device_status_checkbox(self):
        """
        This method marks device status checkbox
        """
        with allure.step("Mark device status checkbox"):
            action = ActionChains(self.driver)
            origin = ScrollOrigin(self.device_status_checkbox, 0, 0)
            action.scroll_from_origin(origin, 0, 300).perform()

            self.click(DEVICE_STATUS_CHECKBOX)

    def mark_shop_checkbox(self):
        """
        This method marks shop checkbox
        """
        with allure.step("Mark shop checkbox"):
            action = ActionChains(self.driver)
            origin = ScrollOrigin(self.shop_checkbox, 0, 0)
            action.scroll_from_origin(origin, 0, 300).perform()

            self.click(SHOP_CHECKBOX)

    def choose_first_item(self):
        """
        This method clicks on first item from list
        """
        with allure.step("Click on first item from list"):
            action = ActionChains(self.driver)
            action.scroll_to_element(self.first_item).perform()

            self.click(FIRST_ITEM)
