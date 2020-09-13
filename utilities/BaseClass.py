import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def waitForElementVisible(self, selector):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH,selector)))
