from Appium_Framework.base.Baseclass import Baseclass
from Appium_Framework.base.driverClass import Driver
import Appium_Framework.utilities.CustomLogger as cl
from Appium_Framework.pages.ContactUsFromPage import ContactUsFor

driver1 = Driver()
log = cl.customLogger()

# lunching the application
driver = driver1.getdrivermethod()
log.info("App lunched successfully")

# working wth the base calsss
# base = Baseclass(driver)

# Object of ContactUsFormPage
contact = ContactUsFor(driver)

contact.clickContactUsFrom()
contact.verifyContactPage()
contact.enterName()
contact.enterEmail()
contact.enterAddress()
contact.enterMoble()
contact.clicksubmit()
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



