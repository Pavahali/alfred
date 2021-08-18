# All settings
import os

version = 1.0

db = './info/database.db'
logs = './info/logs.log'

token = os.getenv("ALFRED")
pinglimit = 5

logchannels = (18044439939645444, 856065877106884628)
cogs = (
    'cogs.guilds',
    'cogs.events',
    'cogs.status',
    'cogs.admin',
    'cogs.comms',
    'cogs.users'
)
