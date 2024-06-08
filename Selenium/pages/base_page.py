from typing import Tuple
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def find(self, locator: Tuple[str, str], timeout: int = 5):
        """
        This method finds element
        :param locator: element locator
        :param timeout: timeout
        :return: web element
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator: Tuple[str, str], timeout: int = 5):
        """
        This method clicks on element
        :param locator: element locator
        :param timeout: timeout
        :return: web element
        """
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def text(self, locator: Tuple[str, str], timeout: int = 5) -> str:
        """
        This method return text of element
        :param locator: element locator
        :param timeout: timeout
        :return: text of element
        """
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    def wait_for(self, locator: Tuple[str, str], timeout: int = 5):
        """
        This method waits visible area of element
        :param locator: element locator
        :param timeout: timeout
        :return: web element
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator: Tuple[str, str], timeout: int = 5):
        """
        This method waits for element to be clickable
        :param locator: element locator
        :param timeout: timeout
        :return: web element
        """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
