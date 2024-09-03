def add(x,y):
    return x + y
import pytest
class TestAdd:
    def setup_class(self):
        print("这是类的setup")
    def teardown_class(self):
        print("这是类的teardown")
    @pytest.mark.parametrize("x,y,expected", [(1,1,2),(2,2,4),(3,3,6)])
    def test_add(self,x,y,expected):
        assert add(x,y) == expected
