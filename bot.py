import krakenex
import json
import time
import datetime
import calendar

#51:41

def get_crypto_data(pair, since):
    return api.query_public('OHLC', data={'pair': pair, 'since': since})['result'][pair]

def analyze(pair, since):
    data = get_crypto_data(pair, since)
    lowest = 0
    highest = 0

    for prices in data:
        balance = get_fake_balance()
        last_trade = get_last_trade()


        open_ = float(prices[1])
        high_ = float(prices[2])
        low_ = float(prices[3])
        close_ = float(prices[4])

def get_balance():
    return api.query_private('Balance')

def get_fake_balance():
    with open ('balance.json','r') as f:
        return json.load(f)

def get_last_trade(pair):
    trades_history = get_fake_trades_history()

    last_trade = {}

    for trade in trades_history:
        trade = trades_history[trade]
        if trade['pair'] == pair and trade['type'] == 'buy':
            last_trade = trade
    return last_trade

def get_fake_trades_history():
    with open('tradeshistory.json', 'r') as f:
        return json.load(f)['result']['trades']

def get_trades_history():
    start_date = datetime.datetime(2022,1,1)
    end_date = datetime.datetime.today()
    return api.query_private('TradesHistory', req(start_date, end_date,1))['result']['trades']

def date_nix(str_date):
    return calendar.timegm(str_date.timetuple())

def req(start, end, ofs):
    req_data = {
        'type':'all',
        'trades':'true',
        'start':str(date_nix(start)),
        'end':str(date_nix(end)),
        'ofs':str(ofs)
    }
    return req_data

if __name__ == '__main__':
    api = krakenex.API()
    api.load_key('kraken.key')
    pair = "XETHZUSD"
    since = str(int(time.time() - 3600))

    analyze(pair)

    print(json.dumps(get_fake_trades_history(),indent=4))

