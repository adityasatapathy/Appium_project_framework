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
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()

time.sleep(2)
ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_classname.send_keys("Aditya")
ele_classname.click()
driver.press_keycode(67)
driver.press_keycode(67)

time.sleep(2)
# back button
driver.press_keycode(4)
driver.press_keycode(4)

time.sleep(5)
# submt_btn = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn1").click()
driver.quit()
