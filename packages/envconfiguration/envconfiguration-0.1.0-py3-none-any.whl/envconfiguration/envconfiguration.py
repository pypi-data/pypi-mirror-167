from dotenv import dotenv_values
from os import environ, getenv, getcwd, walk
from os.path import join, exists, dirname, abspath
from sys import argv


class Configure:

    def getEnvFiles():

        root_path = abspath(dirname(argv[0]))
        env_files = []

        for root, dirs, files in walk(root_path):
            for file in files:
                if file.endswith('.env'):
                    env_files.append(join(root, file))

        return env_files

    def loadConfigFromEnviroment():

        for name, value in environ.items():
            globals()[f'{name}'] = value

    def loadConfigFromFiles(env_file):

        config = dotenv_values(env_file) if exists(env_file) else ()

        for name in config:
            globals()[f'{name}'] = config[name]
