from playwright.sync_api import Page, expect


class SearchProductsVerifyAfterLogin:

    def __init__(self, page: Page):

        self.page = page
        self.__submit_products_btn = self.page.locator('[href="/products"]')
        self.__products_txt = self.page.locator('[class="title text-center"]')
        self.__search_field = self.page.locator('input[class="form-control input-lg"]')
        self.__search_btn = self.page.locator('button[id="submit_search"]')
        self.__searched_products_list = self.page.locator('[class="features_items"]')
        self.__first_product = self.page.locator('[src="/get_product_picture/39"]')
        self.__second_product = self.page.locator('[src="/get_product_picture/40"]')
        self.__third_product = self.page.locator('[src="/get_product_picture/41"]')
        self.__add_first_product = self.page.locator('[class="overlay-content"]>[data-product-id="39"]')
        self.__continue_shopping = self.page.locator('[class="btn btn-success close-modal btn-block"]')
        self.__add_second_product = self.page.locator('[class="overlay-content"]>[data-product-id="40"]')
        self.__add_third_product = self.page.locator('[class="overlay-content"]>[data-product-id="41"]')
        self.__cart_button = self.page.locator('li>[href="/view_cart"]')
        self.__product_in_cart_1 = self.page.locator('[id="product-39"]')
        self.__product_in_cart_2 = self.page.locator('[id="product-40"]')
        self.__product_in_cart_3 = self.page.locator('[id="product-41"]')
        self.__login_submit_btn = self.page.locator('li>[href="/login"]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def products_btn_click(self) -> None:
        self.__submit_products_btn.click()

    def verify_products_page(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/products')

    def verify_products_txt_visible(self, text) -> None:
        expect(self.__products_txt).to_have_text(text)
        expect(self.__products_txt).to_be_visible()

    def search_product(self, product) -> None:
        self.__search_field.type(product)
        self.__search_btn.click()

    def verify_searched_products_visible(self) -> None:
        expect(self.__searched_products_list).to_be_visible()

    def hover_product_1(self) -> None:
        self.__first_product.hover()

    def hover_product_2(self) -> None:
        self.__second_product.hover()

    def hover_product_3(self) -> None:
        self.__third_product.hover()

    def add_first_product(self) -> None:
        self.__add_first_product.click()

    def click_continue_shopping(self) -> None:
        self.__continue_shopping.click()

    def add_second_product(self) -> None:
        self.__add_second_product.click()

    def add_third_product(self) -> None:
        self.__add_third_product.click()

    def click_cart_button(self) -> None:
        self.__cart_button.click()

    def verify_product_1_visible(self) -> None:
        expect(self.__product_in_cart_1).to_be_visible()

    def verify_product_2_visible(self) -> None:
        expect(self.__product_in_cart_2).to_be_visible()

    def verify_product_3_visible(self) -> None:
        expect(self.__product_in_cart_3).to_be_visible()

    def login_submit_btn_click(self) -> None:
        self.__login_submit_btn.click()
