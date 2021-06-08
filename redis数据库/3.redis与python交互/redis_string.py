from redis import *

if __name__ == '__main__':
    # 创建一个 StrictRedis 对象，链接 redis 数据库
    try:
        sr = StrictRedis()
        # res = sr.set('name', 'pel')
        # print(res)
        # res = sr.set('name','pel666')
        # name = sr.get('name')
        # print("name= %s" % name)
        # res = sr.delete('name')
        # print(res)
        print(sr.keys())
    except Exception as e:
        print(e)
