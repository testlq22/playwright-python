import pytest

from pages.remove_products_page import RemoveProducts
from utils.test_data import Data


class TestRemoveProducts:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.removeProducts = RemoveProducts(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
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
