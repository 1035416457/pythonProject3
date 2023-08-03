import json
import time
from selenium.common.exceptions import NoAlertPresentException, NoSuchWindowException, NoSuchFrameException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import os.path


# 创建一个日志实例
from common.Logger import Logger
logger = Logger( logger="BasePage" ).getlog()


class BasePage( object ):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法
    """

    def __init__(self, driver):
        self.driver = driver

        # get an url link


    def open(self, url):
        """

        :rtype: object
        """
        self.driver.get( url )
        # quit browser and end testing
    def quit_browser(self):
        self.driver.quit()

        # 浏览器前进操作

    def forward(self):
        self.driver.forward()
        logger.info( "Click forward on current page." )

        # 浏览器后退操作

    def back(self):
        self.driver.back()
        #logger.info( "Click back on current page." )

        # 显示等待
    def wait(self, loc, seconds):
        try:
            wait_ = WebDriverWait( self.driver, seconds )
            wait_.until( lambda driver: driver.find_element( *loc ) )
            logger.info( "wait for %d seconds." % seconds )
        except NameError as e:
            logger.error( "Failed to load the element with %s" % e )

        # 保存图片

    def get_windows_img(self):
        """
        把file_path保存到我们项目根目录的一个文件夹.\\report\\images
        """
        file_path = os.path.dirname( os.path.abspath( '.' ) + '/report/images/')
        rq = time.strftime( '%Y%m%d%H%M%S', time.localtime( time.time() ) )
        screen_name = file_path+'/' + rq + '.png'
        print( screen_name )
        try:
            self.driver.get_screenshot_as_file( screen_name )
            logger.info( "Had take screenshot and save to folder : /report/images/" )
        except NameError as e:
            logger.error( "Failed to take screenshot! %s" % e )
            self.get_windows_img()

    def find_element(self, loc):
        """
        :return: element
        """
        return self.driver.find_element( *loc )

        # 输入

    def send_keys(self, selector, text):

        el = self.find_element( selector )
        el.click()
        try:
            el.send_keys( text )
            logger.info( "Had type \\' %s \\' in inputBox" % text )
        except NameError as e:
            logger.error( "Failed to select in input box with %s" % e )
            self.get_windows_img()

        # 清除文本框

    def clear(self, selector):
        el = self.find_element( selector )
        #el.click()
        try:
            #el.clear()
            #el.send_keys( Keys.RIGHT)  # 光标向右移方便删除
            el.send_keys( Keys.CONTROL + 'a' )  #全选
            el.send_keys( Keys.BACKSPACE )  # 删除键
            logger.info( "Clear text in input box before typing." )
        except NameError as e:
            logger.error( "Failed to clear in input box with %s" % e )
            self.get_windows_img()

    # 点击元素
    def click(self, selector):
        el = self.find_element( selector )
        try:
            el.click()
            #logger.info( "The element \\'%s\\' was clicked." % el.text )
        except NameError as e:

           logger.error( "Failed to click the element with %s" % e )

    # 鼠标双击
    def double_click(self, selector):
        '''双击事件'''
        el = self.find_element( selector )
        try:
            ActionChains( self.driver ).double_click( el).perform()
        except NameError as e:
            logger.error( "Failed to click the element with %s" % e )

    # def move_by_offset(self, xoffset, yoffset, value, name="xpath"):
    #     """
    #     按住鼠标滑动
    #     :param xoffset: 横坐标
    #     :param yoffset: 纵坐标
    #     :param value: 元素路径
    #     :param name: 定位方法
    #     """
    #     el = self.driver.find_element(name, value)
    #     try:
        #         ActionChains(self.driver).drag_and_drop_by_offset(el, xoffset, yoffset).perform()
    #         # logger.info( "The element \\'%s\\' was move_by_offset" % el.text )
    #     except NameError as e:
    #
    #         logger.error( "Failed to move_by_offset the element with %s" % e )
    #
    #     # 鼠标移动到某个坐标
    # move_by_offset( xoffset, yoffset ) ：鼠标从当前位置移动到某个坐标（需要获取到目标位置的位置坐标）
    #
    # move_to_element( to_element ) ：鼠标移动到某个元素
    #
    #  move_to_element_with_offset( to_element, xoffset, yoffset ) ：移动到距某个元素（左上角坐标）多少距离的位置
    #点击按钮
    def move_by_offset(self, x, y):
        try:
            ActionChains( self.driver).move_by_offset( x, y ).click().perform()
        except Exception as e:
             # logger.error( "Failed to click move_element with %s" % e )
            self.get_windows_img()
    #输入
    def move_by_offset_keys(self, x, y,text):
        try:
            ActionChains( self.driver).move_by_offset( x, y ).click().send_keys(text).perform()
        except Exception as e:
             # logger.error( "Failed to click move_element with %s" % e )
            self.get_windows_img()
    def move_to_element_with_offset(self,selector, x, y):
        el = self.find_element( selector )
        try:
            ActionChains( self.driver ).move_by_offset( el,x, y ).click().perform()
        except Exception as e:
            # logger.error( "Failed to click move_element with %s" % e )
            self.get_windows_img()
        # 强制等待

    def switch_frame(self, loc):
        """
        多表单嵌套切换
        :param loc: 传元素的属性值
        :return: 定位到的元素
        """
        try:
            return self.driver.switch_to_frame( loc )
        except NoSuchFrameException as msg:
            logger.error("查找iframe异常-> {0}".format(msg))

    def switch_windows(self,loc):
        """
        多窗口切换
        :param loc:
        :return:
        """
        try:
            return self.driver.switch_to_window(loc)
        except NoSuchWindowException as msg:
            logger.error("查找窗口句柄handle异常-> {0}".format(msg))

    def switch_alert(self):
        """
        警告框处理
        :return:
        """
        try:
            return self.driver.switch_to_alert()
        except NoAlertPresentException as msg:
            logger.error("查找alert弹出框异常-> {0}".format(msg))

    def script(self, src):
        """
        提供调用JavaScript方法
        :param src: 脚本文件
        :return: JavaScript脚本
        """
        return self.driver.execute_script( src )

    @staticmethod
    def sleep(seconds):
        time.sleep( seconds )
        logger.info( "Sleep for %d seconds" % seconds )