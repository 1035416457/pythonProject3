import json
import time
import redis
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver import ActionChains

from config.function import getConfig
uuid = ''
answer = ''
# 代理服务监控返
Server = Server( r"D:\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat" )
Server.start()
proxy = Server.create_proxy()

#火狐浏览器
profile = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)

#谷歌浏览器
# chrome 调用 browsermob-proxy 方法
# chrome_options = Options()
# chrome_options.add_experimental_option('w3c', False)
# chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
# driver = webdriver.Chrome(chrome_options=chrome_options)
# #chrome_options = webdriver.ChromeOptions()
#t = '-proxy-server={0}'
#f=t.format(proxy.proxy)
#print(f)
#h=chrome_options.add_argument(f)
#print(h)
#chrome_options.add_argument('-proxy-server={0}'.format())
#print(t)
# https需要加上，要不然回报安全连接问题
#chrome_options.add_argument('--ignore-certificate-errors')
# 配置了驱动的环境变量，否则需要写入驱动地址driver_path
##print(driver)
#time.sleep(10)
URL = getConfig("config.ini", 'URL', 'url')
print(URL+"/?app-code=lzos&return-url=http%3A%2F%2F192.168.5.236%2Flzos%2F")
s=proxy.new_har("cs", options={'captureContent': True, 'captureHeaders': True, 'captureBinaryContent': True})
driver.get(URL+"/?app-code=lzos&return-url=http%3A%2F%2F192.168.5.236%2Flzos%2F")
time.sleep(3)

#class1 = driver.find_element_by_class_name('login-btn')
#class1.click()
#time.sleep(3)
#driver.switch_to_window(driver.window_handles[-1])  # 重新获取页面
print(driver.title)#当前页的名称
#driver.find_element_by_class_name('pwd').click()
print(s)
#driver.find_element_by_class_name('imgbox > images').click()
#driver.find_element_by_class_name('justify-center').click()
time.sleep(1)
proxy.wait_for_traffic_to_stop(1, 30)
result = proxy.har
#print(result)
time.sleep(1)
# print(result['logs']['entries'])
#for entry in result['logs']['entries']:
   # _url = entry['request']['url']
    # 根据URL找到数据接口
    #if "/code" in _url:
    #    _response = entry['response']
        #print(_response)
     #   time.sleep(1)
    #    _content = _response['content']['text'] #提取返回值
    #    fhz = json.loads(_content)data
        #转换成json格式
     #   uuid = fhz['uuid']
        # 获取接口返回内容
#print(uuid)
for entry in result['log']['entries']:
    _url = entry['request']['url']
    # 根据URL找到数据接口
    if "/levault/usrsvr/Usr/GetToken" in _url:
        _response = entry['response']
        print(_response)
        _content = _response['content']['text']#提取返回值
        fhz = json.loads(_content)
        #转换成json格式
        uuid = fhz['data']
        # 获取接口返回内容
print(uuid)

# 获取redis配置参数
ip = "192.168.5.236"
port = "6379"
password = '1@#4'
# return uuid
# 连接redis 取值
r = redis.StrictRedis(host=ip, port=port, password=password, decode_responses=True)
#后厂造
#captcha_codes = "captcha_codes:{}".format(uuid)
#乐造
captcha_codes = "lzos:validateCode:{}".format( uuid )
answer = r.get( captcha_codes )[1:-1]  # 去掉“
# answer = r.get( captcha_codes )  #不去“”
print(answer)
# if answer != "":
#     print("获取验证码成功")
# else:
#     print("获取验证码失败")
# time.sleep(3)
#乐造登录
driver.find_element_by_class_name('user-name > .w-full').send_keys('nancaladmin')
driver.find_element_by_xpath("//input[@type='password']").send_keys('admin123')
driver.find_element_by_class_name('verification-code > input').send_keys(answer)
driver.find_element_by_xpath("//button[contains(.,'登录')]").click()
time.sleep(3)
#driver.set_window_size(1920,1080)
#后台给
driver.find_element_by_xpath("//footer/div/div/div/div[3]").click()
time.sleep(2)
driver.find_element_by_xpath("//li[2]/div/span/span[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//span[contains(., '用户管理')]").click()
time.sleep(2)
ActionChains(driver).move_by_offset(320, 165).click().perform() # 鼠标左键点击， 200为x坐标， 100为y坐标
#BOM
# driver.find_element_by_class_name('application_list_wrap:nth-child(5) > .list').click()
#数据字典
#driver.find_element_by_class_name('application_list_wrap:nth-child(4) .text').click()
time.sleep(3)

#driver.window_handles(0)
#定位iframe
#driver.switch_to_frame(0)

# driver.switch_to_frame(driver.find_element_by_xpath('/html/body/div[1]/div/div/div[Test03]/div[Test03]/div/div/iframe'))
# driver.find_element_by_class_name('bom-new-Item').click()
#driver.switch_to_frame(0)

#driver.find_elements_by_css_selector('ant-btn:nth-child(1)')

#后厂造登录
# driver.find_element_by_class_name('co-mobile').send_keys('18500810918')#输入用户名
# driver.find_element_by_xpath("//input[@type='password']").send_keys('admin123')#输入密码
# driver.find_element_by_class_name('pwd-code > .code').send_keys(answer)#输入验证码
# driver.find_element_by_class_name('el-button').click()#点击登录
