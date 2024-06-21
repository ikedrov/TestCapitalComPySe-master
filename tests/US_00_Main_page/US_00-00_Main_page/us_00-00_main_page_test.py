"""
-*- coding: utf-8 -*-
@Time    : 2024/02/25 08:50 GMT+3
@Author  : Artem Dashkov
"""

import allure
import pytest

from pages.common import Common
from pages.Elements.ExploreOurPlatformBlockEasyToUseLink import ExploreOurPlatformBlockEasyToUseLink
from pages.Elements.ExploreOurPlatformBlockTryNowButton import ExploreOurPlatformBlockTryNowButton
from pages.Elements.FindUsOnTradingviewBannerExploreFeaturesButton import FindUsOnTradingviewBannerExploreFeaturesButton
from pages.Elements.ForLearnerTradersBlockTryDemoButton import ForLearnerTradersBlockTryDemoButton
from pages.Elements.ForLearnerTradersBlockSignUpButton import ForLearnerTradersBlockSignUpButton
from pages.Elements.GetInvolvedBannerPracticeForFreeButtonV2 import GetInvolvedBannerPracticeForFreeButtonV2
from pages.Elements.GetInvolvedBannerTradeNowButton import GetInvolvedBannerTradeNowButton
from pages.Elements.GetInvolvedBannerTradeNowButtonV2 import GetInvolvedBannerTradeNowButtonV2
from pages.Elements.GetInvolvedBannerTryFreeDemoButton import GetInvolvedBannerTryFreeDemoButton
from pages.Elements.IndustryLeadingSupportBannerPracticeForFreeButtonV2 import IndustryLeadingSupportBannerPracticeForFreeButtonV2
from pages.Elements.IndustryLeadingSupportBannerStartTradingButtonV2 import IndustryLeadingSupportBannerStartTradingButtonV2
from pages.Elements.MainBannerSignUpButtonMainPage import MainBannerSignUpButtonMainPage
from pages.Elements.MainBannerTryDemoButtonMainPage import MainBannerTryDemoButtonMainPage
from pages.Elements.OurAppsBlockDownloadOnTheAppStoreButton import OurAppsBlockDownloadOnTheAppStoreButton
from pages.Elements.OurAppsBlockGetItOnGooglePlayButton import OurAppsBlockGetItOnGooglePlayButton
from pages.Elements.OurMarketsTableBuyButton import BuyButtonOurMarketsTable
from pages.Elements.OurMarketsTableSellButton import SellButtonOurMarketsTable
from pages.Elements.StepTradingBlock import BlockStepTrading
from pages.Elements.TradeCFDsBlock import TradeCFDsBlock
from pages.Elements.TradingCalculatorStartTradingButton import TradingCalculatorStartTradingButton
from pages.Elements.TradersDashboardWidgetTradeButton import TradersDashboardWidgetTradeButton
from pages.Elements.TradingExperienceStartTradingButton import TradingExperienceStartTradingButton
from pages.Elements.TradingForFreeBlockCreateDemoAccountButton import TradingForFreeBlockCreateDemoAccountButton
from pages.Elements.TradingInstrumentTradeButton import TradingInstrumentTradeButton
from pages.Elements.WhyChooseBlockTryDemoButton import WhyChooseBlockTryDemoButton
from pages.Elements.WhyChooseBlockTryNowButton import WhyChooseBlockTryNowButton
from pages.Elements.WhyChooseBlockSignUpButton import WhyChooseBlockSignUpButton
from src.src import CapitalComPageSrc
from pages.build_dynamic_arg import build_dynamic_arg_v4
from pages.conditions_new import NewConditions
from pages.conditions import Conditions


@pytest.mark.us_00_00
class TestMainPage:
    page_conditions = None

    @allure.step("Start test of button [Try demo] in Block 'Helping traders make better decisions'")
    @pytest.mark.test_101
    def test_101_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try Demo] in Block 'Helping traders make better decisions' Main Page
        Language: EN. License: FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_101", "Testing button [Try Demo] in Block 'Helping traders make better decisions' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemoButtonMainPage(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Sign Up] in Block 'Helping traders make better decisions'")
    @pytest.mark.test_102
    def test_102_main_banner_sign_up_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Sign Up] in Block 'Helping traders make better decisions' Main Page
        Language: EN. License: FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_102", "Testing button [Sign Up] in Block 'Helping traders make better decisions' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerSignUpButtonMainPage(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Try demo] in Block 'Why choose Capital.com'")
    @pytest.mark.test_103
    def test_103_why_choose_block_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try Demo] in Block 'Why choose Capital.com?' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_103", "Testing button [Try Demo] in Block 'Why choose Capital.com?' Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_103", "Testing button [Try Demo] in Block 'Why choose Capital.com?' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = WhyChooseBlockTryDemoButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Sign Up] in Block 'Why choose Capital.com'")
    @pytest.mark.test_104
    def test_104_why_choose_block_sign_up_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Sign Up] in Block 'Why choose Capital.com' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_104", "Testing button [Sign Up] in Block 'Why choose Capital.com' Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_104", "Testing button [Sign Up] in Block 'Why choose Capital.com' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = WhyChooseBlockSignUpButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Sell] in Block 'Our markets'")
    @pytest.mark.test_105
    def test_105_our_markets_block_sell_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_market, instrument):
        """
        Check: Button [Sell] in Block 'Our markets' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_105",
        #               f"Testing button [Sell] in Block 'Our markets' {market} market, {instrument} instrument")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_105",
            f"Testing button [Sell] in Block 'Our markets' '{cur_market}' market, '{instrument}' instrument",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])
        Common().check_market_in_list_and_skip_if_present(cur_market, [
            'Cryptocurrencies', 'Commodities', 'Shares', 'Forex'
        ])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonOurMarketsTable(d, main_page_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, main_page_link, cur_market, instrument)

    @allure.step("Start test of button [Buy] in Block 'Our markets'")
    @pytest.mark.test_106
    def test_106_our_markets_block_buy_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_market, instrument):
        """
        Check: Button [Buy] in Block 'Our markets' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_106",
        #               f"Testing button [Buy] in Block 'Our markets' {market} market, {instrument} instrument")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_106",
            f"Testing button [Buy] in Block 'Our markets' '{cur_market}' market, '{instrument}' instrument",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])
        Common().check_market_in_list_and_skip_if_present(cur_market, [
            'Cryptocurrencies', 'Commodities', 'Shares', 'Forex'
        ])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonOurMarketsTable(d, main_page_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, main_page_link, cur_market, instrument)

    @allure.step("Start test of button [Try demo] in Block 'For learner traders'")
    @pytest.mark.test_107
    def test_107_for_learner_traders_block_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try Demo] in Block 'For learner traders' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_107", "Testing button [Try Demo] in Block 'For learner traders' Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_107", "Testing button [Try Demo] in Block 'For learner traders' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ForLearnerTradersBlockTryDemoButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Sign Up] in Block 'For learner traders'")
    @pytest.mark.test_108
    def test_108_for_learner_traders_block_sign_up_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Sign Up] in Block 'For learner traders' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_108", "Testing button [Sign Up] in Block 'For learner traders' Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_108", "Testing button [Sign Up] in Block 'For learner traders' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ForLearnerTradersBlockSignUpButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [1. Create your account] in Block 'Ready to join a leading broker?'")
    @pytest.mark.test_109
    def test_109_create_your_account_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create your account] in Block 'Ready to join a leading broker?' Main Page
        Language: EN. License: FCA.
        """
        # test_title = ("00", "Main Page",
        #               ".00_109", "Testing button [1. Create your account] in Block 'Ready to join a leading broker?' "
        #                          "Main Page")

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_109", "Testing button [1. Create your account] in Block 'Ready to join a leading broker?' Main Page",
            False, True
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['gb'])

        page_conditions = NewConditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL_NEW, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Trade] in Widget 'Trading instrument'")
    @pytest.mark.test_001
    def test_001_trading_instrument_widget_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_market):
        """
        Check: Button [Trade] in Widget 'Trading instrument' Main Page
        Language: ALL. License: Not FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_001", "Start test of button [Trade] in Widget 'Trading instrument'",
            False, False
        )

        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'au', 'ae']
        )
        Common().check_market_in_list_and_skip_if_present(cur_market, [
            'Commodities', 'Indices', 'Shares', 'Forex'
        ])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradingInstrumentTradeButton(d, main_page_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, main_page_link, cur_market)

    @allure.step("Start test of button [Start trading] in 'The Capital.com trading experience' block")
    @pytest.mark.test_002
    def test_002_start_trading_in_trading_experience_block_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start trading] in 'The Capital.com trading experience' block
        Language: ALL. License: Not FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_002", "Start test of button [Start trading] in 'The Capital.com trading experience' block",
            False, False
        )

        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'au', 'ae']
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradingExperienceStartTradingButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [1. Create & verify your account] in 'Steps trading' block")
    @pytest.mark.test_003
    def test_003_create_and_verify_your_account_button_in_block_steps_trading(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [1. Create & verify your account] in 'Steps trading' block
        Language: ALL. License: Not FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_003",
            "Start test of button [1. Create & verify your account] in 'Steps trading' block",
            False, False
        )

        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'au', 'ae']
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Explore Features] in 'Trade CFDs on Capital.com via TradingView' block")
    @pytest.mark.test_005
    def test_005_explore_features_button_in_block_trade_cfds(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Explore Features] in 'Trade CFDs on Capital.com via TradingView' block
        Language: ALL. License: Not FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_005",
            "Start test of button [Explore Features] in 'Trade CFDs on Capital.com via TradingView' block",
            False, False
        )

        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'au', 'ae']
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradeCFDsBlock(d, main_page_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Create a demo account] in 'Try trading for free' block")
    @pytest.mark.test_006
    def test_006_create_demo_account_in_try_trading_for_free_block_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Create a demo account] in 'Try trading for free' block
        Language: EN. License: Not FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_006", "Start test of button [Create a demo account] in 'Try trading for free' block",
            False, False
        )

        Common().check_language_in_list_and_skip_if_not_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['de', 'au', 'ae'])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradingForFreeBlockCreateDemoAccountButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Download on the App Store] in 'Our Apps' block")
    @pytest.mark.test_008
    def test_008_download_on_the_app_store_button_in_our_apps_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Download on the App Store] in 'Our Apps' block
        Language: ALL. License: Not FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_008",
            "Start test of button [Download on the App Store] in 'Our Apps' block",
            False, False
        )

        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'au', 'ae']
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = OurAppsBlockDownloadOnTheAppStoreButton(d, main_page_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Get it on Google Play] in 'Our Apps' block")
    @pytest.mark.test_009
    def test_009_get_it_on_google_play_button_in_our_apps_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Get it on Google Play] in 'Our Apps' block
        Language: ALL. License: Not FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_009",
            "Start test of button [Get it on Google Play] in 'Our Apps' block",
            False, False
        )

        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'au', 'ae']
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = OurAppsBlockGetItOnGooglePlayButton(d, main_page_link, bid)
        test_element.full_test(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Try now] in 'Why choose Capital.com?' block")
    @pytest.mark.test_010
    def test_010_why_choose_block_try_now_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try now] in 'Why choose Capital.com?' block
        Language: ALL. License: Not FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_010", "Start test of button [Try now] in 'Why choose Capital.com?' block",
            False, False
        )

        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['de', 'au', 'ae'])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = WhyChooseBlockTryNowButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Trade] in 'Trader's Dashboard' widget")
    @pytest.mark.test_011
    def test_011_traders_dashboard_widget_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade] in 'Trader's Dashboard' widget
        Language: ALL. License: Not FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_011", "Start test of button [Trade] in 'Trader's Dashboard' widget",
            False, False
        )

        Common().check_market_in_list_and_skip_if_present(cur_language, ['', 'nl'])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['de', 'au', 'ae'])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradersDashboardWidgetTradeButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of link [easy-to-use] in 'Explore our platform' block")
    @pytest.mark.test_012
    def test_012_explore_our_platform_block_easy_to_use_link(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Link [easy-to-use] in 'Explore our platform' block
        Language: Not EN, NL. License: Not FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_012", "Start test of link [easy-to-use] in 'Explore our platform' block",
            False, False
        )

        Common().check_market_in_list_and_skip_if_present(cur_language, ['', 'nl'])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['de', 'au', 'ae'])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ExploreOurPlatformBlockEasyToUseLink(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Try now] in 'Explore our platform' block")
    @pytest.mark.test_013
    def test_013_explore_our_platform_block_try_now_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try now] in 'Explore our platform' block
        Language: Not EN, NL. License: Not FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_013", "Start test of button [Try now] in 'Explore our platform' block",
            False, False
        )

        Common().check_language_in_list_and_skip_if_present(cur_language, ['', 'nl'])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['de', 'au', 'ae'])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ExploreOurPlatformBlockTryNowButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Start Trading] in Widget 'Trading calculator'")
    @pytest.mark.test_015
    def test_015_start_trading_button_in_trading_calculator(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start Trading] in Widget 'Trading calculator' Main Page
        Language: EN. License: FCA.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_015", "Testing button [Start Trading] in Widget 'Trading calculator' Main Page",
            False, False
        )

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language,
            ['ar', 'de', 'el', 'es', 'fr', 'it', 'hu', 'pl', 'cn', 'ro', 'ru', 'zh']
        )
        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'au', 'ae']
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = TradingCalculatorStartTradingButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Trade now] in Banner 'Get involved. Become a trader_v2'")
    @pytest.mark.test_022
    def test_022_trade_now_button_in_get_involved_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade now] in Banner 'Get involved. Become a trader_v2' Main Page
        Language: EN.
        License: CYSEC, SCB.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_022", "Testing button [Trade now] in Banner 'Get involved. Become a trader_v2' Main Page",
            False, False
        )

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language,
            ['']
        )
        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'ae']
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = GetInvolvedBannerTradeNowButtonV2(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Practice for free] in Banner 'Get involved. Become a trader_v2'")
    @pytest.mark.test_023
    def test_023_practice_for_free_button_in_get_involved_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Practice for free] in Banner 'Get involved. Become a trader_v2' Main Page
        Language: EN.
        License: CYSEC, SCB.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_023", "Testing button [Practice for free] in Banner 'Get involved. Become a trader_v2' Main Page",
            False, False
        )

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language,
            ['']
        )
        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'ae']
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = GetInvolvedBannerPracticeForFreeButtonV2(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Start trading] in Banner 'Industry-leading support for new traders_v2'")
    @pytest.mark.test_024
    def test_024_start_trading_button_in_industry_leading_support_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Start trading] in Banner 'Industry-leading support for new traders_v2' Main Page
        Language: EN.
        License: CYSEC, SCB.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_024",
            "Testing button [Start trading] in Banner 'Industry-leading support for new traders_v2' Main Page",
            False, False
        )

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language,
            ['']
        )
        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'ae']
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = IndustryLeadingSupportBannerStartTradingButtonV2(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Practice for free] in Banner 'Industry-leading support for new traders_v2'")
    @pytest.mark.test_025
    def test_025_practice_for_free_button_in_industry_leading_support_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Practice for free] in Banner 'Industry-leading support for new traders_v2' Main Page
        Language: EN.
        License: CYSEC, SCB.
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_025",
            "Testing button [Practice for free] in Banner 'Industry-leading support for new traders_v2' Main Page",
            False, False
        )

        Common().check_language_in_list_and_skip_if_not_present(
            cur_language,
            ['']
        )
        Common().check_country_in_list_and_skip_if_not_present(
            cur_country,
            ['de', 'ae']
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = IndustryLeadingSupportBannerPracticeForFreeButtonV2(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Trade now] in Banner 'Get involved. Become a trader'")
    @pytest.mark.test_031
    def test_031_trade_now_button_in_get_involved_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Trade now] in Banner 'Get involved. Become a trader' Main Page
        Language: Except EN.
        License:
            CYSEC, SCB - for AR, IT
            CYSEC, ASIC, SCB - for All except AR, IT, EN
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_031", "Testing button [Trade now] in Banner 'Get involved. Become a trader' Main Page",
            False, False
        )

        Common().check_language_and_country_in_list_and_skip_if_not_present(
            cur_language,
            cur_country,
            [['de', 'el', 'es', 'fr', 'hu', 'pl', 'cn', 'ro', 'ru', 'zh'],
             ['de', 'au', 'ae']],
            [['ar', 'it'],
             ['de', 'ae']]
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = GetInvolvedBannerTradeNowButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Try free demo] in Banner 'Get involved. Become a trader'")
    @pytest.mark.test_032
    def test_032_try_free_demo_button_in_get_involved_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Try free demo] in Banner 'Get involved. Become a trader' Main Page
        Language: Except EN.
        License:
            CYSEC, SCB - for AR, IT
            CYSEC, ASIC, SCB - for All except AR, IT, EN
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_032", "Testing button [Try free demo] in Banner 'Get involved. Become a trader' Main Page",
            False, False
        )

        Common().check_language_and_country_in_list_and_skip_if_not_present(
            cur_language,
            cur_country,
            [['de', 'el', 'es', 'fr', 'hu', 'pl', 'cn', 'ro', 'ru', 'zh'],
             ['de', 'au', 'ae']],
            [['ar', 'it'],
             ['de', 'ae']]
        )

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = GetInvolvedBannerTryFreeDemoButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)

    @allure.step("Start test of button [Explore features] in Banner 'Find us on Tradingview'")
    @pytest.mark.test_033
    def test_033_explore_features_button_in_find_us_on_tradingview_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Check: Button [Explore features] in Banner 'Find us on Tradingview' Main Page
        Language: Except EN.
        License: Not FCA
        """

        bid = build_dynamic_arg_v4(
            d, worker_id, cur_language, cur_country, cur_role,
            "00", "Main Page",
            ".00_033", "Testing button [Explore features] in Banner 'Find us on Tradingview' Main Page",
            False, False
        )

        Common().check_language_in_list_and_skip_if_present(cur_language, [''])
        Common().check_country_in_list_and_skip_if_not_present(cur_country, ['de', 'au', 'ae'])

        page_conditions = Conditions(d, "")
        main_page_link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = FindUsOnTradingviewBannerExploreFeaturesButton(d, main_page_link, bid)
        test_element.full_test_with_tpi(d, cur_language, cur_country, cur_role, main_page_link)
