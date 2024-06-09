from selenium.webdriver.common.by import By

DEVICE_STATUS_CHECKBOX = By.XPATH, '//div[contains(text(), "новый")]'

SHOP_CHECKBOX = By.XPATH, '//div[contains(text(), "встроенная")]'

FIRST_ITEM = By.XPATH, ('//div[@class="catalog-form__offers-unit catalog-form__offers-unit_primary"][1]//a['
                        '@class="catalog-form__link catalog-form__link_primary-additional '
                        'catalog-form__link_base-additional catalog-form__link_font-weight_semibold '
                        'catalog-form__link_nodecor"]')
