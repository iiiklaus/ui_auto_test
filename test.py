from appium import webdriver
#初始化app的配置信息
des_dict=dict()
des_dict["platforName"]="android"
des_dict["platfor]Version"]="5.1"
des_dict["deviceName"]="192.168.56.101:5555"
des_dict["appPackage"]="com.android.settings"
des_dict["platforName"]=".Settings"
driver=webdriver.Romte("http://localhost:4723/wd/hub",des_dict)

driver.quit()