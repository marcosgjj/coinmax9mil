from re import A
from core.coin.api.cripto_compare import criptoCompare
from core.coin.api.import_key import importKey


apiKey = importKey("apiKey.key")

BTC = criptoCompare(apiKey, fsym="BTC", tsyms="USD")
ETH = criptoCompare(apiKey, fsym="ETH", tsyms="USD")
BNB = criptoCompare(apiKey, fsym="BNB", tsyms="USD")
XRP = criptoCompare(apiKey, fsym="XRP", tsyms="USD")
USDT = criptoCompare(apiKey, fsym="USDT", tsyms="USD")
USDC = criptoCompare(apiKey, fsym="USDC", tsyms="USD")
ADA = criptoCompare(apiKey, fsym="ADA", tsyms="USD")
BUSD = criptoCompare(apiKey, fsym="BUSD", tsyms="USD")
SOL = criptoCompare(apiKey, fsym="SOL", tsyms="USD")
DOGE = criptoCompare(apiKey, fsym="DOGE", tsyms="USD")
DOT = criptoCompare(apiKey, fsym="DOT", tsyms="USD")
SHIB = criptoCompare(apiKey, fsym="SHIB", tsyms="USD")
XMR = criptoCompare(apiKey, fsym="XMR", tsyms="USD")
LTC = criptoCompare(apiKey, fsym="LTC", tsyms="USD")
CHZ = criptoCompare(apiKey, fsym="CHZ", tsyms="USD")
XLM = criptoCompare(apiKey, fsym="XLM", tsyms="USD")
VET = criptoCompare(apiKey, fsym="VET", tsyms="USD")
FIL = criptoCompare(apiKey, fsym="FIL", tsyms="USD")
ATOM = criptoCompare(apiKey, fsym="ATOM", tsyms="USD")


print(f"Bitcoin: {BTC.content}")
print(f"Ethereum: {ETH.content}")
print(f"BNB: {BNB.content}")
print(f"XRP: {XRP.content}")
    