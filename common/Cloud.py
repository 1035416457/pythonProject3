import unittest
from browsermobproxy import Server
from selenium import webdriver


class TestBase( unittest.TestCase ):
    # setUp()：每个测试方法运行前进行（测试前初始化工作，一条用例执行一次，若N次用例就需要执行N次）
    # tearDown()：每个测试方法运行结束后运行（测试后的清理工作。一条用例执行一次，若N次用例就执行N次）
    # setUpclass()：所有的测试方法运行前运行，为单元测试做前期准备，但必用 @ classmethod装饰器修饰，整个测试过程中只执行一次
    # tearDownClass()：所有的测试方法运行结束后运行，为单元测试做后期清理工作，但必须使用 @ classmethod装饰器进行修饰，整个测试
    @classmethod
    def setUpClass(cls) -> None:
        cls.Server = Server( r"D:\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat" )
        cls.Server.start()
        cls.proxy = cls.Server.create_proxy()  #打开代理
        cls.profile = webdriver.FirefoxProfile()  # 驱动浏览器
        cls.profile.set_proxy( cls.proxy.selenium_proxy() )
        cls.driver = webdriver.Firefox(firefox_profile=cls.profile)
        cls.driver.implicitly_wait( 10 )  # 设置隐式等待
        cls.driver.maximize_window()  # 最大化浏览器
        cls.proxy.new_har( options={'captureContent': True, 'captureHeaders': True, 'captureBinaryContent': True})

    @classmethod
    def tearDownClass(cls) -> None:
          cls.driver.quit()
          cls.proxy.close()




if __name__ == '__main__':
    unittest.main()