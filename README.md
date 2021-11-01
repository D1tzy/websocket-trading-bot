# Trading Bot

## How does it work?

In the config.py folder you will find some config variables. 'DOLLAR_AMOUNT' is the easiest variable, its how many dollars on every trade it will put in. Note this assumes you are using USD or some USD stablecoin. Adjust your amount if you are using a different base currency. 'SAFETY_ORDER_PERCENT' is the percent below last filled price the bot will place a new order. The default value for this variable is .01 (1%), therefore buying every 1% dip, but can be changed to fit any strategy. Every buy order filled is considered a new position, and a corresponding sell order 'PROFIT_GOAL'% above the filled price is placed. There is another variable called 'TAKE_PROFIT_IN_CRYPTO_PERCENT' that allows you to keep some of your profit in the crypto it is trading. For example, if before you sell every position is up $4, and TAKE_PROFIT_IN_CRYPTO_PERCENT is set to .25 (25%) then it will keep $1 in the crypto allowing for future appreciation while simultaneously profiting you in fiat/stablecoins/whatever base crypto you are using as a pairing.

This bot looks to capitalize on volatility and does not operate with any stop loss feature. As a safety feature, there is a 'MAX_ACTIVE_TRADES' variable that allows you to limit how many open trades the bot can have. You can set this value to infinity, or some insanely high number, but please keep in mind the bot also does not cancel orders once theyve been placed. This is a problem as most exchanges have a max open orders allowed, so eventually you'd be blocked by your exchange from placing more orders. 

You can change the crypto pair you are trading using the 'PAIR_TO_TRADE' variable. Input the pairing all lowercase, no special characters, no spaces. If you aren't from the us and not using binance.us, you will need to change the 'tld' variable to 'com' or your country's tld. For example Japan has a special tld, 'jp'.

## How do you plan to improve this repository

One possible way to improve the strategy would be to apply technical indicators and only buy in uptrends or at reversals and then possibly to operate with a stop loss to ensure you're using as much capital on these trades. Another way would be to apply support and resistance levels and buy in the support area and then sell out and stop buying when it approaches the resistance area. 

However, my theory is that getting too fancy trying to beat the market will only burn you in the long run. I personally really like this script the way it is, however, I do plan to bring more strategies and features to this bot. I plan to bring a front end in using react to display performance metrics and allow you to change config.py settings in real time, stop loss active trades, and an option to redeem all or a portion of your crypto profit saved up. I also need to apply canceling orders that were never filled, and to cancel sell orders when the active trades gets too close to the max orders allowed by the exchange so that we don't get blocked from placing orders.

## Is it profitable?

I plan to run this script in my IRA account, so every trade will be tax free. Coupled with low trading fees, this bot should absolutely remain profitable. The only way it wouldn't be would be if the crypto it's trading crashed and never recovered. That's why I only plan to run it on things like Bitcoin, Ethereum, Cardano, Chainlink, that have been around awhile and very likely have a big future in the world. On top of that, the ones I've listed are all fixed in supply, meaning every trade I profit more of a finite asset that I can then hold and allow to appreciate. 

