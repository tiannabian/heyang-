__author__ = '123456'
# coding=utf-8
import pytest

@pytest.fixture()
def init_web():
    print("")
    yield
    print("")

@pytest.fixture(scope='class')
def class_web():
    print("class before")
    yield
    print("class after")

@pytest.fixture(scope="moudule")
def moudule_web():
    print("moudule before")
    yield
    print("moudule after")

@pytest.fixture(scope="session")
def session_web():
    print("session before")
    yield
    print("session after")



class TestA:

    @pytest.mark.q
    def test_demo(self, init_web, class_web, moudule_web, session_web):
        print("执行测试用例")

    @pytest.mark.q
    def test_1_demo(self, init_web, class_web, moudule_web, session_web):
        print("测试用例2")

class TestB:
    @pytest.mark.q
    def test_1_demo(self, init_web, class_web, moudule_web, session_web):
        print("测试用例3")

#执行次数init_web3, class_web2, moudule_web1, session_web1

#重运行  pip install pytest-rerunfailures
#pytest --rerun 2 --rerun -delay 5