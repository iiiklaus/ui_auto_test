import time

import pytest

class TestClass:
    """
    fixture的函数级别
    """
    def setup(self):
        print("测试开始执行时间:",time.time())
    def teardown(self):
        print("测试开始执行时间:",time.time())
    def test_1(self):
        assert 1==1
    def test_2(self):
        assert 2==2
