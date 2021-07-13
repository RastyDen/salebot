import random
from random import randint
import json

def handle(data):

    data = list('abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~@#$%&*')
    random.shuffle(data)
    paswd = ''.join([random.choice(data) for x in range(6)])
    sl = {"kod":f"{paswd}"}
    return json.dumps(sl)


