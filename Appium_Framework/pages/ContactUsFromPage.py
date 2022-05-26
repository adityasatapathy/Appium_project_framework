from Appium_Framework.base.Baseclass import Baseclass
import Appium_Framework.utilities.CustomLogger as cl


class ContactUsFor(Baseclass):
    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator value in contactUs form
    _contactUSFromButton = "com.code2lead.kwad:id/ContactUs"  # ID
    _enterName = "Enter Name"  # text
    _enterEmail = "Enter Email"  # text
    _enterAddress = "Enter Address"  # text
    _enterMobile = "Enter Mobile No"   # text
    _submitButton = "SUBMIT"  # text
    _pageTitile = "Contact Us form" # text

    def clickContactUsFrom(self):
        self.clickelement(self._contactUSFromButton, "id")
        cl.allureLogs("Clicked on Contact US From Button")

    def verifyContactPage(self):
        element = self.isDisplayed(self._pageTitile, "text")
        cl.allureLogs("COntact Us From has been Verified")
        assert element == True

    def enterName(self):
        self.sendText("aditya", self._enterName, "text")

    def enterEmail(self):
        self.sendText("aditya@gmail.com", self._enterEmail, "text")

    def enterAddress(self):
        self.sendText("berhampur", self._enterAddress, "text")

    def enterMoble(self):
        self.sendText("12345", self._enterMobile, "text")

    def clicksubmit(self):
        self.clickelement(self._submitButton, "text")
