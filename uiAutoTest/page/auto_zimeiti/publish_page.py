#这是发表页面
from uiAutoTest.base.mp.base_page import BasePage,BaseHander
from selenium.webdriver.common.by import By
from uiAutoTest.utils import DriverUntil,select_channel,is_exist
class PublishPage(BasePage):
    def __init__(self):
        super().__init__()
        #找元素
        self.tile=By.XPATH,'//*[@placeholder="文章名称"]'
        self.iframe=By.ID,'publishTinymce_ifr'
        # 文章内容输入框
        self.content = By.CSS_SELECTOR, ".mce-content-body "
        # 封道选择
        self.cover = By.XPATH, "//*[@role='radiogroup']/label[4]/span[2]"
        self.chanel = By.XPATH,"//*[@placeholder='请选择']"
        # 发表按钮
        self.publish_btn = By.CSS_SELECTOR, "[class='el-button filter-item el-button--primary']"
    def find_title(self):
        return self.get_element(self.tile)
    def find_iframe(self):
        return self.get_element(self.iframe)
    def find_context(self):
        return self.get_element(self.content)
    def find_chanel(self):
        return self.get_element(self.chanel)
    def find_cover(self):
        return self.get_element(self.cover)
    def find_publish_btn(self):
        return self.get_element(self.publish_btn)
class PublishHandler(BaseHander):
    def __init__(self):
        self.publish_page=PublishPage()
        self.driver=DriverUntil.get_drive()
    def title_input(self,title):
        self.input_text(self.publish_page.find_title(),title)
    #输入文章内容
    def content_input(self,content):
        #切换到iframe当中
        self.driver.switch_to.frame(self.publish_page.find_iframe())
        self.input_text(self.publish_page.find_context(),content)
        #切回页面
        self.driver.switch_to.default_content()
    #封面的操作
    def cover_select(self):
        self.publish_page.find_cover().click()
    #频道选择
    def channel_select(self,channel):
        select_channel(self.driver,self.publish_page.find_chanel(),channel)
    #点击发表按钮
    def publish_btn(self):
        self.publish_page.find_publish_btn().click()
class PublishProxy:
    def __init__(self):
        self.publish_handler=PublishHandler()
    def publish_content(self,title,content,channel):
        self.publish_handler.title_input(title)
        self.publish_handler.content_input(content)
        self.publish_handler.cover_select()
        self.publish_handler.channel_select(channel)
        self.publish_handler.publish_btn()

