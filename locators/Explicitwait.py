from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
# import time

from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
    "appPackage": "com.code2lead.kwad",
    "appActivity": "com.code2lead.kwad.MainActivity",
    "platformName": "Android",
    "deviceName": "Pixel 5 API 30",
    "udid": "emulator-5554",
    "app": "C://Users//user//PycharmProjects//Appium_project//Basic//Android_Demo_App.apk"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
ele = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue"))
ele.click()

ele_classname = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText"))
ele_classname.send_keys("Aditya")

submt_btn = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn1"))
submt_btn.click()

driver.quit()
