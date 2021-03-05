#__author:jiche
#date: 2020/12/1
import random
import  itchat
import  requests
import time


def get_tuling_response(_info):
    print(_info)
    # 图灵机器人的网址
    api_url = "http://www.tuling123.com/openapi/api"
    data = {
        'key': '5ea0f11b5b6146239c52a47849387484',
        'info': _info,
        'userid':'wechat-robot'
    }
    # 发送数据到指定网址,获取网址返回的数据(字典数据类型)
    res = requests.post(api_url, data).json()
    # print(res, type(res))
    # 给用户返回的内容
    print(res['text'])
    return res['text']


# 时刻监控好友发送的文本消息， 并且给予一个回复，
# isGroupChat=True接收群聊消息中的文本信息， 并让图灵机器人自动回复;
# isMapChat=True接收群聊消息中的文本信息， 并让图灵机器人自动回复;

@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def text_reply(msg):
    # 需求: 只对固定的群聊消息， 实现机器人聊天.

    # 获取好友发送消息的内容
    content = msg['Content']
    # 将好友的消息发送给机器人处理， 处理结果就是返回给好友的消息
    returnContent = get_tuling_response(content)
    time.sleep(random.randint(1,10))
    return  returnContent
if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    itchat.run()
