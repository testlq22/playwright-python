from playwright.sync_api import Page, expect


class PlaceOrderLoginBeforeCheckout:

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
        self.__comment_field = self.page.locator('[name="message"]')
        self.__place_order_btn = self.page.locator('[href="/payment"]')
        self.__name_on_card = self.page.locator('[data-qa="name-on-card"]')
        self.__card_number = self.page.locator('[data-qa="card-number"]')
        self.__cvc = self.page.locator('[data-qa="cvc"]')
        self.__exp_month = self.page.locator('[data-qa="expiry-month"]')
        self.__exp_year = self.page.locator('[data-qa="expiry-year"]')
        self.__pay_btn = self.page.locator('[data-qa="pay-button"]')
        self.__success_alert = self.page.locator('[id="success_message"]>[class="alert-success alert"]')
        self.__success_alert2 = self.page.locator('[class="col-sm-9 col-sm-offset-1"]')
        self.__product_in_cart_1 = self.page.locator('[id="product-1"]')
        self.__product_in_cart_2 = self.page.locator('[id="product-2"]')

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

    def verify_product_1_visible(self) -> None:
        expect(self.__product_in_cart_1).to_be_visible()

    def verify_product_2_visible(self) -> None:
        expect(self.__product_in_cart_2).to_be_visible()

    def check_product_1_details_info(self, name, price, quantity, total) -> None:
        expect(self.__product_in_cart_1).to_contain_text(name)
        expect(self.__product_in_cart_1).to_contain_text(price)
        expect(self.__product_in_cart_1).to_contain_text(quantity)
        expect(self.__product_in_cart_1).to_contain_text(total)

    def check_product_2_details_info(self, name, price, quantity, total) -> None:
        expect(self.__product_in_cart_2).to_contain_text(name)
        expect(self.__product_in_cart_2).to_contain_text(price)
        expect(self.__product_in_cart_2).to_contain_text(quantity)
        expect(self.__product_in_cart_2).to_contain_text(total)

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

    def add_comment(self, text) -> None:
        self.__comment_field.fill(text)

    def click_place_order_btn(self) -> None:
        self.__place_order_btn.click()

    def fill_name_on_card(self, firstname, lastname) -> None:
        self.__name_on_card.fill(firstname + lastname)

    def fill_card_number(self, cardnumber) -> None:
        self.__card_number.fill(cardnumber)

    def fill_cvc(self, cvc) -> None:
        self.__cvc.fill(cvc)

    def fill_exp_month(self, month) -> None:
        self.__exp_month.fill(month)

    def fill_exp_year(self, year) -> None:
        self.__exp_year.fill(year)

    def click_pay_btn(self) -> None:
        self.__pay_btn.click()

    def success_msg_visible(self) -> None:
        expect(self.__success_alert).to_have_text('Your order has been placed successfully!')

    def success_msg2_visible(self) -> None:
        expect(self.__success_alert2).to_contain_text('Congratulations! Your order has been confirmed!')
