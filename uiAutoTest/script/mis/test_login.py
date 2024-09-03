#登录测试用例
import pytest

from uiAutoTest.page.auto_houtai.home_page import HomeProxy
from uiAutoTest.page.auto_houtai.login_page import LoginProxy
from uiAutoTest.utils import DriverUntil

class TestLogin:
    #定义类级别的fixture
    def setup_class(self):
        self.login_proxy=LoginProxy()
        self.home_proxy=HomeProxy()
    def teardown_class(self):
        DriverUntil.get_mis_quit()
    def test_login(self,username,password):
        self.login_proxy.login(username,password)
        user=self.home_proxy.get_user()
        assert "管理员" in user

