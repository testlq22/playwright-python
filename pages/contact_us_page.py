from playwright.sync_api import Page, expect


class ContactUs:

    def __init__(self, page: Page):

        self.page = page
        self.__contact_us_btn = self.page.locator('[href="/contact_us"]')

        self.__getInTouch = self.page.locator('#contact-page > div.row > div.col-sm-8 > div > h2')
        # form1
        self.__name_input = self.page.locator('[data-qa="name"]')
        self.__email_input = self.page.locator('[data-qa="email"]')
        self.__subject_input = self.page.locator('[data-qa="subject"]')
        self.__message_input = self.page.locator('[id="message"]')
        self.__upload_file = self.page.locator('input[type="file"]')
        self.__submit_btn = self.page.locator('[data-qa="submit-button"]')

        # form2
        self.__sucess_msg = self.page.locator('[class="status alert alert-success"]')
        self.__home_btn = self.page.locator('[class="fa fa-angle-double-left"]')
        # not used
        self.__pop_up = self.page.locator('#html > body > div[1] > div[2] > div[2] > div > div > div[2] > div > div > div[2]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def contact_us_btn_click(self) -> None:
        self.__contact_us_btn.click()

    def get_in_text_visible(self) -> None:
        expect(self.__getInTouch).to_have_text('Get In Touch')
        expect(self.__getInTouch).to_be_visible()

    def set_username(self, user_name) -> None:
        self.__name_input.fill(user_name)

    def set_email(self, email) -> None:
        self.__email_input.fill(email)

    def set_subject(self, subj) -> None:
        self.__subject_input.fill(subj)

    def set_message(self, msg) -> None:
        self.__message_input.fill(msg)

    def set_upload_file(self, file) -> None:
        self.__upload_file.set_input_files(file)

    def submit_btn_click(self) -> None:
        self.__submit_btn.click()

    def click_ok(self) -> None:
        self.page.on("dialog", lambda dialog: dialog.accept())

    def success_msg_visible(self) -> None:
        expect(self.__sucess_msg).to_have_text('Success! Your details have been submitted successfully.')
        expect(self.__sucess_msg).to_be_visible()

    def click_home_btn(self) -> None:
        self.__home_btn.click()

    """def close_pop_up(self) -> None:
        self.__pop_up.click(force=True)

    def handle_route(self) -> None:
            self.page.route("https://googleads.", lambda route: route.abort())
            self.page.route.continue_()"""

