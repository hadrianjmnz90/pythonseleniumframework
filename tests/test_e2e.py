import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        checkout_page = home_page.shopItems()
        log.info("getting all the card titles")
        cards = checkout_page.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            card_text = card.text
            log.info(card_text)
            if card_text == "Blackberry":
                checkout_page.getCardFooter()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        confirm_page = checkout_page.checkOutItems()
        log.info("Entering country name as ind")
        confirm_page.enter_country()
        self.verifyLinkPresence("India")
        log.info("Country was displayed within time limit ")
        confirm_page.click_country()
        log.info("country clicked")
        confirm_page.click_checkbox()
        log.info("checkbox checked")
        confirm_page.click_submit_btn()
        log.info("submit button clicked")
        text_match = confirm_page.get_alert_text()
        log.info("Text received from application is " + text_match)
        assert ("Success! Thank you!" in text_match)
