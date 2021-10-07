import config, pandas as pd

def calculateTrade(exchange_price, precision):
    # decimal value of amount of crypto to buy
    amount_purchased = round(config.DOLLAR_AMOUNT / exchange_price, precision)
    
    # price it will set the sell order for this trade
    target_price = exchange_price + (exchange_price * config.PROFIT_GOAL)
    
    # calculate safety buy price
    next_buy_price = exchange_price - (exchange_price * config.SAFETY_ORDER_PERCENT)
    
    # profit amount in dollars
    dollar_profit = round(config.DOLLAR_AMOUNT * config.PROFIT_GOAL, 2)
    
    # decimal amount of crypto to sell
    crypto_sell_amount = round(amount_purchased - ((dollar_profit * config.TAKE_PROFIT_IN_CRYPTO_PERCENT) / exchange_price), precision)
    
    # decimal amount of crypto kept from the trade
    crypto_saved = round(amount_purchased - crypto_sell_amount, precision)
    
    # decimal amount of crypto for the safety order
    next_buy_amount = round(config.DOLLAR_AMOUNT / next_buy_price, precision)

    data = {
        "purchase_price": exchange_price,
        "amount_purchased": amount_purchased,
        "target_price": target_price,
        "next_buy_price": next_buy_price,
        "crypto_sell_amount": crypto_sell_amount,
        "dollar_profit": dollar_profit,
        "crypto_saved": crypto_saved,
        "next_buy_amount": next_buy_amount
    }

    return pd.Series(data)
