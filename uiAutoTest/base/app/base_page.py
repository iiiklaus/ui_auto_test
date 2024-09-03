#封装po基类
from selenium.webdriver.support.wait import WebDriverWait

from uiAutoTest.utils import DriverUntil
#对象库层基类封装
class BasePage:
    def __init__(self):
        self.driver=DriverUntil.get_app_driver() #获取app的驱动
    #定义获取元素的方法
    def get_element(self,element):
        return WebDriverWait(self.driver,10,1).until(lambda x:x.find_element(*element))

#操作层基类封装，主要是对一些重复的行为进行封装
class BaseHander:
    def input_text(self,element,text):
        element.clear().send_keys(text)


