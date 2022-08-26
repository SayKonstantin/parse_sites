from environs import Env

env = Env()
env.read_env()
HOST = env.str('HOST')
PORT = env.int('PORT')
USER = env.str('USER')
PASSWORD = env.str('PASSWORD')
DATABASE = env.str("DATABASE")
