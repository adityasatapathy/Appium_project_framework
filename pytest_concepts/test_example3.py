import pytest


@pytest.yield_fixture(scope='module')
def beforeclass():
    print('Before a class')
    yield
    print('After a class')


@pytest.yield_fixture()
def beforemethod():
    print('Before a method')
    yield
    print('After a method')


def test_methodA(beforeclass,beforemethod ):
    print("Thi is for method-A")


def test_methodB(beforeclass,beforemethod ):
    print("Thi is for method-B")