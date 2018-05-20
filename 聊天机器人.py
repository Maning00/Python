import itchat
import time
import requests
import hashlib



def get_response(msg, FromUserName):
    api_url = 'http://www.tuling123.com/openapi/api'
    apikey = 'XXXXXXXXXXXXXXXXX'
    
    hash = hashlib.md5()
    userid = hash.update(FromUserName.encode('utf-8'))
    data = {'key': apikey,
            'info': msg,
            'userid': userid
            }
    try:
        req = requests.post(api_url, data=data).json()
        return req.get('text')
    except:
        return



itchat.auto_login()



@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def Tuling_robot(msg):
    respones = get_response(msg['Content'], msg['FromUserName'])
    itchat.send(respones, msg['FromUserName'])


@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    fileDir = '%s%s'%(msg['Type'], int(time.time()))
    msg['Text'](fileDir)
    itchat.send('%s received'%msg['Type'], msg['FromUserName'])
    itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil', fileDir), msg['FromUserName'])
itchat.run()
