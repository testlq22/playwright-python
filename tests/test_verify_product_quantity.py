import pytest

from pages.verify_product_quantity_page import VerifyProductQuantity
from utils.test_data import Data


class TestVerifyTestCases:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.verProductQuant = VerifyProductQuantity(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.verProductQuant.check_page_loaded()
        self.verProductQuant.third_product_details_click()
        self.verProductQuant.check_product_details_page_loaded()
        self.verProductQuant.set_quantity(Data.quantity)
        self.verProductQuant.add_to_cart_click()
        self.verProductQuant.click_view_cart()
        self.verProductQuant.check_product_3_quantity_info(Data.quantity)
