#!_*_coding:utf-8_*_
#__author__:"Alex huang"
import gevent,time
from urllib import request
from gevent import monkey
monkey.patch_all()
def url(url):
    print("GET:%s" %url)
    resp = request.urlopen(url)
    data = resp.read()
    # with open('url.html','wb') as f:
    #     f.write(data)
    print('%d bytes received from %s.' %(len(data),url))

if __name__ == '__main__':
    urls = [
        "https://www.python.org",
        "https://www.cloudflare.com",
        "https://github.com"
    ]
    sync_time = time.time()
    for i in urls:
        url(i)
    print("sync spends time:%s" %int(time.time()-sync_time))
    async_time = time.time()
    gevent.joinall([
        gevent.spawn(url,"https://www.python.org"),
        gevent.spawn(url,"https://www.cloudflare.com"),
        gevent.spawn(url,"https://github.com")
    ])
    print("async spends time:%s" %int(time.time() - async_time))