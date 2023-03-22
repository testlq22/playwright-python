import pytest

from pages.verify_product_quantity_page import VerifyProductQuantity
from utils.test_data import Data
from utils.tools import take_screenshot


class TestVerifyProductQuantity:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.verProductQuant = VerifyProductQuantity(self.page)

    def test_verify_product_quantity(self, test_setup):
        self.verProductQuant.check_page_loaded()
        self.verProductQuant.third_product_details_click()
        self.verProductQuant.check_product_details_page_loaded()
        self.verProductQuant.set_quantity(Data.quantity)
        self.verProductQuant.add_to_cart_click()
        self.verProductQuant.click_view_cart()
        self.verProductQuant.check_product_3_quantity_info(Data.quantity)
        take_screenshot(self.page, 'verify_product_quantity')
