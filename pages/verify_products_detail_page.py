from playwright.sync_api import Page, expect


class VerifyProductsDetailPage:

    def __init__(self, page: Page):

        self.page = page
        self.__submit_products_btn = self.page.locator('[href="/products"]')
        self.__all_products_txt = self.page.locator('[class="title text-center"]')
        self.__all_products_list = self.page.locator('[class="features_items"]')
        self.__first_product_details_page = self.page.locator('[href="/product_details/1"]')
        self.__product_details_info = self.page.locator('[class="product-information"]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def products_btn_click(self) -> None:
        self.__submit_products_btn.click()

    def verify_all_products_page(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/products')
        expect(self.__all_products_txt).to_have_text('All Products')
        expect(self.__all_products_txt).to_be_visible()

    def verify_all_products_visible(self) -> None:
        expect(self.__all_products_list).to_be_visible()

    def first_product_details_click(self) -> None:
        self.__first_product_details_page.click()

    def check_product_details_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/product_details/1')

    def check_products_details_info(self) -> None:
        expect(self.__product_details_info).to_contain_text('Blue Top')
        expect(self.__product_details_info).to_contain_text('Category:')
        expect(self.__product_details_info).to_contain_text('Rs. 500')
        expect(self.__product_details_info).to_contain_text('Availability:')
        expect(self.__product_details_info).to_contain_text('Condition:')
        expect(self.__product_details_info).to_contain_text('Brand:')
