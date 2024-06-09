import allure
from UI.locators.catalog_page_locators import PARENT_CATEGORY, CHILD_CATEGORY
from UI.pages.base_page import BasePage


class CatalogPage(BasePage):
    @property
    def parent_category_button(self):
        return self.find(PARENT_CATEGORY)

    @property
    def child_category_button(self):
        return self.find(CHILD_CATEGORY)

    def open_parent_category(self):
        """
        This method opens parent category
        """
        with allure.step("Open parent category"):
            self.parent_category_button.click()

    def open_child_category(self):
        """
        This method opens child category button
        """
        with allure.step("Open child category button"):
            self.child_category_button.click()
