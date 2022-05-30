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

    def enter_email(self):
        self.sendText("admin@gmail.com", self._enteradmin, "index")
        cl.allureLogs("email entered successfully")

    def enter_password(self):
        self.sendText("admin123", self._enterpassword, "text")
        cl.allureLogs("password entered successfully")

    def click_submit(self):
        self.clickelement(self._submitbutton, "text")
        cl.allureLogs("All the data entered successfully and submitted the form")

    def verify_adminpage(self):
        element = self.isDisplayed(self._pagetitle, "text")
        assert element == True
        cl.allureLogs("Admin page is verified")

    def enter_text_admin(self):
        self.sendText("aditya", self._enteradmin, "text")
        cl.allureLogs("Entered text")

    def click_submit_admin(self):
        self.clickelement(self._adminsubmit, "text")
        cl.allureLogs("Submitted successfully")




