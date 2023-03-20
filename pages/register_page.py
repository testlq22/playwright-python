from playwright.sync_api import Page, expect


class Register:

    def __init__(self, page: Page):

        self.page = page

        self.__submit_login_btn = self.page.locator('[href="/login"]')
        self.__signup_form = self.page.locator('#form > div > div > div:nth-child(3) > div > h2')
        # form1
        self.__name_input = self.page.locator('[data-qa="signup-name"]')
        self.__email_input = self.page.locator('[data-qa="signup-email"]')
        self.__signup_btn = self.page.locator('[data-qa="signup-button"]')
        # form2(account information)
        self.__first_title = self.page.locator('#form > div > div > div > div > h2 > b')
        self.__mr_radio_btn = self.page.locator('[id="uniform-id_gender1"]')
        self.__password_input = self.page.locator('[data-qa="password"]')
        self.__day_birth = self.page.locator('select[id="days"]')
        self.__month_birth = self.page.locator('select[id="months"]')
        self.__year_birth = self.page.locator('select[id="years"]')
        self.__newsletter = self.page.locator('#newsletter')
        self.__special_offers = self.page.locator('#optin')
        # form(address information)
        self.__first_name = self.page.locator('input[id="first_name"]')
        self.__last_name = self.page.locator('input[id="last_name"]')
        self.__company = self.page.locator('input[id="company"]')
        self.__address_1 = self.page.locator('input[id="address1"]')
        self.__address_2 = self.page.locator('input[id="address2"]')
        self.__country = self.page.locator('select[id="country"]')
        self.__state = self.page.locator('input[id="state"]')
        self.__city = self.page.locator('input[id="city"]')
        self.__zip_code = self.page.locator('input[id="zipcode"]')
        self.__mobile_number = self.page.locator('input[id="mobile_number"]')
        self.__submit_btn = self.page.locator('//button[text()="Create Account"]')
        # form4(confirmation)
        self.__account_info = self.page.locator('[class="title text-center"]')
        self.__continue_btn = self.page.locator('[class="btn btn-primary"]')
        # form5(logged)
        self.__logged_user = self.page.locator('#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(10) > a')
        self.__del_user = self.page.locator('[href="/delete_account"]')
        self.__logout_user = self.page.locator('[href="/logout"]')
        self.__main_logo = self.page.locator('[class="logo pull-left"]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def submit_login_btn_click(self) -> None:
        self.__submit_login_btn.click()

    def signup_text_visible(self) -> None:
        expect(self.__signup_form).to_have_text('New User Signup!')
        expect(self.__signup_form).to_be_visible()

    def set_username(self, user_name) -> None:
        self.__name_input.fill(user_name)

    def set_email(self, email) -> None:
        self.__email_input.fill(email)

    def signup_btn_click(self) -> None:
        self.__signup_btn.click()

    def first_title_visible(self) -> None:
        expect(self.__first_title).to_have_text('Enter Account Information')
        expect(self.__first_title).to_be_visible()

    def select_mr(self) -> None:
        self.__mr_radio_btn.check()

    def set_password(self, password) -> None:
        self.__password_input.fill(password)

    def select_day(self, day) -> None:
        self.__day_birth.select_option(day)

    def select_month(self, month) -> None:
        self.__month_birth.select_option(month)

    def select_year(self, year) -> None:
        self.__year_birth.select_option(year)

    def select_newsletter_checkbox(self) -> None:
        self.__newsletter.check()

    def select_special_offers_checkbox(self) -> None:
        self.__special_offers.check()

    def set_first_name(self, first_name) -> None:
        self.__first_name.fill(first_name)

    def set_last_name(self, last_name) -> None:
        self.__last_name.fill(last_name)

    def set_company(self, company_name) -> None:
        self.__company.fill(company_name)

    def set_address_1(self, address) -> None:
        self.__address_1.fill(address)

    def set_address_2(self, address) -> None:
        self.__address_2.fill(address)

    def select_country(self, country) -> None:
        self.__country.select_option(country)

    def set_state(self, state) -> None:
        self.__state.fill(state)

    def set_city(self, city) -> None:
        self.__city.fill(city)

    def set_zip_code(self, zip_code) -> None:
        self.__zip_code.fill(zip_code)

    def set_mobile_number(self, number) -> None:
        self.__mobile_number.fill(number)

    def click_create_account_btn(self) -> None:
        self.__submit_btn.click()

    def account_confirmation_visible(self) -> None:
        expect(self.__account_info).to_have_text('Account Created!')
        expect(self.__account_info).to_be_visible()

    def click_continue_btn(self) -> None:
        self.__continue_btn.click()

    def logged_as_visible(self, user_name) -> None:
        expect(self.__logged_user).to_have_text(f' Logged in as {user_name}')
        expect(self.__logged_user).to_be_visible()

    def click_delete_account_btn(self) -> None:
        self.__del_user.click()

    def account_deleted_visible(self) -> None:
        expect(self.__account_info).to_have_text('Account Deleted!')
        expect(self.__account_info).to_be_visible()

    def click_logout_btn(self) -> None:
        self.__logout_user.click()

    def click_logo(self) -> None:
        self.__main_logo.click()

