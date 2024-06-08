import allure
import pytest


class TestAddToBucket:
    @allure.feature("Bucket")
    @allure.title("Test bucket")
    @allure.id("1")
    @allure.epic("J-1")
    @allure.severity("Major")
    @pytest.mark.smoke
    def test_bucket(self, main_page, catalog_page, item_list_page, item_page, cart_page):
        main_page.open_catalog()

        catalog_page.open_parent_category()
        catalog_page.open_child_category()

        item_list_page.mark_device_status_checkbox()
        item_list_page.mark_shop_checkbox()
        item_list_page.choose_first_item()

        item_page.add_to_cart()
        item_price = item_page.item_price
        item_page.go_to_cart()

        cart_page.check_cart_title()
        cart_page.check_cart_price(item_price)
        cart_page.check_cart_items_amount(1)
        cart_page.check_submit_is_clickable()
