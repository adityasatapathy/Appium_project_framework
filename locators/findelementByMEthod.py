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
ele_loop = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
for element in ele_loop:
    print(element.text)

for element in ele_loop:
    button = element.text
    if button == "CONTACT US FORM":
        button.click()
        break
time.sleep(2)