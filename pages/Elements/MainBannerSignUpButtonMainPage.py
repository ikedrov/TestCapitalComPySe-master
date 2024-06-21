"""
-*- coding: utf-8 -*-
@Time    : 2024/02/26 22:20
@Author  : Artem Dashkov
"""
from datetime import datetime
import pytest
import allure

from pages.base_page import BasePage
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import MainBannerLocators
from pages.Signup_login.signup_login import SignupLogin
from selenium.common.exceptions import ElementClickInterceptedException


class MainBannerSignUpButtonMainPage(BasePage):

    @allure.step(f'{datetime.now()}   Start Full test for Sign Up button of Main banner')
    def full_test_with_tpi(self, d, cur_language, cur_country, cur_role, cur_item_link):
        self.arrange_(d, cur_item_link)
        self.element_click()

        test_element = AssertClass(d, cur_item_link, self.bid)
        match cur_role:
            case "NoReg":
                if cur_country == 'gb':
                    test_element.assert_signup_pause(d, cur_language, cur_item_link)
                else:
                    test_element.assert_signup(d, cur_language, cur_item_link)
            case "NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v4(d, cur_item_link)

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange_v0")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        button_list = self.driver.find_elements(*MainBannerLocators.BUTTON_SIGN_UP_MAIN_PAGE)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_SIGN_UP is not present on this page")
            del button_list
            pytest.fail("Testing element 'BUTTON_SIGN_UP on the main banner' is not present on this page")
        else:
            print(f"{datetime.now()}   => BUTTON_SIGN_UP is present on this page")

        print(f"{datetime.now()}   BUTTON_SIGN_UP scroll =>")
        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});', button_list[0]
        )

        print(f"{datetime.now()}   BUTTON_SIGN_UP is visible? =>")
        if self.element_is_visible(MainBannerLocators.BUTTON_SIGN_UP_MAIN_PAGE):
            print(f"{datetime.now()}   => BUTTON_SIGN_UP is visible on this page")
        else:
            print(f"{datetime.now()}   => BUTTON_SIGN_UP is not visible on this page")
            pytest.fail("Bug! Testing element 'BUTTON_SIGN_UP on main banner' is present on this page, "
                        "but not visible")

    @allure.step("Click button [Sign Up] on Main banner")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act_v0")

        button_list = self.driver.find_elements(*MainBannerLocators.BUTTON_SIGN_UP_MAIN_PAGE)
        print(f"{datetime.now()}   BUTTON_SIGN_UP is clickable? =>")
        time_out = 3
        if not self.element_is_clickable(button_list[0], time_out):
            print(f"{datetime.now()}   => BUTTON_SIGN_UP is not clickable after {time_out} sec. Stop TC>")
            pytest.fail(f"BUTTON_SIGN_UP is not clickable after {time_out} sec.")

        try:
            self.driver.execute_script("arguments[0].click();", button_list[0])
            print(f"{datetime.now()}   => BUTTON_SIGN_UP clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_SIGN_UP NOT CLICKED")
            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

            page_ = SignupLogin(self.driver)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            self.driver.execute_script("arguments[0].click();", button_list[0])
            del page_

        del button_list
        return True
