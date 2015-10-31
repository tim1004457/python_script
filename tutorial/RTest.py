__author__ = 'bj'
import redis

r = redis.Redis(host='120.24.163.163', port=6379, password='8pigiou')
target = redis.StrictRedis(host='localhost', port=6379)
keys = r.keys()

for key in keys:
    print key, r.mget(key)

print target.dbsize()