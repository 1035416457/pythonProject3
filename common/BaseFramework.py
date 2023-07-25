from browsermobproxy import Server
from selenium import webdriver


class BaseFramework(object):

    def __init__(self):
        # 修改下载的文件路径
        self.Server = Server( r"D:\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat" )
        self.Server.start()
        self.proxy = self.Server.create_proxy()  # 打开代理
        self.profile = webdriver.FirefoxProfile()  # 驱动浏览器
        self.profile.set_proxy( self.proxy.selenium_proxy() )
        self.driver = webdriver.Firefox( firefox_profile=self.profile )
        self.driver.implicitly_wait( 10 )  # 设置隐式等待
        self.driver.maximize_window()  # 最大化浏览器


    def process_request(self, request, response):
        pass

    def process_response(self, response, request):
        pass

    def run(self, func, *args):
        self.proxy.new_har(options={'captureContent': True, 'captureHeaders': True, 'captureBinaryContent': True})
        func(*args)
        self.proxy.wait_for_traffic_to_stop( 1, 30 )
        result = self.proxy.har
        for entry in result['log']['entries']:
            request = entry['request']
            response = entry['response']
            self.process_request(request, response)
            self.process_response(response, request)

    def __del__(self):
        self.proxy.close()
        self.browser.close()