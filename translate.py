import json
import requests

def tran(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    response = requests.post(url, data=key)
    if response.status_code == 200:
        return response.text
    else:
        print("有道词典调用失败")
        return None

def reuslt(repsonse):
    result = json.loads(repsonse)
    print ("翻译结果为：%s" % result['translateResult'][0][0]['tgt'])

def translate():
    print("我可以把中文翻译成英文，\n也可以把英文翻译成中文哦")
    word = input('请输入您想要翻译的词或句子：\n\t\t\t\t\t\t')
    list_trans = tran(word)
    reuslt(list_trans)