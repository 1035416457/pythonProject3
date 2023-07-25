import sys
import redis

import cx_Oracle
def get_answer():
    # 获取redis配置参数
    ip = '192.168.5.214'
    port = '6379'
    password = '1@#4'
    uuid = 'st!5olyfbng40lc'

    # 连接redis 取值
    r = redis.StrictRedis(host=ip, port=port, password=password, decode_responses=True)
    captcha_codes = "mp:validatecode:{}".format(uuid)
    answer = r.get(captcha_codes)[1:-1]


    return answer

if __name__ == '__main__':
    print(get_answer())