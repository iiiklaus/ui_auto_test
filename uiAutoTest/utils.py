#工具类
"""
1、建立连接
"""
from selenium import webdriver
from appium import webdriver as appdrive
import time
#自媒体的驱动
class DriverUntil:
    _drive=None
    _mis_driver=None #管理后端浏览器驱动
    _app_driver=None #app的驱动
    _mis_quit=True
    @classmethod
    def get_drive(cls):
        if cls._drive is None:
            cls._drive=webdriver.Chrome()
            cls._drive.maximize_window()
            # cls._drive.implicitly_wait(10)
            cls._drive.get("http://ttmp.research.itcast.cn/")
        return cls._drive
    @classmethod
    def quit_driver(cls):
        if cls._drive is not None:
            cls.get_drive().quit()
            cls._drive = None
    @classmethod
    def get_mis_driver(cls):
        if cls._mis_driver is None:
            cls._mis_driver=webdriver.Chrome()
            cls._mis_driver.maximize_window()
            cls._mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls._mis_driver
    @classmethod
    def get_mis_quit(cls):
        if cls._mis_driver is None and cls._mis_quit:
            cls.get_mis_driver().quit()
            cls._mis_driver = None
    #qpp驱动
    @classmethod
    def get_app_driver(cls):
        if cls._app_driver is None:
            des_dict = dict()
            des_dict["platforName"] = "android"
            des_dict["platformVersion"] = "5.1"
            des_dict["deviceName"] = "192.168.56.101:5555"
            des_dict["appPackage"] = "com.itcast.toutiaoApp"
            des_dict['appActivity'] = ".MainActivity"
            des_dict["noReset"] = True
            des_dict['unicodeKeyboard'] = True
            des_dict['resetKeyboard'] = True
            cls._app_driver = appdrive.Romte("http://localhost:4723/wd/hub", des_dict)
        return cls._app_driver
    @classmethod
    def quit_app_driver(cls):
        if cls._app_driver is not None:
            cls._app_driver.quit()
            cls._app_driver = None
def select_channel(driver,element,channel):
    element.click()
    time.sleep(0.5)
    find_xpath = f"//*[@class='el-select-dropdown wrap el-scrollbar wrap' ]//*[text()='{channel}']"
    driver.find_element_by_xpath(find_xpath).click()
#封装一个方法判断元素是否存在
def is_exist(driver,text):
    """
    :param driver: 浏览器驱动
    :param text: 定位元素的文本内容
    :return:
    """
    xpath_find=f"//*[contains(text(),'{text}')]"
    try:
        time.sleep(0.5)
        return driver.find_element_by_xpath(xpath_find)
    except Exception as e:
        return False