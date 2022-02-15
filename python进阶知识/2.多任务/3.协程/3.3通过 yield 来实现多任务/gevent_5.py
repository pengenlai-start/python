"""
gevent 的使用案例
"""

import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name, img_url):  # img_url 是图片源
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(img_name, 'wb') as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "C:\\Users\\penge\\Desktop\\downloader.jpg", "https://www.baidu.com/img/flexible/logo/pc/result.png")
    ])


if __name__ == "__main__":
    main()
