import unittest
import pytest
from Appium_Framework.base.Baseclass import Baseclass
from Appium_Framework.base.driverClass import Driver
import Appium_Framework.utilities.CustomLogger as cl
from Appium_Framework.pages.ContactUsFromPage import ContactUsFor
# driver1 = Driver()
# log = cl.customLogger()
# lunching the application
# driver = driver1.getdrivermethod()
# log.info("App lunched successfully")
# working wth the base calsss
# base = Baseclass(driver)
# Object of ContactUsFormPage
# contact = ContactUsFor(driver)


@pytest.mark.usefixtures('beforeclass')
class TestContactUsForm(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_object(self):
        self.cf = ContactUsFor(self.driver)

    @pytest.mark.run(order=1)
    def test_open_contact_form(self):
        self.cf.clickContactUsFrom()
        self.cf.verifyContactPage()

    @pytest.mark.run(order=2)
    def test_enter_data(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMoble()
        self.cf.clicksubmit()


# with using waitforElement method
# element = base.waitforElement("com.code2lead.kwad:id/ContactUs", "id")
# element.click()

# taking the screenshot after lunching the app"
# base.screeenShots("Lunched the app")
# to check element is displayed or not
# element = base.isDisplayed("com.code2lead.kwad:id/ContactUs", "id")
# print(element)

# with using clickElement method from Baseclass
# base.clickelement("com.code2lead.kwad:id/ContactUs", "id")

# After clicking on contact us then we are sending text using send_keys method from Baseclass
# base.sendText("Aditya", "Enter Name", "text")
# base.screeenShots("All task executed")



