import json
import redis
from common.Cloud import TestBase
from config.function import getConfig
from page.LoginBase import LoginBase
from page.UserBase import UserBase

url = getConfig( "config.ini", "URL", "URL" )
ip = getConfig( "config.ini", "Redis", "host" )
port = getConfig( "config.ini", "Redis", "port" )
password = getConfig( "config.ini", "Redis", "password" )
urlone=  "http://192.168.5.236/lzos/iframe?id=1662073673189691392&isShowMenu=1"
class User(TestBase):
    def test01_lzos_login(self):  # 登录
         """成功登录验证"""
         input = LoginBase( self.driver )
         input.open( url + "/?app-code=lzos&return-url=http%3A%2F%2F192.168.5.236%2Flzos%2F" )
         input.sleep( 5 )  # 显示等待验证码输入框元素出现
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
                 uuid = fhz['data']
                 # 获取接口返回内容

         # return uuid
         # 获取redis配置参数
         # 连接redis 取值
         r = redis.StrictRedis( host=ip, port=port, password=password, decode_responses=True )
         captcha_codes = "lzos:validateCode:{}".format( uuid )
         answer = r.get( captcha_codes )[1:-1]  # 去掉“
         # answer = r.get( captcha_codes )  #不去“”
         input.user_name("nancaladmin")  # 调用页面对象中的方法
         input.pass_word("admin123")
         input.invert_input( answer )
         # input.submit_btn()  # 调用页面对象类中的点击搜索按钮方法
         input.login_btn()
         input.sleep(2)
         # 调用基类截图方法
         try:
             assert (urlone and self.driver.current_url)  # 路径正确"""登录失败"""
             input.get_windows_img()
         except Exception as e:
             input.get_windows_img()
             raise AssertionError( '密码错误登录验证不通过' )

    def test02_Application(self):
        """
        """
        input = UserBase(self.driver)
        #input.move_by_offset(320,165)
        input.sleep(10)
        input.click_BackGround()
        try:
            assert (urlone and self.driver.current_url)
            input.get_windows_img()
        except Exception as e:
            input.get_windows_img()
            raise AssertionError( '未找到后台管理应用' )

    def test03_Ant_menu(self):
            """
            """
            input = UserBase( self.driver )
            input.sleep( 3 )
            # input.move_by_offset(0,100)
            input.click_Ant_Menu()
            try:
                assert ("http://192.168.5.236/lzos/iframe?id=1641275680475848704&isShowMenu=1" and self.driver.current_url)
                input.get_windows_img()
            except Exception as e:
                input.get_windows_img()
                raise AssertionError( '未找到组织结构菜单' )
    def test04_User(self):
            """
            """
            input = UserBase( self.driver )
            input.sleep( 4 )
            # input.move_by_offset(0,100)
            input.click_User()
            try:
                assert ("http://192.168.5.236/lzos/iframe?id=1641275680475848704&isShowMenu=1" and self.driver.current_url)
                input.get_windows_img()
            except Exception as e:
                input.get_windows_img()
                raise AssertionError( '未找到用户管理菜单' )
    def test05_Add_User(self):
            """
            """
            input = UserBase( self.driver )
            #input.sleep( 3 )
            input.move_by_offset(320, 165)
            #input.click()
            #input.click_User()
            #input.click_user_add()
            try:
                assert ("http://192.168.5.236/lzos/iframe?id=1641275680475848704&isShowMenu=1" and self.driver.current_url)
                input.get_windows_img()
            except Exception as e:
                input.get_windows_img()
                raise AssertionError( '未找到用户管理菜单' )
        # input.get_windows_img()  # 调用基类截图方法
        # try:
        #     assert 'selenium' in 'selenium'
        #     print( 'Test Pass.' )
        # except Exception as e:
        #     print( 'Test Fail.', format( e ) )