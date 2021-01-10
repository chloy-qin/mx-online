import requests
import json


# 发送单条短信,apikey是注册的时候，网址给的，这是针对云片网写的方法
def send_single_sms(apikey, code, mobile):
    url = "https://sms.yunpian.com/v2/sms/single_send.json"
    text = "".format(code)
    res = requests.post(url, data = {
        'apikey': apikey,
        'mobile': mobile,
        'text': text,
    })
    re_json = json.loads(res.text)
    return re_json


# 调用发送单条短信方法
if __name__ == '__main__':
    res = send_single_sms('', '', '')  # 分别填写参数
    import json
    res_json = json.load(res.text)
    code = res_json['code']
    msg = res_json['msg']
    if code == 0:
        print('发送成功')
    else:
        print('发送失败：{}'.format(msg))

    print(res.text)