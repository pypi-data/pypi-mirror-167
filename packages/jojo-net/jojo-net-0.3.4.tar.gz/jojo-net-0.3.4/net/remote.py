from net import Http
import requests
import json


class Remote:
    def __init__(self, url):
        self.url = url

    def call(self, func_name, *args, **kwargs):
        data = kwargs  # .encode('utf-8')
        print(data)
        response = Http.post(self.url + func_name, data)
        # response = Http.get(self.url + func_name + '?name=ok')
        if response.status_code == 200:
            # print(response.text)
            return response.json()


api = Remote("http://127.0.0.1/")
ret = api.call("dict", name="Sam")
print(type(ret), ret)

