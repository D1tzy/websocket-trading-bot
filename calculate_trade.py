import config, pandas as pd

def calculateTrade(exchange_price):
    amount_purchased = round(config.DOLLAR_AMOUNT / exchange_price, 8)
    target_price = exchange_price + (exchange_price * config.PROFIT_GOAL)
    next_buy_price = exchange_price - (exchange_price * config.SAFETY_ORDER_PERCENT)
    dollar_profit = config.DOLLAR_AMOUNT * config.PROFIT_GOAL
    crypto_sell_amount = round(amount_purchased - ((dollar_profit * config.TAKE_PROFIT_IN_CRYPTO_PERCENT) / exchange_price), 8)
    crypto_saved = round(amount_purchased - crypto_sell_amount, 8)
    next_buy_amount = round(config.DOLLAR_AMOUNT / next_buy_price, 8)

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
