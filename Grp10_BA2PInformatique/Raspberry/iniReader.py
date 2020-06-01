import ConfigParser

class IniReader:
    # shortcut to get config key value in config.ini
    @staticmethod
    def read(section, key):
        parser = ConfigParser.ConfigParser()
        parser.read('config.ini')
        return parser.get(section, key)