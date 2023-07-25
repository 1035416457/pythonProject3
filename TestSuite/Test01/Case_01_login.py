import json
import time

import redis
from page.LoginBase import LoginBase
from common.Cloud import TestBase
from config.function import getConfig
url = getConfig( "config.ini", "URL", "URL" )
ip = getConfig( "config.ini", "Redis", "host" )
port = getConfig( "config.ini", "Redis", "port" )
password = getConfig( "config.ini", "Redis", "password" )
uuid=''
urlone=  "http://192.168.5.236/lzos-login/?app-code=lzos&return-url=http%3A%2F%2F192.168.5.236%2Flzos%2F"
class lzoslogin(TestBase):

    def test01_lzos_login(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。打开登录页面。
        :return:打开登录页面
        """
        input = LoginBase( self.driver )
        input.open(url+"/?app-code=lzos&return-url=http%3A%2F%2F192.168.5.236%2Flzos%2F")
        input.sleep(5) #显示等待验证码输入框元素出现
        try:
            assert '乐造OS2.0' in self.driver.title
            input.get_windows_img()
            #print( '打开登录页面成功')
        except Exception as e:
            input.get_windows_img()
            #print( '打开登录页面异常', format( e ) )
            raise AssertionError( '未打开乐造OS2.0登录页面' )
    def test02_lzos_login(self):
        """登录名不存在"""
        input = LoginBase( self.driver )
        #input.clear_user_name()
        input.user_name( "4444" )  # 调用页面对象中的方法
        input.pass_word( "admin123" )
        #input.invert_input( 99 )
        # input.submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        input.login_btn()
        # 调用基类截图方法
        try:
            assert ( urlone and self.driver.current_url )
            input.get_windows_img()
            #print( '登录名不存在登录验证通过' )
        except Exception as e:
            input.get_windows_img()
            raise AssertionError( '登录名不存在验证不通过' )
    def test03_lzos_login(self):
        """密码错误"""
        input = LoginBase( self.driver )
        input.clear_user_name()
        input.user_name( "nancaladmin" )  # 调用页面对象中的方法
        input.pass_word( "admin123456" )
        #input.clear_input()  # 清除输入验证码
        input.contains_btn()  # 换一张验证码
        self.proxy.wait_for_traffic_to_stop( 1, 3000 )
        result = self.proxy.har
        for entry in result['log']['entries']:
            _url = entry['request']['url']
            # 根据URL找到数据接口
            if "/levault/usrsvr/Usr/GetToken" in _url:
                _response = entry['response']
                # print( _response )
                _content = _response['content']['text']  # 提取返回值
                fhz = json.loads( _content )
                # 转换成json格式
                global uuid
                uuid = fhz['data']
                # 获取接口返回内容

        # return uuid
        # 获取redis配置参数
        # 连接redis 取值
        r = redis.StrictRedis( host=ip, port=port, password=password, decode_responses=True )
        captcha_codes = "lzos:validateCode:{}".format( uuid )
        answer = r.get( captcha_codes )[1:-1]  # 去掉“
        # answer = r.get( captcha_codes )  #不去“”
        # input.user_name("nancaladmin")  # 调用页面对象中的方法
        # input.pass_word("admin123")
        input.invert_input( answer )
        # input.submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        input.login_btn()
        # 调用基类截图方法
        try:
            assert ( urlone and self.driver.current_url )  # 路径正确"""登录失败"""
            input.get_windows_img()
        except Exception as e:
            input.get_windows_img()
            raise AssertionError( '密码错误登录验证不通过' )
    def test04_lzos_login(self):
        """验证码错误登录"""
        time.sleep(3)
        input = LoginBase( self.driver )
        #input.user_name( "nancaladmin" )# 调用页面对象中的方法
        input.clear_pass_word()
        input.pass_word( "admin123" )
        input.invert_input( 99 )
        # input.submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        input.login_btn()
        # 调用基类截图方法
        try:
            assert ( urlone and self.driver.current_url )  # 路径正确"""登录失败"""
            input.get_windows_img()
        except Exception as e:
            input.get_windows_img()
            raise AssertionError( '验证码错误登录验证不通过' )



    def test05_lzos_login(self):#登录
        """成功登录验证"""
        input = LoginBase( self.driver )
        #input.click_input()#双击验证码
        input.clear_input()#清除输入验证码
        input.contains_btn()#换一张验证码
        # self.proxy.wait_for_traffic_to_stop( 1, 3000 )
        # result=self.proxy.har
        # for entry in result['log']['entries']:
        #     _url = entry['request']['url']
        #   # 根据URL找到数据接口
        #     if "/levault/usrsvr/Usr/GetToken" in _url:
        #         _response = entry['response']
        #         #print( _response )
        #         _content = _response['content']['text']  # 提取返回值
        #         fhz = json.loads( _content )
        #         # 转换成json格式
        #         uuid = fhz['data']
        #         # 获取接口返回内容

        # return uuid
        # 获取redis配置参数
        # 连接redis 取值
        r = redis.StrictRedis( host=ip, port=port, password=password, decode_responses=True )
        captcha_codes = "lzos:validateCode:{}".format( uuid )
        answer = r.get(captcha_codes)[1:-1] #去掉“
        #answer = r.get( captcha_codes )  #不去“”
        #input.user_name("nancaladmin")  # 调用页面对象中的方法
        #input.pass_word("admin123")
        input.invert_input(answer)
        #input.submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        input.login_btn()
        # 调用基类截图方法
        time.sleep(5)
        try:
            assert ("http://192.168.5.236/lzos/" and self.driver.current_url) # 路径正确"""登录成功"""
            input.get_windows_img()
            #print( '登录成功')
        except Exception as e:
            input.get_windows_img()
            raise AssertionError( '登录失败' )
        # 调用基类截图方法
        #input.item_btn()
        #print(self.driver.title)
        # try:
        #     assert 'http://192.168.5.236/lzos/' in self.driver.current_url
        #     print( 'Test Pass.登录成功' )
        # except Exception as e:
        #     print( 'Test Fail.', format( e ) )
    #


