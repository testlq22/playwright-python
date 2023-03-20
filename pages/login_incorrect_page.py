from playwright.sync_api import Page, expect


class LoginIncorrectCred:

    def __init__(self, page: Page):

        self.page = page

        self.__submit_login_btn = self.page.locator('[href="/login"]')
        self.__login_form = self.page.locator('#form > div > div > div.col-sm-4.col-sm-offset-1 > div > h2')
        # form1
        self.__email_input = self.page.locator('[data-qa="login-email"]')
        self.__password_input = self.page.locator('[data-qa="login-password"]')
        self.__login_btn = self.page.locator('[data-qa="login-button"]')

        # form2
        self.__error_msg = self.page.locator('#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > p')

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

    def error_msg_visible(self) -> None:
        expect(self.__error_msg).to_have_text('Your email or password is incorrect!')
        expect(self.__error_msg).to_be_visible()

