import pytest
#定义的类名必须以Test开头
def add(x,y):
    return x+y
class TestADD:
    #定义的类名必须以test开头
    def test_add_01(self):
        result=add(1,2)
        print(result)
    def test_add_02(self):
        result=add(2,3)
        print(result)



