"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""
import sys
import os
from datetime import datetime
import re
import platform

import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from allure_commons.types import AttachmentType

import conf


def pytest_addoption(parser):
    # проверка аргументов командной строки
    parser.addoption('--retest', action='store', default=False,
                     help="Re-Testing: '--retest=True'")

    parser.addoption('--browser_name', action='store', default=False,
                     help="Choose browser: '--browser_name=Chrome' or '--browser_name=Edge'")

    parser.addoption('--lang', action='store', default=False,
                     help="Choose language: '--lang='en' for 'en'")

    parser.addoption('--country', action='store', default=False,
                     help="Choose License: '--country=ae'")

    parser.addoption('--role', action='store', default=False,
                     help="Choose Role: --role=NoAuth'")

    parser.addoption('--tpi_link', action='store', default=False,
                     help="cur_item_link: '--tpi_link=https://capital.com/fr/trading-amazon'")

    parser.addoption('--os', action='store', default=False,
                     help="os: '--os=U22'")


"""
пример командной строки для автотестов: --retest=True --browser_name=Chrome --lang='' --country=ae --role=Auth
    --tpi_link=https://capital.com/fr/trading-amazon --os=U22 -m test_02 --no-summary -v
    tests/US_11_Education/US_11-02-02_Shares_trading/US_11-02-02-01_Shares_trading_test.py
#########  
пример командной строки для тестов:--browser_name=Chrome --lang='en' --country=ae --role=Auth --os=U22 
-m test_02 --no-summary -vs tests/US_11_Education/US_11-02-02_Shares_trading/US_11-02-02-01_Shares_trading_test.py
!!! порядок расположение аргументов не имеет значения
"""

role_list = list()
input_list = sys.argv
search_value = "--role"
pattern = re.compile(f'{search_value}=(\\S+)')

for item in input_list:
    match = pattern.search(item)
    if match:
        role_list = (match.group(1),)
        break
else:
    role_list = (
        "NoReg",
        "Auth",
        "NoAuth",  # "Reg/NoAuth"
    )


@pytest.fixture(
    scope="class",
    params=[*role_list],
)
def cur_role(request):
    """Fixture"""
    # проверка аргументов командной строки
    cur_role = request.param
    print(f"Current test role - {cur_role}\n")
    return cur_role


# Language parameter
@pytest.fixture(
    scope="class",
    params=[
        # "",  # "en" - 21 us
        # "ar",  # 8 us
        # "de",  # 15 us
        # "es",  # 20 us
        "it",  # 15 us
        # "ru",  # 15 us
        # "cn",  # 13 us Education to trade present, financial glossary not present
        # "zh",  # 12 us
        # "fr",  # 11 us
        # "pl",  # 10 us
        # "ro",  # 10 us
        # "nl",  # 8 us
        # "el",  # 5 us
        # "hu",  # 5 us Magyar
    ],
)
def cur_language(request):
    """Fixture"""
    # проверка аргументов командной строки
    if request.config.getoption("lang"):
        if request.config.getoption("lang") == "en":
            language = ""
        else:
            language = request.config.getoption("lang")
    else:
        language = request.param
    print(f"Current test language - {"en" if language == "" else language}")
    return language


# Country/License parameter
@pytest.fixture(
    scope="class",
    params=[
        # "gb",  # Great Britain - "FCA"
        # "de",  # Germany  - "CYSEC"
        # "au",  # Australia - "ASIC"
        "ae",  # United Arab Emirates - "SCB"
        #
        # "gr",  # Greece - "CYSEC"
        # "es",  # Spain - "CYSEC"
        # "fr",  # France - "CYSEC"
        # "it",  # Italy - "CYSEC"
        # "hu",  # Hungary - "CYSEC"
        # "nl",  # Netherlands - "CYSEC"
        # "pl",  # Poland - "CYSEC"
        # "ro",  # Romania - "CYSEC"
        # "tw",  # Taiwan - "SCB"
        # "hk",  # Hong Kong - "SCB"

        # # "ru" - not support
        # "NBRB" - not support
        # "SFB",
        # "FSA"
    ],
)
def cur_country(request):
    """Fixture"""
    # проверка аргументов командной строки
    if request.config.getoption("country"):
        country = request.config.getoption("country")
    else:
        country = request.param
    print(f"Current country of trading - {country}")
    return country


@pytest.fixture(
    scope="class",
    params=[
        "test001.miketar+1@gmail.com"
        # "aqa.tomelo.an@gmail.com"  # для локального тестирования у Саши
    ],
)
def cur_login(request):
    """Fixture"""
    print(f"Current login - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "Qwer1234-!@#$"
        # "iT9Vgqi6d$fiZ*Z"  # для локального тестирования у Саши
    ],
)
def cur_password(request):
    """Fixture"""
    print(f"Current password - {request.param}")
    return request.param


@pytest.fixture(
    scope="session",
    params=[
        # 'W22',
        # 'W10',
        # 'W11',
        # 'M14',
        'U22',

    ],
)
def cur_os(request):
    """Fixture"""
    # проверка аргументов командной строки
    if request.config.getoption("os"):
        test_os = request.config.getoption("os")
    else:
        test_os = request.param
    # os_info = platform.system()
    # os_version = platform.version()
    platform_v = platform.platform()
    print(f"Current OS - {platform_v}")
    return test_os


@pytest.fixture(
    scope="session",
    params=[
        True,
        # False
    ],
)
def cur_headless(request):
    """Fixture"""
    print(f"Current Headless - {request.param}")
    return request.param


@pytest.fixture(
    # scope="module",
    scope="session",
    params=[
        "Chrome",
        # "Edge",
        # "Firefox",
        # "Safari",
    ],
    autouse=True,
    # ids=pre_go,
)
def d(request):
    """WebDriver Initialization"""
    print(f'\n{datetime.now()}   *** autouse fixture {request.param} ***\n')

    # проверка аргументов командной строки
    if request.config.getoption("browser_name"):
        test_browser = request.config.getoption("browser_name")
    else:
        test_browser = request.param

    d = None
    if test_browser == "Chrome":
        d = init_remote_driver_chrome()
        # d = init_remote_driver_chrome_v2(cur_headless)
    elif test_browser == "Edge":
        d = init_remote_driver_edge()
    elif test_browser == "Firefox":
        d = init_remote_driver_firefox()
    elif test_browser == "Safari":
        d = init_remote_driver_safari()
    elif test_browser == "Opera":
        pass
    else:
        print(f'Please pass the correct browser name: {test_browser}')
        raise Exception('driver is not found')
    print(f'Current browser name: {d.capabilities['browserName']}')
    # Установка максимального тайм-аута загрузки страницы
    d.set_page_load_timeout(60)
    yield d

    d.quit()
    print(f"\n{datetime.now()}   *** end fixture Browser = teardown ***\n")


def init_remote_driver_chrome():
    # chrome_version = "114.0.5735.90"
    # chrome_version = "115.0.5790.102" - версия chromium CFT
    # chrome_version = "115.0.5790.114"
    # chrome_version = "116.0.5845.96"
    chrome_options = webdriver.ChromeOptions()

    chrome_options.page_load_strategy = "normal"
    # chrome_options.page_load_strategy = "eager"

    chrome_options.add_argument(conf.CHROME_WINDOW_SIZES)
    # chrome_options.add_argument(conf.CHROME_WINDOW_SIZES_4k)

    # Код, отмены информационного сообщения "USB: usb_device_handle_win.cc"
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--accept-lang=en")

    # !!!
    # безголовый режим задается переменной headless в самом начале текущего модуля
    if conf.HEADLESS:
        chrome_options.add_argument(conf.CHROMIUM_HEADLESS)

    # chrome_options.add_argument("--disable-browser-side-navigation")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-gpu")

    # driver = webdriver.Chrome(executable_path='/home/trendsen/virtualenv/GoogleTrendsBOT/3.8/bin/chromedriver',
    #                           options=options)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    # driver = webdriver.Chrome(
    #     service=ChromeService(ChromeDriverManager(version=chrome_version).install()), options=chrome_options
    # )

    print(driver.get_window_size())
    driver.implicitly_wait(1)
    driver.set_script_timeout(20000)

    return driver


def init_remote_driver_chrome_v2(headless):
    chrome_options = webdriver.ChromeOptions()

    chrome_options.page_load_strategy = "normal"

    chrome_options.add_argument(conf.CHROME_WINDOW_SIZES)

    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--accept-lang=en")

    # !!!
    # безголовый режим задается переменной headless в самом начале текущего модуля
    if headless:
        chrome_options.add_argument(conf.CHROMIUM_HEADLESS)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    print(driver.get_window_size())
    driver.implicitly_wait(1)
    driver.set_script_timeout(20000)
    return driver


def init_remote_driver_edge():
    edge_options = webdriver.EdgeOptions()

    edge_options.page_load_strategy = 'normal'
    # edge_options.page_load_strategy = "eager"

    # edge_options.add_argument(conf.WINDOW_SIZES)
    edge_options.add_argument(conf.CHROMIUM_WINDOW_WIDTH)
    edge_options.add_argument(conf.CHROMIUM_WINDOW_HEIGHT)

    # !!!
    # безголовый режим браузера задается переменной headless, задаваемой в самом начале
    if conf.HEADLESS:
        edge_options.add_argument(conf.CHROMIUM_HEADLESS)

    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)

    print(driver.get_window_size())
    driver.implicitly_wait(5)

    return driver


def init_remote_driver_firefox():
    firefox_options = webdriver.FirefoxOptions()

    firefox_options.page_load_strategy = 'normal'
    # firefox_options.page_load_strategy = "eager"

    firefox_options.add_argument(conf.FIREFOX_WINDOW_WIDTH)
    firefox_options.add_argument(conf.FIREFOX_WINDOW_HEIGHT)

    # !!!
    # безголовый режим браузера задается переменной headless
    if conf.HEADLESS:
        firefox_options.add_argument("--headless")  # ?похоже, не работает на MacOS
    ser = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=ser, options=firefox_options)

    print(driver.get_window_size())
    driver.implicitly_wait(5)
    return driver


def init_remote_driver_safari():
    # !!!
    # Safari не поддерживает Headless

    driver = webdriver.Safari()
    driver.set_window_size(*conf.SAFARI_WINDOW_SIZES)

    print(driver.get_window_size())
    driver.implicitly_wait(5)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        feature_request = item.funcargs["request"]
        driver = feature_request.getfixturevalue("d")
        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            # Добавлен скриншот для пропущенных тестов
            # if (report.skipped and xfail) or (report.failed and not xfail) or (report.skipped and not xfail):
            report_dir = os.path.dirname(item.config.option.htmlpath)
            len_dir = len(os.path.dirname(item.nodeid))
            file_name = report.nodeid[len_dir:].replace("::", "_")[1:] + ".png"
            destination_file = os.path.join(report_dir, file_name)

            def s(x):
                return driver.execute_script(
                    "return document.body.parentNode.scroll" + x)

            # driver.set_window_size(s("Width"), s("Height"))
            # driver.find_element(By.TAG_NAME, "body").screenshot(destination_file)
            driver.save_screenshot(destination_file)  # необходимо для корректной работы ретестов
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=AttachmentType.PNG,
            )
            if file_name:
                html = \
                    ('<div><img src="%s" alt="screenshot" style="width:300px;height:200px" '
                     'onclick="window.open(this.src)" align="right"/></div>' % file_name)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "REPORT"
