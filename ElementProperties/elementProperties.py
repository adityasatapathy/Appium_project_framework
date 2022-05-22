from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps ={
    "appPackage": "com.code2lead.kwad",
    "appActivity": "com.code2lead.kwad.MainActivity",
    "platformName": "Android",
    "deviceName": "Pixel 5 API 30",
    "udid": "emulator-5554",
    "app": "C://Users//user//PycharmProjects//Appium_project//Basic//Android_Demo_App.apk"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
ele = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")

print("Is Displayed: ", ele.is_displayed())
print("Is Enabled: ", ele.is_enabled())
print("Is Selected: ", ele.is_selected())
print("Size: ", ele.size)
print("Location: ", ele.location)

time.sleep(2)
driver.quit()