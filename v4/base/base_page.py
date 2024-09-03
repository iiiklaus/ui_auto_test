#定义一个对象库层的基类
from altair.vega import element
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

import untils
class BasePage:
    def __init__(self):
        #浏览器驱动
        self.driver=untils.untilDrive.get_drive()
    #基类的元素定位
    """
    location:定位元素的方法
    就是添加了时间等待
    """
    def get_element(self,location):
        wait=WebDriverWait(self.driver,10,1)
        return wait.until(lambda x:x.find_element(*location))

#定义操作层的基类
class BaseHander:
    # def __init__(self):
    #     self.element=BasePage()
    # def input_text(self,text):
    #     element_input=self.element.get_element()
    #     element_input.clear()
    #     element_input.send_keys(text)
    def input_text(self,element_input,text):
        element_input.clear().send_keys(text)