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
# xpath and content desc
#ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Btn1"]')
# xpath and resource id
ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]')

ele_xpath.click()
time.sleep(2)
driver.quit()