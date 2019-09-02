import json


def readJsonConfig():
    with open('mirrorConfig.json') as f:
        d = json.load(f)
        return d


def getWeatherConfigData():
    data = readJsonConfig()
    return data["weatherApi"]


def getQuoteConfigData():
    data = readJsonConfig()
    return data["quoteApi"]


def getTrafficConfigData():
    data = readJsonConfig()
    return data["googleTrafficApi"]
