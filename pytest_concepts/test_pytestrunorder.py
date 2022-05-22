import pytest
import allure

@pytest.mark.run(order=4)
def test_methodA():
    allurelogs("Launching the app")
    print("Print method-A")


@pytest.mark.run(order=2)
def test_methodB():
    print("Print method-B")


@pytest.mark.skip
@pytest.mark.run(order=3)
def test_methodC():
    print("Print method-C")


@pytest.mark.run(order=1)
def test_methodD():
    print("Print method-D")
    assert False


def allurelogs(text):
    with allure.step(text):
        pass