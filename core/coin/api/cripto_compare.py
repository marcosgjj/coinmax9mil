from urllib import request


def criptoCompare(apiKey, fsym, tsyms):
    return request.get(f"https://min-api.cryptocompare.com/data/price?fsym={fsym}&tsyms={tsyms}&api_key={apiKey}")