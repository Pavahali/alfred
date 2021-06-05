# Not a cog
from aiofile import async_open
from cogs import logs
import json
import os

async def duser(userid):
    async with async_open('./cogs/db.json','r') as f:
        db = json.loads(await f.read())

    del db["users"][userid]

    async with async_open('./cogs/db.json', 'w') as f:
        f.seek(0)
        await f.write(json.dumps(db, indent=4))

    logs.log(f"Deleted user with userid: {userid}")


async def wuser(userid, content):
    async with async_open('./cogs/db.json','r') as f:
        db = json.loads(await f.read())

    if str(userid) in db["users"]:
        db["users"][str(userid)].update(content)
    else:
        db["users"][str(userid)] = content

    async with async_open('./cogs/db.json', 'w') as f:
        f.seek(0)
        await f.write(json.dumps(db, indent=4))

    logs.log(f'changed userinfo for {userid}', '0')


async def ruser(userid):
    userid = str(userid)

    async with async_open('./cogs/db.json', 'r') as f:
        db = json.loads(await f.read())

    if userid in db["users"]:
        return db["users"][userid]
    else:
        await wuser(userid, db["dblook"])
        logs.log(f'created new user for {userid}', '0')

        return db["dblook"]
