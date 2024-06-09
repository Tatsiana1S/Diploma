import allure
from UI.locators.item_page_locators import A_ITEM_PRICE, BN_ADD_TO_BUCKET, BN_GO_TO_CART
from UI.pages.base_page import BasePage


class ItemPage(BasePage):
    @property
    def item_price(self):
        return self.find(A_ITEM_PRICE).text.split()[0]

    def add_to_cart(self):
        """
        This method clicks on "Add to cart" button
        """
        with allure.step("Add item to cart"):
            self.click(BN_ADD_TO_BUCKET)

    def go_to_cart(self):
        """
        This method clicks on "Go to cart" button
        """
        with allure.step("Go to cart"):
            self.click(BN_GO_TO_CART)
