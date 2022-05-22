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
# 1st method with using UiSelector
# ele_txt = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ENTER SOME VALUE")')
# 2nd without using UiSelector
ele_txt = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("ENTER SOME VALUE")')
ele_txt.click()
