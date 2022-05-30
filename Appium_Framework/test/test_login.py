import unittest
import pytest
import Appium_Framework.utilities.CustomLogger as cl
from Appium_Framework.base.Baseclass import Baseclass
from Appium_Framework.pages.LoginPage import LoginPage


@pytest.mark.usefixtures('beforeclass')
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_object(self):
        self.lg = LoginPage(self.driver)
        self.base = Baseclass(self.driver)

    @pytest.mark.run(order=2)
    def test_open_contact_form(self):
        self.lg.enter_text_admin()
        self.lg.click_submit_admin()

    @pytest.mark.run(order=1)
    def test_open_login_screen(self):
        cl.allureLogs("App opened")
        self.lg.clickloginbuton()
        self.lg.enter_email()
        self.lg.enter_password()
        self.lg.enter_password()
        self.lg.click_submit()
        self.lg.verify_adminpage()

