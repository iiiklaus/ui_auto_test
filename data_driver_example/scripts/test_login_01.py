import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from untils import get_msg,untilDrive,get_case_login_data
from data_driver_example.page.page_login import LoginProxy
from v4.page.page_login import login_proxy


class TestLogin:
    def setup_class(self):
        self.driver = untilDrive.get_drive()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # self.driver.get("http://localhost/litecart/en/")
        self.login_proxy=login_proxy()
    def teardown_class(self):
        self.driver.quit()
    def setup(self):
        # 处理弹出框 方法级别的setup
        self.driver.get("http://localhost/litecart/en/")
        self.driver.refresh()
    @pytest.mark.parametrize("username,password,verify_code,expect_msg",get_case_login_data('./data_driver_example/case_data/login_case_data.json'))
    def test_login_01(self,username,password,verify_code,expect_msg):
        self.login_proxy.hander_login(username,password,verify_code)
        # self.driver.find_element(By.CSS_SELECTOR,'.red').click()
        # #跳转登录页面，用户名为空 密码
        # self.driver.find_element(By.ID,'username').send_keys(" ")
        # self.driver.find_element(By.ID,'password').send_keys("123")
        # self.driver.find_element(By.ID,'verify_code').send_keys("888")
        # self.driver.find_element(By.CSS_SELECTOR,'.J-login-submit').click()
        #断言
        # msg=self.driver.find_element(By.CSS_SELECTOR,'.layui-layer-content').text
        element=By.CSS_SELECTOR,'.layui-layer-content'
        msg=get_msg(element)
        assert expect_msg in msg

