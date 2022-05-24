import time

import pytest
from Appium_Framework.base.driverClass import Driver


@pytest.yield_fixture(scope='class')
def beforeclass(request):
    print('Before a class')
    driver1 = Driver()
    driver = driver1.getdrivermethod()
    if request.cls is not None:
        request.cls.driver = driver  # making driver object class variable
    yield
    time.sleep(1)
    driver.quit()
    print('After class')
