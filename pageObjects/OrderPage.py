from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
import time



class OrderPage(BaseClass):


    def __init__(self,driver):
        self.driver= driver

    addressSearchInputBox=(By.ID,"addresstext")
    delieveryAddressText=(By.XPATH,"//div[contains(@class,'tt-dataset-2')]//div[text()='1084 E Lancaster Ave, Bryn Mawr, PA']")
    delieveryButton=(By.XPATH,"//h5[text()='Bryn Mawr, PA']/parent::div//button[text()='Delivery']")
    continueButton=(By.XPATH,"//button[text()='Continue']")
    continueOrderButton = (By.XPATH, "//div[@class='card-footer datepicker']//button[text()='Continue']")

    def enterAddressSearchInputBox(self):
          self.driver.find_element(*OrderPage.addressSearchInputBox).send_keys("1084 East Lancaster Ave Byrn Mawr, PA")

    def selectDelieveryAddress(self):
        self.waitForElementVisible("//div[contains(@class,'tt-dataset-2')]//div[text()='1084 E Lancaster Ave, Bryn Mawr, PA']")
        self.driver.find_element(*OrderPage.delieveryAddressText).click()

    def clickDelieveryButton(self):
        self.waitForElementVisible("//h5[text()='Bryn Mawr, PA']/parent::div//button[text()='Delivery']")
        delieveryButton = self.driver.find_element_by_xpath("//h5[text()='Bryn Mawr, PA']/parent::div//button[text()='Delivery']")
        self.driver.execute_script("arguments[0].click();", delieveryButton)

    def clickContinueButton(self):
        self.waitForElementVisible("//button[text()='Continue']")
        self.driver.find_element(*OrderPage.continueButton).click()

    def clickContinueOrderButton(self):
        self.waitForElementVisible("//div[@class='card-footer datepicker']//button[text()='Continue']")
        time.sleep(2)
        self.driver.find_element(*OrderPage.continueOrderButton).click()
        WebDriverWait(self.driver, 20).until(expected_conditions.title_contains("Catalog"))

    def verifyCatalogPageReDirect(self):
        return self.driver.title=="Insomnia Cookies | Catalog"