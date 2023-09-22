from configparser import ConfigParser

def read_configuration(category,key):
    config=ConfigParser()
    config.read("C:\\Users\\Srikanth Chelukala\\PycharmProjects\\practNinja\\Configurations\\config.ini")
    return config.get(category,key)
