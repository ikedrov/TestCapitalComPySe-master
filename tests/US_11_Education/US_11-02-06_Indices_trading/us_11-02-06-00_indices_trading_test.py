"""
-*- coding: utf-8 -*-
@Time    : 2023/06/25 18:30 GMT+3
@Author  : Andrey Bozhko
"""
# import random
import pytest
import allure
# import logging

from pages.common import Common
from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.MainBannerStartTradingButton import MainBannerStartTrading
from pages.Elements.MostTradedWidgetTradeButton import ButtonTradeOnWidgetMostTraded
from pages.Elements.MainBannerTryDemoButton import MainBannerTryDemo
from pages.Elements.VerticalBannerButton import ButtonOnVerticalBanner
from pages.Elements.HorizontalBannerButton import ButtonOnHorizontalBanner
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.build_dynamic_arg import build_dynamic_arg_v4
from pages.Elements.testing_elements_locators import SubPages

# logger = logging.getLogger()
# first_run_pretest = True
count = 1
cur_page_url = ""


@pytest.mark.us_11_02_06_00
class TestIndicesTradingGuidePreset:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    @pytest.mark.test_01
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading] on Main banner
        Language: EN, AR, DE, ES, IT, CN, RU, ZH. License: All.
        """
        test_title = ("11.02.06", "Education > Menu item [Indices Trading]",
                      ".00_01", "Testing button [Start Trading] on Main banner")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "ar", "de", "es", "it", "cn", "ru", "zh"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_indices_trading_menu(d, cur_language, cur_country, main_page_link)

        test_element = MainBannerStartTrading(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    @pytest.mark.test_02
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading] on Main banner
        Language: EN, AR, DE, ES, IT, CN, RU, ZH. License: All.
        """
        test_title = ("11.02.06", "Education > Menu item [Indices Trading]",
                      ".00_02", "Testing button [Try demo] on Main banner")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "ar", "de", "es", "it", "cn", "ru", "zh"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_indices_trading_menu(d, cur_language, cur_country, main_page_link)

        test_element = MainBannerTryDemo(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    @pytest.mark.test_03
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade] in Most traded block
        Language: EN, AR, DE, ES, IT, CN, RU, ZH. License: All (Except: FCA).
        """

        test_title = ("11.02.06", "Education > Menu item [Indices Trading]",
                      ".00_03", "Testing button [Trade] in Most traded block")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "ar", "de", "es", "it", "cn", "ru", "zh"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_indices_trading_menu(d, cur_language, cur_country, main_page_link)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link)

    @allure.step("Start test of button [1. Create & verify your account] in Block 'Steps trading'")
    @pytest.mark.test_04
    def test_04_create_and_verify_your_account_button_in_block_steps_trading(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create & verify your account] in block 'Steps trading'
        Language: EN, AR, DE, ES, IT, CN, RU, ZH. License: All.
        """

        test_title = ("11.02.06", "Education > Menu item [Indices Trading]",
                      ".00_04", "Testing button [1. Create & verify your account] in Block 'Steps trading'")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role, *test_title)

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["", "ar", "de", "es", "it", "cn", "ru", "zh"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_indices_trading_menu(d, cur_language, cur_country, main_page_link)

        test_element = BlockStepTrading(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link)

    @allure.step("Start test of button in block [Vertical banner]")
    @pytest.mark.test_11
    def test_11_block_vert_banner_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
                Check the [Button] on the Vertical side banner at the bottom of the page.
                Language: DE, ES, ZH. License: All.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.06", "Education > Menu item [Indices Trading]",
            ".00_11", "Testing button in block [Vertical banner]")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["de", "es", "zh"])

        # test_element.arrange_0()
        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # банеры должны открываться в Demo mode for US_00
        banner00_ver_tpd = []
        # банеры должны открываться в Live mode for US_00
        banner00_ver_tp = ['166', '196', '425']
        # банеры должны открываться в Demo mode for US_01
        banner01_ver_tpd = []
        # банеры должны открываться в Live mode for US_01
        banner01_ver_tp = []

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_indices_trading_menu(d, cur_language, cur_country, main_page_link)

        test_element = ButtonOnVerticalBanner(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link, banner00_ver_tpd,
                                        banner00_ver_tp, banner01_ver_tpd, banner01_ver_tp)

    @allure.step("Start test of button in block [Horizontal banner]")
    @pytest.mark.test_12
    def test_12_block_hor_banner_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check the [Button] on the Horizontal banner at the bottom of the page.
        Language: AR, DE, ES, IT, RU, ZH. License: All.
        For "Authorized user" role:
        The trading platform page is opened depend on the banner [type-id]:
                Live mode if the banner in the Live mode banners list
                Demo mode if the banner in the Demo mode banners list
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.06", "Education > Menu item [Indices Trading]",
            ".00_12", "Testing button in block [Horizontal banner]")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(
            cur_language, ["ar", "de", "es", "it", "ru", "zh"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        # банеры должны открываться в Demo mode for US_00
        banner00_hor_tpd = ['197']
        # банеры должны открываться в Live mode for US_00
        banner00_hor_tp = ['103', '167', '252', '390', '428']
        # банеры должны открываться в Demo mode for US_01
        banner01_hor_tpd = []
        # банеры должны открываться в Live mode for US_01
        banner01_hor_tp = []

        page_menu = MenuSection(d, main_page_link)
        cur_menu_link = page_menu.open_education_indices_trading_menu(d, cur_language, cur_country, main_page_link)

        test_element = ButtonOnHorizontalBanner(d, cur_menu_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, cur_menu_link,
                                        banner00_hor_tpd, banner00_hor_tp, banner01_hor_tpd, banner01_hor_tp)

    @allure.step("Start pretest")
    def test_99_indices_trading_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        global count
        global cur_page_url

        build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "11.02.06", "Education > Menu item [Indices Trading]",
            ".00_99", "Pretest for US_11.02.06.01")

        if count == 0:
            pytest.skip("Так надо")

        Common().check_country_in_list_and_skip_if_present(cur_country, ["gb"])
        Common().skip_if_eng_lang_and_fca_license(cur_language, cur_country)
        Common().check_language_in_list_and_skip_if_not_present(cur_language, ["", "de", "es", "it", "ru", "zh"])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, main_page_link)
        page_menu.open_education_indices_trading_menu(d, cur_language, cur_country, main_page_link)

        file_name = "tests/US_11_Education/US_11-02-06_Indices_trading/list_of_href.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)

        Common().creating_file_of_hrefs("Indices trading", list_items, file_name)

        count -= 1

    # "------------------------------------"

    # @allure.step("Start pretest")
    # def test_indices_trading_guide_pretest(self, worker_id, d, cur_language, cur_country, cur_role, cur_login,
    #                                        cur_password, prob_run_tc):
    #     test_title = ("11.02.06", "Educations > Menu item [Indices Trading]", "00", "Pretest")
    #
    #     global first_run_pretest
    #
    #     logger.info(f"====== START testing {', '.join(test_title)} ======")
    #
    #     link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc, *test_title)
    #
    #     if not first_run_pretest:
    #         logger.info("Skip the pretest, since we've already passed it before.")
    #         logger.info(f"====== SKIP testing {', '.join(test_title)} ======")
    #         pytest.skip("Skip the pretest, since we've already passed it before.")
    #
    #     if cur_language not in ["", "ar", "de", "es", "it", "ch"]:
    #         logger.info(f"Test section released not for '{cur_language}' language.")
    #         logger.info(f"====== SKIP testing {', '.join(test_title)} ======")
    #         pytest.skip(f"Test section released not for '{cur_language}' language.")
    #
    #     page_conditions = Conditions(d, "")
    #     page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language, cur_country)
    #     page_menu.sub_menu_indices_trading_move_focus_click(d, cur_language)
    #
    #     name_file = "tests/US_11_Education/US_11-02-06_Indices_trading/list_of_href.txt"
    #
    #     list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)
    #
    #     href_list = list()
    #     if len(list_items) > 0:
    #         href_list = list(map(lambda element: element.get_property("href"), list_items))
    #     else:
    #         href_list.append(d.current_url)
    #
    #     count_all = len(href_list)
    #     logger.info(f"Indices Trading Guide include {count_all} items on selected "
    #                 f"'{'en' if cur_language == '' else cur_language}' language")
    #     logger.info("Choose no more than 3 random items")
    #     random_list = random.sample(href_list, 3 if count_all >= 3 else count_all)
    #     with open(name_file, "w", encoding='UTF-8') as f:
    #         for val in random_list:
    #             f.write(val + "\n")
    #             logger.info(f"The element '{val}' has been added to the file")
    #     logger.info(f"Test data include {len(random_list)} Indices Trading Guide item(s)")
    #     logger.info(f"The probability of test coverage = {len(random_list) / count_all * 100} %")
    #     first_run_pretest = False
    #
    #     logger.info(f"====== END testing {', '.join(test_title)} ======")
