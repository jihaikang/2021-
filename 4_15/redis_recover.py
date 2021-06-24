import redis
try:
    r = redis.Redis() # Redis到这里把，要用的时候在回顾吧15. April 2021 04:57PM
    r.set('name','pig')
    print(r[name]) #  name 'name' is not defined 



except Exception as e:
    print(e)