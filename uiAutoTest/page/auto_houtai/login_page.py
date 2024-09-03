#po模式-封装登录页面
from selenium.webdriver.common.by import By

from uiAutoTest.base.mis.base_page import BasePage,BaseHander
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        #元素信息
        self.username=By.NAME,'username'
        self.password=By.password,'password'
        self.login_btn=By.id,'inp1'

    def find_username(self):
        return self.get_element(self.username)
    def find_password(self):
        return self.get_element(self.password)
    def find_login_btn(self):
        #在点击登录之前需要删除disable属性
        return self.get_element(self.login_btn)
class LoginHandler(BaseHander):
    def __init__(self):
        self.login_element=LoginPage()
    def input_username(self,username):
        self.input_text(self.login_element.find_username(),username)
    def input_password(self,password):
        self.input_text(self.login_element.find_password(),password)
    def click_login_btn(self):
        #需要移除disable属性才能点击
        js_code="document.getElementById('inp1').removeAttribute('disable');"
        #通过execute_script
        self.login_element.driver.execute_script(js_code)
        self.login_element.find_login_btn().click()
class LoginProxy:
    def __init__(self):
        self.login_handler=LoginHandler()
    def login(self,username,password):
        self.login_handler.input_username(username)
        self.login_handler.input_password(password)
        self.login_handler.click_login_btn()
