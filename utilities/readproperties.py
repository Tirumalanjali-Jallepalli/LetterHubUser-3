import configparser

config = configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')


class Readdata:
    @staticmethod
    def applicationurl():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def username():
        username = config.get('common info', 'email')
        return username

    @staticmethod
    def password():
        password = config.get('common info', 'id')
        return password


