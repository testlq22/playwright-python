from playwright.sync_api import Page, expect


class LoginValidCred:

    def __init__(self, page: Page):

        self.page = page

        self.__submit_login_btn = self.page.locator('[href="/login"]')
        self.__login_form = self.page.locator('#form > div > div > div.col-sm-4.col-sm-offset-1 > div > h2')
        # form1
        self.__email_input = self.page.locator('[data-qa="login-email"]')
        self.__password_input = self.page.locator('[data-qa="login-password"]')
        self.__login_btn = self.page.locator('[data-qa="login-button"]')

        # form5(logged)
        self.__logged_user = self.page.locator('#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(10) > a')
        self.__del_user = self.page.locator('[href="/delete_account"]')
        self.__account_info = self.page.locator('[class="title text-center"]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def submit_login_btn_click(self) -> None:
        self.__submit_login_btn.click()

    def login_text_visible(self) -> None:
        expect(self.__login_form).to_have_text('Login to your account')
        expect(self.__login_form).to_be_visible()

    def set_email(self, email) -> None:
        self.__email_input.fill(email)

    def login_btn_click(self) -> None:
        self.__login_btn.click()

    def set_password(self, password) -> None:
        self.__password_input.fill(password)

    def logged_as_visible(self, user_name) -> None:
        expect(self.__logged_user).to_have_text(f' Logged in as {user_name}')
        expect(self.__logged_user).to_be_visible()

    def click_delete_account_btn(self) -> None:
        self.__del_user.click()

    def account_deleted_visible(self) -> None:
        expect(self.__account_info).to_have_text('Account Deleted!')
        expect(self.__account_info).to_be_visible()

