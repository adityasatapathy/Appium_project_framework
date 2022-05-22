import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps ={
    "appPackage": "com.code2lead.kwad",
    "appActivity": "com.code2lead.kwad.MainActivity",
    "platformName": "Android",
    "deviceName": "Pixel 5 API 30",
    "udid": "emulator-5554",
    "app": "C://Users//user//PycharmProjects//Appium_project//Basic//Android_Demo_App.apk"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(2)
# call startActivity method
driver.start_activity("com.android.gallery3d", "com.android.gallery3d.app.GalleryActivity")

time.sleep(2)

driver.start_activity("com.code2lead.kwad", "com.code2lead.kwad.MainActivity")
time.sleep(1)
driver.quit()