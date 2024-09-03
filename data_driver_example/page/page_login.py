#登录页面
from selenium.webdriver.common.by import By

import untils
from data_driver_example.base.base_page import BasePage,BaseHander


#对象库层-封装元素定位的方法
class LoginEelement(BasePage):
    def __init__(self):
        super().__init__()
        #获取浏览器驱动对象
        # self.driver=untils.untilDrive.get_drive()
        self.username=By.ID,'username'
        self.password=By.ID,'password'
        self.login_verify=By.ID,'verify_code'
        self.login_button=By.CSS_SELECTOR,'.J-login-submit'
        self.forget_passwd=By.PARTIAL_LINK_TEXT,'忘记密码'
    def username_box(self):
        #用户名输入
        return self.get_element(self.username)
    def password_box(self):
        # 密码输入
        return self.get_element(self.password)
    def verify_box(self):
        # 验证码输入
        return self.get_element(self.login_verify)
        # return self.driver.find_element(*self.login_verify)
    def login_btn(self):
        # 登录点击输入
        return self.get_element(self.login_button)
        # return self.driver.find_element(*self.login_button)
    def forget_passwd(self):
        return self.get_element(self.forget_passwd)
        # return self.driver.find_element(*self.forget_passwd)

#操作层-对封装的元素进行操作
class LoginOperator(BaseHander):
    def __init__(self):
        #实例化对象库层
        self.login_element = LoginEelement()
    def input_username(self,username):
        # element = self.login_element.username_box()
        # element.clear()
        # element.send_keys(username)
        self.input_text(self.login_element.username_box(),username)

    def input_password(self,password):
        # element = self.login_element.password_box()
        # element.clear()
        # element.send_keys(password)
        self.input_text(self.login_element.password_box(),password)
    def input_verify_code(self,code):
        # element = self.login_element.verify_box()
        # element.clear()
        # element.send_keys(code)
        self.input_text(self.login_element.verify_box(),code)
    def login_btn_click(self):
        self.login_element.login_btn().click()
    def forget_passwd(self):
        self.login_element.forget_passwd().click()
    # def box_send(self,username,password,verify_box):
    #     self.login_element.username_box().send_keys(username)
    #     self.login_element.password_box().send_keys(password)
    #     self.login_element.verify_box().send_keys(verify_box)
    #     self.login_element.login_btn().click()

#业务层-操作组合
class LoginProxy:
    def __init__(self):
        self.login_operator = LoginOperator()
    def hander_login(self,username,password,verify_code):
        # self.login_operator.box_send(username,password,verify_box)
        self.login_operator.input_username(username)
        self.login_operator.input_password(password)
        self.login_operator.input_verify_code(verify_code)
        self.login_operator.login_btn_click()
    def forget_passwd_hander(self):
        self.login_operator.forget_passwd()

# login_proxy = LoginProxy()
# #在这个部分的时候就可以开始编写测试用例了，包括参数化和断言
# login_proxy.hander_login("123","123","888")