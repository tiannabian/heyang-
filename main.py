__author__ = '123456'
# coding=utf-8
import pytest

if __name__ == '__main__':
    pytest.main(["-m demo", r"--junitxml=report\test.xml", r"--alluredir=report\allure"])