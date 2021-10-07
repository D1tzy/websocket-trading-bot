import websocket, json, pandas as pd
import calculate_trade, config
from binance.client import Client
from binance.enums import * 

binance_url = config.BINANCE_WS_STREAM
currency = config.PAIR_TO_TRADE

successful_trades = 0
lifetime_profit = 0
lifetime_crypto_profit = 0

active_trades = pd.DataFrame()

client = Client(config.API_KEY, config.API_SECRET_KEY, tld=config.tld)

info = client.get_symbol_info(currency)
#print(info)
asset_precision = int(info['quoteAssetPrecision'])


############# ORDER FUNCTIONS ###############

def new_trade(trade):
    market_order(trade['amount_purchased'])

    create_order(SIDE_BUY, trade['amount_purchased'], trade['next_buy_price'])

    create_order(SIDE_SELL, trade['amount_purchased'], trade['target_price'])

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
        print(quantity)
        #ws.close()

def market_order(quantity):
    try: client.create_test_order(
            symbol = config.PAIR_TO_TRADE.upper(),
            side = SIDE_BUY,
            type = ORDER_TYPE_MARKET,
            quantity = quantity
        )
    except Exception as e:
        print(e)
        print(quantity)



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

    best_ask = float(message['a'])

    if len(active_trades) == 0:
        trade = calculate_trade.calculateTrade(best_ask, asset_precision)

        active_trades = active_trades.append(trade, ignore_index = True)
        
        new_trade(trade)

        print('New trade info:')
        print(active_trades.iloc[-1])   


    if best_ask < active_trades.iloc[-1]['next_buy_price'] and len(active_trades) < config.MAX_ACTIVE_TRADES:
        trade = calculate_trade.calculateTrade(active_trades.iloc[-1]['next_buy_price'], asset_precision)

        active_trades = active_trades.append(trade, ignore_index = True)

        safety_trade(trade)
        
        print("Safety order triggered")
        print('New trade info:')
        print(active_trades.iloc[-1])   
        print('Active trades:')    
        print(active_trades)

    if best_ask > active_trades.iloc[-1]['target_price']:
        successful_trades += 1

        print(f"Trade successful! Total successful trades: {successful_trades}.")

        trade = active_trades.iloc[-1]
        lifetime_profit += trade['dollar_profit']
        lifetime_crypto_profit += trade['crypto_saved']

        print(f"Lifetime dollar profit: {lifetime_profit}.")
        print(f"Lifetime crypto profit: {lifetime_crypto_profit}")


        print("Profit info")
        print("Sold {sold} crypto at ${profit_price} for a ${amount} profit. Kept {hodld} crypto".format(
            sold = trade['crypto_sell_amount'],
            profit_price = trade['target_price'],
            amount = trade['dollar_profit'],
            hodld = trade['crypto_saved']
        ))

        active_trades = active_trades.drop([len(active_trades) - 1])

        if len(active_trades) == 0:
            print('All trades completed!')
            print('Starting new trade:')
        else:
            print('Placing buy order for safety order')
            create_order(SIDE_BUY, active_trades.iloc[-1]['next_buy_amount'], active_trades.iloc[-1]['next_buy_price'])
            print('Active trades:')
            print(active_trades)        


############ WEBSOCKET CONTROLS #############
ws = websocket.WebSocketApp(f"{binance_url}{currency}@ticker", 
                            on_open=ws_open, 
                            on_close=ws_close, 
                            on_message=run,
                            on_error=on_error)

ws.run_forever(ping_interval=200)

