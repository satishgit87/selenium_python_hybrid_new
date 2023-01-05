import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationUrl():
        url = config.get("COMMON INFO", "baseURL")
        return url

    @staticmethod
    def getUserName():
        userName = config.get("COMMON INFO", "userName")
        return userName

    @staticmethod
    def getPassword():
        password = config.get("COMMON INFO", "password")
        return password