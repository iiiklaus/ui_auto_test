from selenium.webdriver.common.by import By

from uiAutoTest.base.mis.base_page import BasePage,BaseHander
from uiAutoTest.utils import select_channel,DriverUntil,is_exist

class AuditPage(BasePage):
    def __init__(self):
        super().__init__()
        self.title = By.CSS_SELECTOR, "[placeholder='请输入:文章名称']"
        self.channel = By.CSS_SELECTOR,"[placeholder='请选择状态']"
        self.query_btn = By.CSS_SELECTOR,".find"
        self.pass_btn = By.XPATH, "//tbody/tr/td[8]/div/button[2]"
        self.confirm_btn = By.CSS_SELECTOR, ".el-button--primary"
        self.end_time=By.XPATH, "[placeholder='选择结束时间']"
    def find_title(self):
        return self.get_element(self.title)
    #定位状态选择框
    def find_channel(self):
        return self.get_element(self.channel)
    def find_query_btn(self):
        return self.get_element(self.query_btn)
    def find_pass_btn(self):
        return self.get_element(self.pass_btn)
    def find_confirm_btn(self):
        return self.get_element(self.confirm_btn)
    def find_end_time(self):
        return self.get_element(self.end_time)
class AuditHandler(BaseHander):
    def __init__(self):
        self.audit_element = AuditPage()
    #输入文章标题
    def input_title(self, title):
        self.input_text(self.audit_element.find_title(), title)
    #选择状态
    def select_channel(self, status):
        select_channel(self.audit_element.driver,self.audit_element.find_channel(),status)

    #点击查询
    def click_query_btn(self):
        self.audit_element.find_query_btn().click()
    #点击通过
    def click_pass_btn(self):
        self.audit_element.find_pass_btn().click()
    #点击确定
    def click_confirm_btn(self):
        self.audit_element.find_confirm_btn().click()
    def input_time(self,end_time):
        self.input_text(self.audit_element.find_end_time(), end_time)
class AuditProxy:
    def __init__(self):
        self.audit_handler = AuditHandler()
    #审核第一条文章
    def audit_article(self,title,status,end_time):
        self.audit_handler.input_title(title)
        self.audit_handler.select_channel(status)
        self.audit_handler.input_time(end_time)
        self.audit_handler.click_query_btn()
        self.audit_handler.click_pass_btn()
        self.audit_handler.click_confirm_btn()
    #查询审核通过
    def audit_article_pass(self,title):
        self.audit_handler.input_title(title)
        self.audit_handler.select_channel('审核通过')
        self.audit_handler.click_query_btn()
        return is_exist(self.audit_handler.audit_element.driver,title)