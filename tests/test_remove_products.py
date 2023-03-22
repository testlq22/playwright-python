import pytest

from pages.remove_products_page import RemoveProducts
from utils.test_data import Data
from utils.tools import take_screenshot


class TestRemoveProducts:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.removeProducts = RemoveProducts(self.page)

    def test_remove_products(self, test_setup):
        self.removeProducts.check_page_loaded()
        self.removeProducts.products_btn_click()
        self.removeProducts.hover_product_1()
        self.removeProducts.add_first_product()
        self.removeProducts.click_continue_shopping()
        self.removeProducts.hover_product_2()
        self.removeProducts.add_second_product()
        self.removeProducts.click_continue_shopping()
        self.removeProducts.click_cart_button()
        self.removeProducts.check_cart_page_loaded()
        self.removeProducts.verify_product_1_visible()
        self.removeProducts.verify_product_2_visible()
        self.removeProducts.del_product_1()
        self.removeProducts.del_product_2()
        self.removeProducts.verify_product_1_not_visible(Data.id1)
        self.removeProducts.verify_product_2_not_visible(Data.id2)
        take_screenshot(self.page, 'remove_products')
