import json
import time

from selenium import webdriver

#定义一个获取弹出框的方法
def get_msg(element):
    time.sleep(2)
    #拿到弹出框文本信息
    return untilDrive.get_drive().find_element(*element).text

def get_case_login_data(path_data):
    data_list_total=[]
    with open(path_data, 'r',encoding='utf-8') as f:
        case_data=json.load(f)
    for value_inter in case_data.values():
        data_list_total.append(tuple(value_inter.values()))
    # print(data_list_total)
    return data_list_total
# get_case_login_data('./data_driver_example/case_data/login_case_data.json')
class untilDrive:
    _drive=None
    @classmethod #类方法
    def get_drive(cls):
        if cls._drive is None:
            cls._drive=webdriver.edge()
            cls._drive.maximize_window()
            cls._drive.implicitly_wait(10)
        return cls._drive
    @classmethod
    def quit_driver(cls):
        if cls._drive is not None:
            cls._drive.quit()
            cls._drive = None
