from playwright.sync_api import Page, expect


class SearchProductPage:

    def __init__(self, page: Page):

        self.page = page
        self.__submit_products_btn = self.page.locator('[href="/products"]')
        self.__searched_products_txt = self.page.locator('[class="title text-center"]')
        self.__searched_products_list = self.page.locator('[class="features_items"]')
        self.__first_product_details_page = self.page.locator('[href="/product_details/1"]')
        self.__product_details_info = self.page.locator('[class="product-information"]')
        self.__search_field = self.page.locator('input[class="form-control input-lg"]')
        self.__search_btn = self.page.locator('button[id="submit_search"]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def products_btn_click(self) -> None:
        self.__submit_products_btn.click()

    def verify_products_page(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/products')

    def search_product(self, product) -> None:
        self.__search_field.type(product)
        self.__search_btn.click()

    def verify_searched_products_txt_visible(self) -> None:
        expect(self.__searched_products_txt).to_have_text('Searched Products')
        expect(self.__searched_products_txt).to_be_visible()

    def verify_searched_products_visible(self) -> None:
        expect(self.__searched_products_list).to_be_visible()
