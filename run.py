import os,time
import smtplib
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr, formatdate
from common import HTMLTestRunner
from config.function import getConfig

my_host =getConfig( "config.ini", "mail", "host" ) #邮件代理
my_mail = getConfig( "config.ini", "mail", "username" ) # 发件人邮箱账号
my_pass = getConfig( "config.ini", "mail", "password" )  # 发件人邮箱密码（密钥）
to_mail = getConfig( "config.ini", "mail", "mail_to" ) # 收件人邮箱账号

def creatSuit():
    '''创建测试用例集，加载测试用例：TestSuite'''
    test_units = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(os.getcwd() + '//TestSuite//Test02', pattern = "Case*.py")
    print(discover)
    test_units.addTests(discover)
    return test_units


def mail(now):  #发送邮件
    msg = MIMEMultipart()
    msg['From'] = "{}".format(my_mail)  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] =",".join(to_mail)# 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = "自动化测试测试报告"  # 邮件的主题，也可以说是标题
    msg['Date'] = formatdate()

    report_path =(os.path.join( os.getcwd()+"\\report\\html\\"+ now + "report.html"))
    #report_path =input("D:\PycharmProjects\pythonProject3\report\html\20230712170701report.html")
    file = open(report_path,"rb")
    htlm = file.read()
    file.close()
    #print(htlm)
    part1 = MIMEText(htlm, 'base64', 'utf-8')# 内容, 格式, 编码
    #print(part1)
    part1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    part1["Content-Disposition"] = 'attachment; filename="自动化测试报告.html"'
    part2 = MIMEText( "附件为自动化测试报告" )

    msg.attach( part1 )
    msg.attach( part2 )
    # try:
    #     server = smtplib.SMTP( my_host, 25 )
    # except:
    #     server = smtplib.SMTP_SSL()
    #     server.connect( my_host, 587 )
    server = smtplib.SMTP_SSL( my_host, 465 )  # 发件人邮箱中的SMTP服务器，端口是25
    server.login( my_mail, my_pass )  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail( my_mail, [to_mail], msg.as_string() )  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
if __name__ == "__main__":
    # 获取当前时间，用于命名的html文件名字
    now = time.strftime("%Y%m%d%H%M%S",time.localtime())
    # 根目录
    root_path = os.getcwd()
    file_name = ''.join([root_path + '\\report\\html\\'+ now + "report.html"])
    with open(file_name, "wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
                stream = fp,
                title = "测试报告",
                description = "用例执行情况：",
                tester="小白")

        # 运行测试用例集TestSuite（creatSuit返回值）
        runner.run(creatSuit())
        fp.close() #关闭，必须加不然影响文件读取，关闭
        time.sleep( 10 )
        #mail(now)