#自媒体的首页

from selenium.webdriver.common.by import By

from uiAutoTest.base.mp.base_page import BasePage,BaseHander
#po模式 --对象库层/操作层/业务层
class HomePage(BasePage):
    def __init__(self):
        super().__init__(self)
        #手机号码、验证码、登录点击
        self.content_mag= By.XPATH,'//*[@text()="内容管理"]'
        self.publish_content=By.XPATH,'//*[@class="el-menu-item is-active"]'
        self.username=By.XPATH,"//*[@class='sidebar-el-menu-el-menu']/div[2]/li/ul/li[1]"
    def find_content_msg(self):
        return self.driver.get_element(self.content_mag)
    def find_publish_content(self):
        return self.driver.get_element(self.publish_content)
    def find_username(self):
        return self.driver.get_element(self.username)
class HomeHandler(BaseHander):
    def __init__(self):
        self.login_element=HomePage()
    def content_click(self):
        self.login_element.find_content_msg().click()
    def publish_click(self):
        self.login_element.find_publish_content().click()
    def get_username(self):
        return self.login_element.find_username().text

class HomeProxy:
    def __init__(self):
        self.login_handler=HomeHandler()
    #进入发布页面
    def publish_page(self):
        self.login_handler.content_click()
        self.login_handler.publish_click()
    def assert_yewu(self):
        return self.login_handler.get_username()