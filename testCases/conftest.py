import pytest, platform
from selenium import webdriver as wb
from testConfig import settings

_browser = settings.browser if settings.browser else "chrome"
if _browser == "chrome":
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
elif _browser == "firefox":
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def launch_browser(request):
    _driver = None
    if _browser == "chrome":
        options = wb.ChromeOptions()
        if platform.system() == "Linux":
            options.add_argument('--headless')
        #_driver = wb.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        service = Service(r"seleniumDrivers/chromedriver.exe")
        _driver = wb.Chrome(service=service, options=options)
        _driver.set_window_size(1920, 1080)
    elif _browser == "firefox":
        options = Options()
        if platform.system() == "Linux":
            options.headless = True
        #_driver = wb.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        service = Service(r"seleniumDrivers/geckodriver.exe")
        _driver = wb.Chrome(service=service, options=options)

    _driver.maximize_window()
    _driver.implicitly_wait(20)
    _driver.get(settings.url)
    request.cls.driver = _driver

    yield
    _driver.close()
