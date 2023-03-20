import pytest

from pages.contact_us_page import ContactUs
from utils.test_data import Data


class TestContactUs:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.contact = ContactUs(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_contact_us(self, test_setup):
        self.contact.check_page_loaded()
        self.contact.contact_us_btn_click()
        self.contact.get_in_text_visible()
        self.contact.set_username(Data.fakeUser)
        self.contact.set_email(Data.fakeEmail)
        self.contact.set_subject(Data.subject)
        self.contact.set_message(Data.message)
        self.contact.set_upload_file(Data.fileToUpload)
        self.page.wait_for_timeout(1000)
        self.contact.click_ok()
        self.contact.submit_btn_click()
        self.contact.success_msg_visible()
        self.contact.click_home_btn()
        self.contact.check_page_loaded()




