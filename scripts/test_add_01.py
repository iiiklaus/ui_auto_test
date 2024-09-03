import time
import pytest
#定义的类名必须以Test开头
def add(x,y):
    return x+y
version=22
class TestADD:
    #函数级别的fixture
    def setup(self):
        print("测试开始执行时间:", time.time())
    def teardown(self):
        print("测试结束执行时间:", time.time())
    #类级别的fixture
    def setup_class(self):
        print("111测试开始执行时间:", time.time())
    def teardown_class(self):
        print("111测试结束执行时间:", time.time())
    # @pytest.mark.trylast
    @pytest.mark.skipif(condition=version>21,reason="版本原因直接跳过")
    def test_add_01(self):
        result=add(1,2)
        print(result)
    @pytest.mark.run(order=1)
    def test_add_02(self):
        result=add(2,3)
        print(result)


