#自媒体平台的登录页面
from selenium.webdriver.common.by import By

from uiAutoTest.base.mp.base_page import BasePage,BaseHander
#po模式 --对象库层/操作层/业务层
class LoginPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        #手机号码、验证码、登录点击
        self.phone_num= By.XPATH,'//*[@placeholder="请输入手机号"]'
        self.code=By.XPATH,'//*[@placeholder="验证码"]'
        self.login_btn=By.CSS_SELECTOR,'.el-button--primary'
    def find_phone_num(self):
        return self.driver.get_element(self.phone_num)
    def find_code(self):
        return self.driver.get_element(self.code)
    def find_login_btn(self):
        return self.driver.get_element(self.login_btn)
class LoginHander(BaseHander):
    def __init__(self):
        self.login_element=LoginPage()
    def input_phone(self,text):
        self.input_text(self.login_element.find_phone_num(),text)
    def input_code(self,text):
        self.input_text(self.login_element.find_code(),text)
    def input_login_btn(self):
        return self.login_element.find_login_btn().click()

class LoginProxy:
    def __init__(self):
        self.login_hander=LoginHander()
    #完成登录
    def loginpage(self,phone,code):
        self.login_hander.input_phone(phone)
        self.login_hander.input_code(code)
        self.login_hander.input_login_btn()