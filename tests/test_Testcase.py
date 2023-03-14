import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObject.Homepage import Homepage


@pytest.mark.usefixtures("setup")
class TestBuy:
    def test_1st(self):
        buy_tab = Homepage(self.driver)
        buy_tab.click_buytab()
        time.sleep(3)
        buy_tab.select_location()
        time.sleep(3)
        buy_tab.for_particular_location()
        time.sleep(4)
        buy_tab.to_get_selected_location()
        time.sleep(5)

    def test_2nd(self):
        buy_tab = Homepage(self.driver)
        buy_tab.click_buytab()
        time.sleep(3)
        buy_tab.select_for_particular_location()
        time.sleep(3)
        buy_tab.choose_for_particular_location()
        time.sleep(4)
        buy_tab.search_bar_is_shown()
        time.sleep(5)
        buy_tab.find_agent_is_shown()
        time.sleep(5)

    def test_3rd(self):
        buy_tab = Homepage(self.driver)
        buy_tab.click_buytab
        time.sleep(3)
        buy_tab.buyer_location_choices()
        time.sleep(2)
        buy_tab.buyer_selected_location()
        time.sleep(4)
        buy_tab.search_under_budjet()
        time.sleep(3)
        buy_tab.feeding_minimum_budjet()
        time.sleep(2)
        buy_tab.feeding_maximum_budjet()
        time.sleep(3)
        buy_tab.fixing_the_budjet()
        time.sleep(2)
        buy_tab.searching_under_feeded_budjet()
        time.sleep(10)

    def test_4th(self):
        buy_tab = Homepage(self.driver)
        buy_tab.click_buytab()
        time.sleep(3)
        buy_tab.switch_to_the_window()
        buy_tab.rates_and_trends()
        time.sleep(10)

    def test_5th(self):
        buy_tab = Homepage(self.driver)
        buy_tab.click_buytab()
        time.sleep(5)
        buy_tab.tips_and_guides()
        time.sleep(6)
        buy_tab.switch_to_the_window()
        time.sleep(2)
        buy_tab.scroll_to_middle()
        time.sleep(5)
        buy_tab.choose_first_location()
        time.sleep(10)
        buy_tab.select_first_location()
        time.sleep(15)
        buy_tab.choose_second_location()
        time.sleep(10)
        buy_tab.select_second_location()
        time.sleep(15)
        buy_tab.click_compare_button()
        time.sleep(10)

    def test_6th(self):
        buy_tab = Homepage(self.driver)
        buy_tab.click_buytab()
        time.sleep(6)
        buy_tab.propworth()
        time.sleep(5)