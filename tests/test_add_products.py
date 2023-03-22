import pytest


from pages.add_products_page import AddProducts
from utils.test_data import Data
from utils.tools import take_screenshot


class TestAddProducts:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.addProducts = AddProducts(self.page)


    def test_add_products(self, test_setup):
        self.addProducts.check_page_loaded()
        self.addProducts.products_btn_click()
        self.addProducts.hover_product_1()
        self.addProducts.add_first_product()
        self.addProducts.click_continue_shopping()
        self.addProducts.hover_product_2()
        self.addProducts.add_second_product()
        self.addProducts.click_view_cart()
        self.addProducts.verify_product_1_visible()
        self.addProducts.verify_product_2_visible()
        self.addProducts.check_product_1_details_info(Data.product1Char[0], Data.product1Char[1], Data.product1Char[2],
                                                      Data.product1Char[3])
        self.addProducts.check_product_2_details_info(Data.product2Char[0], Data.product2Char[1], Data.product2Char[2],
                                                      Data.product2Char[3])
        take_screenshot(self.page, 'add_products')
