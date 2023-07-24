import base64


def get_answer():
    # 获取redis配置参数
    auth = base64.b64encode( ("dd970442d9f46b7e07a24fb83d016169").encode( encoding='utf-8' )).decode( encoding="utf-8" )
    print( auth )
    return auth


if __name__ == '__main__':
    print( get_answer() )
