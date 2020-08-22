import os
import environ
from functions import backup, restore

env = environ.Env()
environ.Env.read_env()

DATABASE_SOURCE = env.db('DATABASE_SOURCE')
DATABASE = env.db('DATABASE')

backup(DATABASE_SOURCE)
restore(DATABASE)
