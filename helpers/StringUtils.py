class StringUtils:
    @staticmethod
    def replaceAllStringForValue(value, strToReplace, symbol):
        return value.replace(strToReplace, symbol)

    @staticmethod
    def getStringToUpperCase(value):
        return value.upper()

    @staticmethod
    def getStringToLowerCase(value):
        return value.lower()
