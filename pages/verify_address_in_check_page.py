from playwright.sync_api import Page, expect


class VerifyAddressInCheckout:

    def __init__(self, page: Page):

        self.page = page

        self.__first_product = self.page.locator('[src="/get_product_picture/1"]')
        self.__second_product = self.page.locator('[src="/get_product_picture/2"]')
        self.__add_first_product = self.page.locator('[class="overlay-content"]>[data-product-id="1"]')
        self.__continue_shopping = self.page.locator('[class="btn btn-success close-modal btn-block"]')
        self.__add_second_product = self.page.locator('[class="overlay-content"]>[data-product-id="2"]')
        self.__header_cart_btn = self.page.locator('li>[href="/view_cart"]')
        self.__cart_with_products = self.page.locator('[id="cart_info"]')
        self.__proceed_to_checkout_btn = self.page.locator('[class="btn btn-default check_out"]')
        self.__register_login_btn = self.page.locator('[class="text-center"]>[href="/login"]')
        self.__delivery_address = self.page.locator('[id="address_delivery"]')
        self.__billing_address = self.page.locator('[id="address_invoice"]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def hover_product_1(self) -> None:
        self.__first_product.hover()

    def hover_product_2(self) -> None:
        self.__second_product.hover()

    def add_first_product(self) -> None:
        self.__add_first_product.click()

    def click_continue_shopping(self) -> None:
        self.__continue_shopping.click()

    def add_second_product(self) -> None:
        self.__add_second_product.click()

    def click_header_cart_btn(self) -> None:
        self.__header_cart_btn.click()

    def check_cart_displayed(self) -> None:
        self.__cart_with_products.is_visible()

    def click_proceed_btn(self) -> None:
        self.__proceed_to_checkout_btn.click()

    def click_register_login_btn(self) -> None:
        self.__register_login_btn.click()

    def check_delivery_address(self, firstname, lastname, company, address1, address2, country, state, city, zipcode, mobilenumber) -> None:
        expect(self.__delivery_address).to_contain_text(firstname)
        expect(self.__delivery_address).to_contain_text(lastname)
        expect(self.__delivery_address).to_contain_text(company)
        expect(self.__delivery_address).to_contain_text(address1)
        expect(self.__delivery_address).to_contain_text(address2)
        expect(self.__delivery_address).to_contain_text(country)
        expect(self.__delivery_address).to_contain_text(state)
        expect(self.__delivery_address).to_contain_text(city)
        expect(self.__delivery_address).to_contain_text(zipcode)
        expect(self.__delivery_address).to_contain_text(mobilenumber)

    def check_billing_address(self, firstname, lastname, company, address1, address2, country, state, city, zipcode, mobilenumber) -> None:
        expect(self.__billing_address).to_contain_text(firstname)
        expect(self.__billing_address).to_contain_text(lastname)
        expect(self.__billing_address).to_contain_text(company)
        expect(self.__billing_address).to_contain_text(address1)
        expect(self.__billing_address).to_contain_text(address2)
        expect(self.__billing_address).to_contain_text(country)
        expect(self.__billing_address).to_contain_text(state)
        expect(self.__billing_address).to_contain_text(city)
        expect(self.__billing_address).to_contain_text(zipcode)
        expect(self.__billing_address).to_contain_text(mobilenumber)
