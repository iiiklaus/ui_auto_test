#写测试用例
import pytest

from uiAutoTest.page.auto_zimeiti.login_page import LoginProxy
from uiAutoTest.page.auto_zimeiti.publish_page import PublishProxy
from uiAutoTest.utils import is_exist,DriverUntil
from uiAutoTest.page.auto_zimeiti.home_page import HomeProxy


class TestArticle:
    def setup_class(self):
        #类级别的fix
        self.homeProxy=HomeProxy()
        self.loginProxy=LoginProxy()
        self.publishProxy=PublishProxy()
    def teardown_class(self):
        DriverUntil.quit_driver()
    def test_login(self,phone,code,expect_user):
        self.loginProxy.loginpage(phone,code)
        text=self.homeProxy.assert_yewu()
        assert expect_user == text
    def test_publish(self,title,content,channel,expect_status):
        self.publishProxy.publish_content(title,content,channel)
        assert is_exist(DriverUntil.get_drive(),expect_status)

