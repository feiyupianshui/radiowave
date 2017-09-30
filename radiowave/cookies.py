#!/use/bin/env python
#_*_coding:utf-8_*_
import requests
import json
import redis
import logging
from .settings import REDIS_URL

logger = logging.getLogger(__name__)
reds = redis.Redis.from_url(REDIS_URL, db=2, decode_responses=True)#把账密放到了db2，最后一个参数必须有，不然数据会变成byte形式，那就完全毁了。
login_url = 'http://dbfansub.com/'

def get_cookie(account, password):#获取cookie
    s = requests.Session()
    payload = {
        'log': account,
        'pwd': password,
        'wp-submit': '登录',
        'redirect_to': 'http://dbfansub.com/tvshow/8902.html',
        'testcookie': '1'
    }
    response = s.post(login_url, data=payload)#模拟提交表单
    cookies = response.cookies.get_dict()
    logger.warning('获取Cookie成功！帐号为：%s' %account)
    return json.dumps(cookies)