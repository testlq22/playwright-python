from playwright.sync_api import Page, expect


class RegExistMail:

    def __init__(self, page: Page):

        self.page = page

        self.__submit_login_btn = self.page.locator('[href="/login"]')
        self.__signup_form = self.page.locator('#form > div > div > div:nth-child(3) > div > h2')
        # form1
        self.__name_input = self.page.locator('[data-qa="signup-name"]')
        self.__email_input = self.page.locator('[data-qa="signup-email"]')
        self.__signup_btn = self.page.locator('[data-qa="signup-button"]')
        self.__error_msg = self.page.locator('#form > div > div > div:nth-child(3) > div > form > p')

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

    def error_msg_visible(self) -> None:
        expect(self.__error_msg).to_have_text('Email Address already exist!')
        expect(self.__error_msg).to_be_visible()
