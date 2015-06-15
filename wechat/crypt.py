import hashlib #
import urllib2 # fetch internet resources

def valid():
    data = request.GET
    token = get_token() # get wechat token
    a = [token, data['timestamp'], data['nonce']];
    a = sorted(tmp)
    a = hashlib.sha1(a)
    if a == data['signature']:
        return True
    else:
        return False


def get_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET'
    req = urllib2.Request(url)
