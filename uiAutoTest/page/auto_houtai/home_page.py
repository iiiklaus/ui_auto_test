#首页页面封装
from selenium.webdriver.common.by import By

from uiAutoTest.base.mis.base_page import BasePage,BaseHander
class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        #写元素
        self.user_info=By.CSS_SELECTOR,'.user_info span'
        # 信息管理
        self.content_manage = By.XPATH, "//*[@class='side bar']/ul/li[3]/a"
        # 内容审核
        self.content_audit = By.XPATH, "//*[@class='current3']/li[3]/a"
    #查找元素
    def find_user_info(self):
        return self.get_element(self.user_info)
    def find_content_manage(self):
        return self.get_element(self.content_manage)
    def find_content_audit(self):
        return self.get_element(self.content_audit)
class HomeHandler(BaseHander):
    def __init__(self):
        self.home_element=HomePage()
    #操作元素
    #获取用户信息
    def get_user_info(self):
        return self.home_element.find_user_info().text
    #点击信息管理
    def click_content_manage(self):
        self.home_element.find_content_manage().click()
    #点击内容管理
    def click_content_audit(self):
        self.home_element.find_content_audit().click()
class HomeProxy:
    def __init__(self):
        self.home_handler=HomeHandler()
    #组合
    def get_user(self):
        return self.home_handler.get_user_info()
    def go_content_audit(self):
        self.home_handler.click_content_manage()
        self.home_handler.click_content_audit()