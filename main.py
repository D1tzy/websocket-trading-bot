import websocket, json, pandas as pd
import calculate_trade as calculateTrade
from binance.client import Client
from binance.enums import *
import config

binance_url = config.BINANCE_WS_STREAM
currency = config.PAIR_TO_TRADE

successful_trades = 0
lifetime_profit = 0
lifetime_crypto_profit = 0

active_trades = pd.DataFrame(columns = ['purchase_price', 
                                        'target_price', 
                                        'next_buy_price', 
                                        'amount_of_crypto',
                                        'crypto_to_be_sold',
                                        'crypto_to_be_hodld',
                                        'dollar_profit_amount'])

client = Client(config.API_KEY, config.API_SECRET_KEY, tld=config.tld)

info = client.get_symbol_info(config.PAIR_TO_TRADE)
asset_precision = info['quoteAssetPrecision']


############# ORDER FUNCTIONS ###############

def new_trade(trade, price):
    create_order(SIDE_BUY, float(f"{{:{asset_precision + 1}f}}".format(trade['amount_purchased'])), price)

    create_order(SIDE_BUY, float(f"{{:{asset_precision + 1}f}}".format(trade['next_buy_amount'])), trade['next_buy_price'])

    create_order(SIDE_SELL, float(f"{{:{asset_precision + 1}f}}".format(trade['crypto_sell_amount'])), trade['target_price'])


def safety_trade(trade):
    create_order(SIDE_BUY, trade['next_buy_amount'], trade['next_buy_price'])

    create_order(SIDE_SELL, trade['crypto_sell_amount'], trade['target_price'])


def create_order(side, quantity, price):
    print('trying')
    try:
        order = client.create_test_order(
            symbol = config.PAIR_TO_TRADE.upper(),
            side = side,
            type = ORDER_TYPE_LIMIT,
            timeInForce = TIME_IN_FORCE_GTC,
            price = price,
            quantity = quantity
        )

        print("Order created:")
        print(order)
    except Exception as e:
        print(e)
        #ws.close()



############ WEBSOCKET ############

def ws_open(ws):
    print("Bot started")

def ws_close(ws):
    print("Bot stopped")

def on_error(ws, event):
    print(event)


def run(ws, message):
    global active_trades, successful_trades, lifetime_profit, lifetime_crypto_profit

    message = json.loads(message)

    if len(active_trades) == 0:
        price = float(message['a'])
        
        trade = calculateTrade.calculateTrade(price)

        active_trades = active_trades.append({'purchase_price': trade['purchase_price'], 
                                                'target_price': trade['target_price'], 
                                                'next_buy_price': trade['next_buy_price'],
                                                'amount_of_crypto': trade['amount_purchased'],
                                                'crypto_to_be_sold': trade['crypto_sell_amount'],
                                                'crypto_to_be_hodld': trade['crypto_saved'],
                                                'dollar_profit_amount': trade['dollar_profit']
                                                }, 
                                                ignore_index = True)
        

        print(f"{{:{asset_precision + 1}f}}".format(trade['next_buy_amount']))
        new_trade(trade, price)

        print('New trade info:')
        print(active_trades.iloc[-1])   


    if float(message['a']) < active_trades.iloc[-1]['next_buy_price']:
        trade = calculateTrade.calculateTrade(active_trades.iloc[-1]['next_buy_price'])

        active_trades = active_trades.append({'purchase_price': trade['purchase_price'], 
                                                'target_price': trade['target_price'], 
                                                'next_buy_price': trade['next_buy_price'],
                                                'amount_of_crypto': trade['amount_purchased'],
                                                'crypto_to_be_sold': trade['crypto_sell_amount'],
                                                'crypto_to_be_hodld': trade['crypto_saved'],
                                                'dollar_profit_amount': trade['dollar_profit']
                                                }, 
                                                ignore_index = True)
        
        safety_trade(trade)
        
        print("Safety order triggered")
        print('New trade info:')
        print(active_trades.iloc[-1])   
        print('Active trades:')    
        print(active_trades)

    if float(message['a']) > active_trades.iloc[-1]['target_price']:
        successful_trades += 1
        trade = active_trades.iloc[-1]
        lifetime_profit += trade['dollar_profit_amount']
        lifetime_crypto_profit += trade['crypto_to_be_hodld']

        print(f"Trade successful! Total successful trades: {successful_trades}.")
        print(f"Lifetime dollar profit: {lifetime_profit}.")
        print(f"Lifetime crypto profit: {lifetime_crypto_profit}")


        print("Profit info")
        print("Sold {sold} crypto at ${profit_price} for a ${amount} profit. Kept {hodld} crypto".format(
            sold = trade['crypto_to_be_sold'],
            profit_price = trade['target_price'],
            amount = trade['dollar_profit_amount'],
            hodld = trade['crypto_to_be_hodld']
        ))

        active_trades = active_trades.drop([len(active_trades) - 1])

        if len(active_trades) == 0:
            print('All trades completed!')
            print('Starting new trade:')
        else:
            print('Active trades:')
            print(active_trades)

        

ws = websocket.WebSocketApp(f"{binance_url}{currency}@ticker", 
                            on_open=ws_open, 
                            on_close=ws_close, 
                            on_message=run,
                            on_error=on_error)
ws.run_forever()

