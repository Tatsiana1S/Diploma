from selenium.webdriver.common.by import By

TXT_CART_PRICE = By.XPATH, '//div[contains(@class, "cart-form__offers-part_sum_clover")]'

IN_ITEM_COUNT = By.XPATH, ('//div[@class="input-style__wrapper cart-form__input-wrapper '
                           'cart-form__input-wrapper_nonadaptive"]/input')

BN_SUBMIT = By.XPATH, '//a[contains(text(), "Перейти к оформлению")]'
