from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait
import Appium_Framework.utilities.CustomLogger as cl


class Baseclass:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitforElement(self, locator_value, locator_type):
        locator_type = locator_type.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        if locator_type == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locator_value))
            return element

        elif locator_type == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locator_value))
            return element

        elif locator_type == "desc":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("%s")' % (locator_value)))
            return element

        elif locator_type == "index":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().index("%d")' % int(locator_value)))
            return element

        elif locator_type == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locator_value))
            return element

        elif locator_type == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % locator_value))
            return element

        else:
            self.log.info(f"Element not found{locator_value}")
        return element

    def getelement(self,locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.waitforElement(locator_value,locator_type)
            self.log.info(f"Element found with locatortype: " + locator_value + "with the locator value" + locator_type)
        except:
            self.log.info(f"Element not found with locatortype: " + locator_value + "and the locator value is: " + locator_type)

        return element

    def clickelement(self,locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.waitforElement(locator_value,locator_type)
            element.click()
            self.log.info(f"Clicked on Element found with locatortype: " + locator_value + "and the locator value is :" + locator_type)
        except:
            self.log.info(f"Unable to click on the locator with locatortype: " + locator_value + "and with the locator value is:" + locator_type)




