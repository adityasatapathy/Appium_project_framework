from Appium_Framework.base.Baseclass import Baseclass
from Appium_Framework.base.driverClass import Driver
import Appium_Framework.utilities.CustomLogger as cl

driver1 = Driver()
log = cl.customLogger()

# lunching the application
driver = driver1.getdrivermethod()
log.info("App lunched successfully")

# working wth the base calsss
base = Baseclass(driver)
# with using waitforElement method
# element = base.waitforElement("com.code2lead.kwad:id/ContactUs", "id")
# element.click()

# to check element is displayed or not
element = base.isDisplayed("com.code2lead.kwad:id/ContactUs", "id")
print(element)

# with using clickElement method from Baseclass
base.clickelement("com.code2lead.kwad:id/ContactUs", "id")

# After clicking on contact us then we are sending text using send_keys method from Baseclass
base.sendText("Aditya", "Enter Name", "text")



