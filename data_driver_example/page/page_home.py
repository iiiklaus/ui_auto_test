from selenium.webdriver.common.by import By


import untils
from data_driver_example.base import base_page
#home页面
#对象库层
class PageHome(base_page.BasePage):
    #封装元素定位的方法
    def __init__(self):
        super().__init__()
        # self.driver = untils.untilDrive.get_drive()
        self.login_btn=By.CSS_SELECTOR,'.red'
        #找到登录按钮
    def find_login_btn(self):
        return self.get_element(self.login_btn)
#操作层 --操作元素
class OpeatorHome(base_page.BaseHander):
    def __init__(self):
        self.home_element=PageHome()
    def hand_button(self):
        self.home_element.find_login_btn().click()
#业务层 --调用操作层组合操作
class HomeProxy:
    def __init__(self):
        self.hander=OpeatorHome()
    def hand_button(self):
        self.hander.hand_button()


