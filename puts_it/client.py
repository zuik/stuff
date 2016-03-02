import requests
import time

URL = 'http://localhost:5000/'
def post_msg(what, by_who, time=time.time()):
    payload = {
        'content':what,
        'user':by_who,
        'time':time
    }
    r = requests.post(URL+'putMsg', data=payload)

def get_msg(id):
    r = requests.get(URL+'getMsg', params={'id':id})
    return r.text
def get_all_msg():
    r = requests.get(URL+'getMsg/all')
    return r.text
if __name__ == '__main__':
    while True:
        d = input('Type your messages here: ')
        if d.split()[0] == 'get':
            if d.split()[1] == 'all':
                print(get_all_msg())
            else:
                print(get_msg(int(d.split()[1])))
        else:
            post_msg(d.encode('utf-8'), 'Nobody')
