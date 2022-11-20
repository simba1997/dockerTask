from flask import Flask
import requests
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)



@app.route("/")
def home():
    
    while True:
        bitCoinPrice = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD').json()['USD']
        
        updatedBitcoinPrice = requests.get('https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=9').json()['Data']['Data']
        sum=0
        for updatedPrice in updatedBitcoinPrice:
            sum+=updatedPrice['open']
        
        
        
        
        
        price = float((bitCoinPrice))
        average_price = float(sum/10)
        cache.set('RealtimePrice', price)
        cache.set('Average', average_price)
        return """
    <meta http-equiv="refresh" content="5" >
    <h1>Realtime BitCoin Price: {}$</h1><br> <h1>The Avg price in the last 10 mins:
        {}$ </h1>""".format(price,average_price)


def averagePrice_ten_min():
    updatedBitcoinPrice = requests.get('https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=9').json()['Data']['Data']
    sum=0
    for updatedPrice in updatedBitcoinPrice:
        sum+=updatedPrice['open']
    return (sum/10)
