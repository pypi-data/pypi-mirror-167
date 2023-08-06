from .envconfiguration import Configure

if __name__ == 'envconfiguration':

    Configure.loadConfigFromEnviroment()
    
    for env_file in Configure.getEnvFiles():
        Configure.loadConfigFromFiles(env_file)
    
    for name in envconfiguration.__dict__:
        globals()[f'{name}'] = envconfiguration.__dict__[name]