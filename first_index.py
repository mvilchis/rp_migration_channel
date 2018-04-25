from utils import *

keys = sorted(USERS.keys(), key = lambda x: (len(x),x))

for u in keys:
    add_user_db(USERS[u]["phone"], USERS[u]["name"], u)
