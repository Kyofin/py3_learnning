#!/usr/bin/env python3

"""
python3
使用钉钉发送告警信息
"""
import json
import requests


def send_msg(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",  # 发送消息类型为文本
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,  # 不@所有人
        },
        "text": {
            "content": msg,  # 消息正文
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text


if __name__ == '__main__':
    msg = '业务告警 1'
    reminders = []
    url = ''
    print(send_msg(url, reminders, msg))
