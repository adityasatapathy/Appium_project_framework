from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps ={
    "appPackage": "com.code2lead.kwad",
    "appActivity": "com.code2lead.kwad.MainActivity",
    "platformName": "Android",
    "deviceName": "OnePlus 7T",
    "udid": "1e8f62ec",
    "app": "C://Users//user//PycharmProjects//Appium_project//Basic//Android_Demo_App.apk"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()