from datetime import datetime

import allure

from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import MyAccountButtonLocators
from pages.base_page import BasePage
from pages.common import Common
from src.src import CapitalComPageSrc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class MyAccountButton(BasePage):
    @allure.step(f"{datetime.now()}   Start full test of 'My account' button in the header")
    def full_test(self, d, cur_language, cur_country, cur_role, link):
        self.arrange_(d)
        self.element_click()

        test_element = AssertClass(d, self.bid)
        match cur_role:
            case "Auth":
                test_element.assert_my_account_menu(d)

    def arrange_(self, link):
        print(f"\n{datetime.now()}   1. Arrange for My account button")

        if not self.current_page_is(link):
            self.link = CapitalComPageSrc.URL_NEW
            self.open_page()

        print(f"{datetime.now()}   Is BUTTON_MY_ACCOUNT present on the page? =>")
        button = self.driver.find_elements(*MyAccountButtonLocators.BUTTON_MY_ACCOUNT)
        if len(button) == 0:
            print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is not present on the page")
            Common().pytest_fail("BUTTON_MY_ACCOUNT is not present on the page")
        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is present on the page")

        self.driver.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button[0]
        )

        print(f"{datetime.now()}   Is BUTTON_MY_ACCOUNT clickable?  =>")
        time_out = 3
        if not self.element_is_clickable(button[0], time_out):
            print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is not clickable after {time_out} sec")
            Common.pytest_fail("Bug ? BUTTON_MY_ACCOUNT is not clickable")
        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is clickable")

    @allure.step("Click My account button in the page header")
    def element_click(self):
        print(f"{datetime.now()}   2. Act for My account button")
        print(f"{datetime.now()}   Start to click BUTTON_MY_ACCOUNT =>")

        button = self.driver.find_elements(*MyAccountButtonLocators.BUTTON_MY_ACCOUNT)
        button[0].click()

        WebDriverWait(self.driver, 10).until(
            EC.url_changes(self.driver.current_url)
        )

        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is clicked")
