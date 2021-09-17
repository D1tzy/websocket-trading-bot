import config

def calculateTrade(exchange_price):
    amount_purchased = config.DOLLAR_AMOUNT / exchange_price
    target_price = exchange_price + (exchange_price * config.PROFIT_GOAL)
    next_buy_price = exchange_price - (exchange_price * config.SAFETY_ORDER_PERCENT)
    dollar_profit = config.DOLLAR_AMOUNT * config.PROFIT_GOAL
    crypto_sell_amount = amount_purchased - (dollar_profit / exchange_price)
    crypto_saved = amount_purchased - crypto_sell_amount
    next_buy_amount = config.DOLLAR_AMOUNT / next_buy_price

    return {
        "purchase_price": exchange_price,
        "amount_purchased": amount_purchased,
        "target_price": target_price,
        "next_buy_price": next_buy_price,
        "crypto_sell_amount": crypto_sell_amount,
        "dollar_profit": dollar_profit,
        "crypto_saved": crypto_saved,
        "next_buy_amount": next_buy_amount
    }     