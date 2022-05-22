import time

from appium.webdriver.appium_service import AppiumService
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Step-1 create object of appium service
appium_service = AppiumService()

# Step-2 call start method by using service class object
appium_service.start()

# Step-3 create desire capabilities
desired_caps ={
    "appPackage": "com.code2lead.kwad",
    "appActivity": "com.code2lead.kwad.MainActivity",
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "deviceName": "Pixel 5 API 30",
    "udid": "emulator-5554",
    "app": "C://Users//user//PycharmProjects//Appium_project//Basic//Android_Demo_App.apk"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()

time.sleep(5)
driver.quit()

# Step-4 stop the server mandatory
appium_service.stop()
