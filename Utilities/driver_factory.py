from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        """
        this method is return a driver basis of browser
        :param browser:
        :return: driver
        """

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            options.add_argument('--ignore-certificate-errors')
            options.add_argument("--mute-audio")
            # options.add_argument("--headless")
            options.add_argument('--no-sandbox')

            return webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            options.add_argument("−−mute−audio")
            return webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()),
                                     options=options)
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            options.add_argument("−−mute−audio")

            return webdriver.Edge(service=Service(executable_path=EdgeChromiumDriverManager().install()),
                                  options=options)
        raise Exception("Provide valid driver name [ supported browser=>  chrome, firefox and edge]")
