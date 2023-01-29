import time
from selenium.webdriver.common.action_chains import ActionChains
import allure
from selenium.webdriver.support import expected_conditions as ec
from Locators.electronics_locators import locators
from selenium.webdriver.support.wait import WebDriverWait


class ElectronicsPage:
    """
    it contains some method related to the electronics page
    """

    @allure.step('initializing the driver and another object')
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    @allure.step('Launching the web url')
    def open_target_page(self, url):
        self.driver.get(url)

    @allure.step('closing the login popup by clicking  cross icon')
    def close_the_login_popup(self):
        try:
            self.wait.until(ec.visibility_of_element_located(locators.pop_up_cross_icon))
            self.driver.find_element(*locators.pop_up_cross_icon).click()
            self.driver.refresh()
        except Exception as e:
            print('login pop up not found at moment', e)

    @allure.step('Clicking on banner')
    def click_on_banner(self):
        try:
            time.sleep(2)
            self.wait.until(ec.element_to_be_clickable(locators.banner))
            self.driver.find_element(*locators.banner).click()
        except Exception as e:
            print('Failed to clicking on banner', e)

    @allure.step('hover the mouse on electronics_section')
    def mouse_hover_on_electronics_section(self):
        element = self.driver.find_element(*locators.electronics_XPATH)
        self.action.move_to_element(element).perform()

    @allure.step("Getting text from web elements")
    def get_mobileBrandTextList_from_webElementList(self):
        self.wait.until(ec.visibility_of_all_elements_located(locators.all_mobile_brands_Xpath))
        for element in range(len(self.driver.find_elements(*locators.all_mobile_brands_Xpath))):
            text = self.driver.find_elements(*locators.all_mobile_brands_Xpath)[element].text
            print("{}. {}".format(element + 1, text))
