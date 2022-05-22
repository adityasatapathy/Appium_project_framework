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
# desired_caps["noReset"] = True noReset
# desired_caps["fullReset"] = True it will install the app then uninstall it
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()
driver.quit()