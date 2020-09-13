from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CatalogPage import CatalogPage
from pageObjects.OrderPage import OrderPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        orderPage=OrderPage(self.driver)
        catalogPage=CatalogPage(self.driver)

        orderPage.enterAddressSearchInputBox()
        orderPage.selectDelieveryAddress()
        orderPage.clickDelieveryButton()
        orderPage.clickContinueButton()
        orderPage.clickContinueOrderButton()
        assert orderPage.verifyCatalogPageReDirect()
        catalogPage.selectProduct()
        assert catalogPage.verifyProductDetailsModalDisplayed()

