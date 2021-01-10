import redis
import time

r = redis.Redis(host = '127.0.0.1', port = 6379, db = 0, charset = 'utf8', decode_responses = True)
r.set('mobile', '123')
r.expire('mobile', 1)
time.sleep(1)
print(r.get('mobile'))
