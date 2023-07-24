import json
import time

from common.BaseFramework import BaseFramework


class Framework(BaseFramework):

    def load(self, url):
        self.driver.get(url)
        time.sleep(3)

    def process_request(self, request, response):
        pass

    def process_response(self, response, request):
        # print(request['url'])
        # 找到你所需数据的url即可快乐的解析数据了
        if '/levault/usrsvr/Usr/GetToken' in request['url']:
            text = response['content']['text']
            text_dict = json.loads(text)
            data_result = text_dict['data']
            return data_result




if __name__ == '__main__':
    Framework = Framework()
    Framework.run( Framework.load, 'http://192.168.5.233/lzos-login/?app-code=lzos&return-url=http%3A%2F%2F192.168.5.233%2Flzos%2F' )
