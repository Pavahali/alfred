# Not a cog
import json
from cogs import logs
import os

def wuser(userid, content):
    with open('./cogs/db.json','r') as f:
        db = json.load(f)

    if str(userid) in db["users"]:
        db["users"][str(userid)].update(content)
    else:
        db["users"][str(userid)] = content
        
    with open('./cogs/db.json', 'w') as f:
        json.dump(db,f, indent=4)

    logs.log(f'changed userinfo for {userid}', '0')


def ruser(userid):
    userid = str(userid)

    with open('./cogs/db.json') as f:
        db = json.load(f)

    if userid in db["users"]:
        return db["users"][userid]
    else:
        wuser(userid, db["dblook"])
        logs.log(f'created new user for {userid}', '0')

        return db["dblook"]
