import pytest

from pages.contact_us_page import ContactUs
from utils.test_data import Data
from utils.tools import take_screenshot


class TestContactUs:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.contact = ContactUs(self.page)

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
        take_screenshot(self.page, 'contact_us')




