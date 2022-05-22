import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


def deviceDrivers(deviceID, systemPort):
    desired_caps = {
        "appPackage": "com.skill2lead.appiumdemo",
        "appActivity": "com.skill2lead.appiumdemo.MainActivity",
        "platformName": "Android",
        "deviceName": "Pixel 5 API 30",
        "udid": "emulator-5554",
        "deviceName": "systemPort",
        "udid" = "deviceID",
        "app": "C://Users//user//PycharmProjects//Appium_project//Android_Appium_Demo.apk"
    }
#     desired_caps ={
#         "appPackage": "com.skill2lead.appiumdemo",
#         "appActivity": "com.skill2lead.appiumdemo.MainActivity",
#         "platformName": "Android",
#         "deviceName": "Pixel 5 API 30",
#         "udid": "emulator-5554",
#         "deviceName": systemPort,
#         "udid" = deviceID,
#         "app": "C://Users//user//PycharmProjects//Appium_project//Android_Appium_Demo.apk"
# }
    # desired_caps['deviceName'] = systemPort
    # desired_caps['udid'] = deviceID
    # desired_caps['app'] = "C://Users//user//PycharmProjects//Appium_project//Android_Appium_Demo.apk"


    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver


def enterText(driver):
    ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    ele_id.click()

    time.sleep(2)
    # using class name
    ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    ele_classname.send_keys("Aditya")
    submt_btn = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn1")
    submt_btn.click()
    time.sleep(2)
    driver.quit()


def test_deviceTest():
    d1 = deviceDrivers('1e8f62ec', 8200)
    d2 = deviceDrivers('emulator-5554', 8201)
    enterText(d1)
    enterText(d2)



