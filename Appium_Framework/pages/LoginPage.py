from Appium_Framework.base.Baseclass import Baseclass
import Appium_Framework.utilities.CustomLogger as cl


class LoginPage(Baseclass):
    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator for Login PAge
    _loginbutton = "com.code2lead.kwad:id/Login"  # ID
    _enteremail = "3"  # index
    _enterpassword = "Enter Password"  # text
    _submitbutton = "LOGIN"  # text
    _wrongcred = "Wrong Credentials"  # text
    _pagetitle = "Enter Admin"  # text
    _enteradmin = "Enter Admin"  # text
    _adminsubmit = "SUBMIT"  # text

    def clickloginbuton(self):
        self.clickelement(self._loginbutton, "id")
        cl.allureLogs("CLicked on login button")



