from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
import time

class CatalogPage(BaseClass):
    def __init__(self,driver):
        self.driver= driver

    selectProductImage = (By.XPATH, "//img[@alt='Insomniac (24 Classic)']")
    productDetailsModal=  (By.XPATH, "//h2[@class='modal-title' and text()='Insomniac (24 Classic)']")

    def selectProduct(self):
        self.waitForElementVisible("//img[@alt='Insomniac (24 Classic)']")
        self.driver.find_element(*CatalogPage.selectProductImage).click()

    def verifyProductDetailsModalDisplayed(self):
        self.waitForElementVisible("//h2[@class='modal-title' and text()='Insomniac (24 Classic)']")
        return self.driver.find_element(*CatalogPage.productDetailsModal).is_displayed()


