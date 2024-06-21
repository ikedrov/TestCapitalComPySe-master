"""
-*- coding: utf-8 -*-
@Time    : 2023/04/29 00:30
@Author  : Suleyman Alirzaev
"""
import random
from datetime import datetime

import pytest
import allure
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

from pages.base_page import BasePage
from pages.common import Common
from pages.Elements.testing_elements_locators import ButtonTradeOnWidgetMostTradedLocators
from test_data.trading_platform_data import data
from pages.Elements.AssertClass import AssertClass
from pages.Capital.Trading_platform.trading_platform_locators import TradingInstruments
from pages.Signup_login.signup_login import SignupLogin


class ButtonTradeOnWidgetMostTraded(BasePage):

    @allure.step(f'{datetime.now()}   Start Full test Trade button on Most Traded widget')
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        qty_rnd = 1
        # self.clear_chart_list()
        num_item = self.arrange_v4(cur_item_link)
        random_indexes = random.sample(range(0, num_item), qty_rnd)
        print(f"\n{datetime.now()}   Random indexes = {random_indexes}")
        counter = 0
        for i, index in enumerate(random_indexes):
            # if counter:
            #     self.clear_chart_list()
            #     self.arrange_v4(cur_item_link)

            print(f"\n{datetime.now()}   Testing Most traded {i + 1} random element with {index} index")
            trade_instrument = self.element_click_v4(index)
            if not trade_instrument:
                Common().pytest_fail("Bug # ??? Testing element is not clicked")

            test_element = AssertClass(d, cur_item_link, self.bid)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    test_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform_v4(d, cur_item_link, False, True, trade_instrument)
            counter += 1

    def full_test(self, d, cur_language, cur_country, cur_role, cur_item_link):
        # self.clear_chart_list()
        num_item = self.arrange_v4(cur_item_link)
        random_indexes = random.sample(range(0, num_item), 2)
        counter = 0
        for i, index in enumerate(random_indexes):
            # if counter:
            #     # self.clear_chart_list()
            #     self.arrange_v4(cur_item_link)

            print(f"\n{datetime.now()}   Testing Most traded random element #{i + 1}")
            trade_instrument = self.element_click_v4(index)
            if not trade_instrument:
                pytest.fail("Testing element is not clicked")

            check_element = AssertClass(d, cur_item_link)
            counter += 1
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, cur_item_link)
                case "NoAuth":
                    check_element.assert_login(d, cur_language, cur_item_link)
                case "Auth":
                    check_element.assert_trading_platform_v4(d, cur_item_link, False, True, trade_instrument)

    def arrange_v4(self, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v4")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   MOST_TRADED is present? =>")
        item_list = self.driver.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED_LIST)
        num_item = len(item_list)
        if num_item == 0:
            print(f"{datetime.now()}   => MOST_TRADED is not present on this page")
            Common().pytest_fail("Bug # ??? Checking element is not on this page")
        print(f"{datetime.now()}   => MOST_TRADED widget is present on this page")
        print(f"{datetime.now()}   => Found {num_item} elements in block MOST_TRADED")

        print(f"{datetime.now()}   Most traded widget is scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', item_list[0])
        print(f"{datetime.now()}   => Most traded widget is scrolled into screen center")

        # возвращаем количество элементов в Most Trade block
        return num_item

    def clear_chart_list(self):
        """
        Clear all tabs on the Charts menu of the Trading platform
        """
        print(f"\n{datetime.now()}   Clear Top Chart list =>")
        chart_link = data["CHART_URL"]

        if not self.wait_for_target_url(chart_link, 1):
            self.link = chart_link
            self.open_page()

        close_all_buttons = self.elements_are_present(*TradingInstruments.CLOSE_ALL_BUTTON)
        if len(close_all_buttons) > 1:
            close_all_buttons[1].click()
        # проверка, что все вкладки удалены
        close_all_buttons = self.elements_are_present(*TradingInstruments.CLOSE_ALL_BUTTON)
        if len(close_all_buttons) != 0:
            print(f"{datetime.now()}   => Bug!!! The [Close all] button on the Trading platform page is not closed "
                  f"all chart tabs")

    @allure.step('Click Trade button on Most traded widget')
    def element_click_v4(self, random_index):
        print(f"\n{datetime.now()}   2. Act_v4")

        # Checking if [SignUP for is popped up on the page]
        check_popup = SignupLogin(self.driver, self.link)
        check_popup.check_popup_signup_form()
        del check_popup
        #

        trade_instrument_list = self.driver.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED_NAME_LIST)
        if len(trade_instrument_list) == 0:
            Common().pytest_fail("Problem! List of instruments is empty.")
        instrument_item = trade_instrument_list[random_index]
        # print(f"{datetime.now()}   instrument_item = {instrument_item}")
        instrument_title = instrument_item.get_attribute('title')
        print(f"{datetime.now()}   instrument_title = '{instrument_title}'")

        item_list = self.driver.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED_LIST)
        element = item_list[random_index]

        print(f"{datetime.now()}   Selected Trade button on Most traded widget is scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', element)

        print(f"{datetime.now()}   Selected Trade button click for '{instrument_title}' trading instrument =>")

        ActionChains(self.driver) \
            .move_to_element(element) \
            .pause(0.5) \
            .move_to_element(element) \
            .perform()

        if not self.element_is_clickable(element, 3):
            return ""

        ActionChains(self.driver) \
            .click() \
            .perform()
        print(f"{datetime.now()}   => Selected Trade button clicked!")

        return instrument_title  # возвращаем название торгового инструмента

    def arrange_v3(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v3")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   MOST_TRADED is visible? =>")
        if len(self.driver.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED_LIST)) == 0:
            print(f"{datetime.now()}   => MOST_TRADED is not visible on the page!")
            pytest.skip("Checking element is not on this page")
        print(f"{datetime.now()}   => MOST_TRADED is visible on the page!")

    @allure.step("Click button MOST_TRADED")
    def element_click_v3(self, i, cur_role):
        print(f"\n{datetime.now()}   2. Act_v3")
        i -= 1
        button_list = self.driver.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED_LIST)
        # if len(button_list) == 0:
        #     print(f"{datetime.now()}   => MOST_TRADED is not present on the page!")
        #     del button_list
        #     return False

        print(f"{datetime.now()}   MOST_TRADED scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[i]
        )

        # Удаляем класс js-mostTraded у Most traded блока, чтобы избежать рандомных фейлов
        # (кнопки меняют состояние каждые ~2.5 секунды)
        print(f"{datetime.now()}   MOST_TRADED delete js-mostTraded class =>")
        # if i == 0:
        #     self.driver.execute_script('document.getElementsByClassName("js-mostTraded")[0].'
        #                                 'classList.remove("js-mostTraded");')
        self.driver.execute_script('document.getElementsByClassName("js-mostTraded")[0].'
                                    'classList.remove("js-mostTraded");')

        # Вытаскиваем линку из кнопки
        button_link = button_list[i].get_attribute('href')
        # Берём ID item, на который кликаем для сравнения с открытым ID на платформе
        target_link = button_link[button_link.find("spotlight") + 10:button_link.find("?")]
        print(f"{datetime.now()}   Start Click button MOST_TRADED with id item {target_link} =>")

        # Наводим на тестовый элемент, чтобы кнопка могла корректно отработать нажатие
        # hover = ActionChains(self.driver).move_to_element(button_list[i])

        print(f"{datetime.now()}   MOST_TRADED click =>")
        try:
            print(f"{datetime.now()}   MOST_TRADED is clickable? =>")
            self.element_is_clickable(button_list[i], 10)
            # button_list[i].click()
            self.driver.execute_script("arguments[0].click();", button_list[i])
            print(f"{datetime.now()}   => MOST_TRADED clicked!")

        except ElementClickInterceptedException:
            print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")

            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_form()
            del page_
            self.driver.execute_script("arguments[0].click();", button_list[i])
            print(f"{datetime.now()}   => MOST_TRADED clicked!")

        return target_link

    @allure.step("Works ARRANGE MOST_TRADED (generator) - ver 2")
    def arrange_v2_(self):
        print(f"\n{datetime.now()}   1. Arrange_v2")
        self.open_page()
        item_list = self.driver.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED_LIST)
        if len(item_list) == 0:
            pytest.skip("No items found for testing")
        print(f"{datetime.now()}   => Found {len(item_list)} elements in block MOST_TRADED")
        random_element_for_test = random.sample(range(0, len(item_list)), 2)
        for i in random_element_for_test:
            yield item_list[i]
            self.open_page()
            item_list = self.driver.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED_LIST)

    @allure.step("Click button MOST_TRADED - ver 2")
    def element_click_v2(self, web_element):
        print(f"\n{datetime.now()}   2. Act_v2")
        print(f"{datetime.now()}   Start Click button MOST_TRADED =>")
        print(f"{datetime.now()}   MOST_TRADED Deleting a class that expanded items =>")
        self.driver.execute_script(
            'document.getElementsByClassName("mostTraded__box--expanded")[0]'
            '.classList.remove("mostTraded__box--expanded");')
        print(f"{datetime.now()}   MOST_TRADED scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            web_element
        )
        print(f"{datetime.now()}   MOST_TRADED click ver 2 =>")
        try:
            web_element.click()
            return True
        except ElementClickInterceptedException:
            return False
