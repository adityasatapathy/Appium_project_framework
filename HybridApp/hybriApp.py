import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# 1. mobile browser and chrome should be in same version
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait

desired_caps ={
    "appPackage": "net.oneplus.launcher",
    "appActivity": ".Launcher",
    "platformName": "Android",
    "deviceName": "OnePlus 7T",
    "udid": "1e8f62ec",
    "app": "C://Users//user//PycharmProjects//Appium_project//Basic//Android_Demo_App.apk"
}

# 1. create drive object
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 2. create webdriverwait
wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

# 3. Open the URL in browser
ele_lunch = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Chrome"]'))
ele_lunch.click()

# 4. entering text in search bar
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(x=211, y=165)
actions.w3c_actions.pointer_action.click()
actions.send_keys("https://www.google.com/")
driver.press_keycode(66)
actions.w3c_actions.perform()
# ele_search = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/search_box_text"))
# ele_search.click()
# ele_search.send_keys("https://www.google.com/")
# 66 is for enter
# driver.press_keycode(66)
# time.sleep(2)
