import  pytest

from uiAutoTest.page.auto_houtai.home_page import HomeProxy
from uiAutoTest.page.auto_houtai.login_page import LoginProxy
from uiAutoTest.page.auto_houtai.shenhe_page import AuditProxy
from uiAutoTest.utils import DriverUntil

class TestAudit:
    def setup_class(self):
        self.home_proxy=HomeProxy()
        self.audit_proxy=AuditProxy()
    def teardown_class(self):
        DriverUntil.get_mis_quit()
    def test_audit(self,title,status,end_time):
        self.home_proxy.go_content_audit()
        self.audit_proxy.audit_article(title,status,end_time)
        result=self.audit_proxy.audit_article_pass(title)
        assert result