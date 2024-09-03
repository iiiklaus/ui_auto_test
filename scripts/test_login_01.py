import pytest
import requests
from altair.vega import element
from selenium import webdriver
from selenium.webdriver.common.by import By
from untils import get_msg,untilDrive
from test import driver


class TestLogin:
    def setup_class(self):
        self.driver = untilDrive.get_drive()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost/litecart/en/")
    def teardown_class(self):
        self.driver.quit()
    def setup(self):
        # 处理弹出框 方法级别的setup
        self.driver.refresh()
    def test_login_01(self):
        self.driver.find_element(By.CSS_SELECTOR,'.red').click()
        #跳转登录页面，用户名为空 密码
        self.driver.find_element(By.ID,'username').send_keys(" ")
        self.driver.find_element(By.ID,'password').send_keys("123")
        self.driver.find_element(By.ID,'verify_code').send_keys("888")
        self.driver.find_element(By.CSS_SELECTOR,'.J-login-submit').click()
        #断言
        # msg=self.driver.find_element(By.CSS_SELECTOR,'.layui-layer-content').text
        element=By.CSS_SELECTOR,'.layui-layer-content'
        msg=get_msg(element)
        assert "用户名不能为空" in msg

