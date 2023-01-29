import pytest
from Pages.electronics_page import ElectronicsPage
from ConfigurationData.config import config_data


@pytest.mark.usefixtures("setup")
class TestElectronics:
    """
    it contains tests related to Electronics items
    """

    def test_getting_the_mobile_brand_list_from_electronics_section(self):
        """
        Gating the mobile brands name which is available on flipkart
        :return: mobile brands name in proper format
        """
        electronics_driver = ElectronicsPage(driver=self.driver)
        electronics_driver.open_target_page(url=config_data['flipkart_url'])
        electronics_driver.close_the_login_popup()
        electronics_driver.click_on_banner()
        electronics_driver.mouse_hover_on_electronics_section()
        electronics_driver.get_mobileBrandTextList_from_webElementList()
