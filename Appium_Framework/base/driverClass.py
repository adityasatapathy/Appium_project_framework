from appium import webdriver


class Driver:
    def getdrivermethod(self):
        desired_caps = {
            "appPackage": "com.code2lead.kwad",
            "appActivity": "com.code2lead.kwad.MainActivity",
            "platformName": "Android",
            "deviceName": "Pixel 5 API 30",
            "udid": "emulator-5554",
            "app": "C://Users//user//PycharmProjects//Appium_project//Basic//Android_Demo_App.apk"
        }

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return driver
    
