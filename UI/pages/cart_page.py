import allure
from UI.locators.cart_page_locators import TXT_CART_PRICE, IN_ITEM_COUNT, BN_SUBMIT
from UI.pages.base_page import BasePage


class CartPage(BasePage):
    @property
    def item_count(self):
        return self.find(IN_ITEM_COUNT)

    def check_cart_price(self, expected_price: str):
        """
        This method checks card price
        :param expected_price: expected price
        """
        with allure.step("Check cart price"):
            cart_price = self.text(TXT_CART_PRICE).split()[0]

            assert expected_price == cart_price, f"Prices are not equal, {expected_price=} != {cart_price=}"

    def check_cart_items_amount(self, expected_amount: int):
        """
        This method checks cart items amount
        :param expected_amount: expected amount
        """
        with allure.step("Check cart items amount"):
            cart_amount = int(self.item_count.get_attribute('value'))

            assert expected_amount == cart_amount, f"Amounts are not equal, {expected_amount} != {cart_amount}"

    def check_cart_title(self):
        """
        This method checks cart title
        """
        with allure.step("Check cart title"):
            page_title = self.driver.title

            assert page_title == "Корзина заказов onliner.by", f"Navigation wrong. {page_title=} != 'Корзина заказов onliner.by'"

    def check_submit_is_clickable(self):
        """
        This method checks submit button is clickable
        """
        with allure.step("Check submit button is clickable"):
            self.wait_for_element_to_be_clickable(BN_SUBMIT)
