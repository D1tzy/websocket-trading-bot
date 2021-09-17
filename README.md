# Trading Bot

## How does it work?

As soon as the bot turns on, it will attempt to get a fill at market value. The trade information will be calculated and put into a pandas dataframe, to help the 
bot keep track of buy and sell levels as well as the amount to buy or sell. If the price dips more than defined by **'SAFETY_ORDER_PERCENT'** in config.py, the
the next buy will have been filled, so the bot will place the newly bought crypto for sale at the price defined by **'PROFIT_GOAL'**, and a new LIMIT order for
the price below **SAFETY_ORDER_PERCENT**.

## Is it risky>

YES!

As you can tell, the bot buys regardless of trend. My thought process behind why this bot may outperform many quantitative trading models is that it sacrifices
capital efficiency in order to capitalize on the voaltile nature of the crypto markets. Essentially, this first version of my bot cures the *retail fallacy* 
of buying high and selling low by essentially admitting that no one can *time* the market, one can only hope to profit on the fluctuations. 

In essence, this bought will always buy low sell high, because **THERE IS NO STOP LOSS**. Although, at the same time, it is also ALWAYS buying the top. Therefore, 
in practice, this script could lose CLOSE TO ALL of your money if the crypto you have it is set to trade crashes 90%+ and your **SAFETY_ORDER_PERCENT** is 
too low compared to your **DOLLAR_AMOUNT** and how much capital you have allocated in total. 

To put it simply remember this. If you have $200 allocated to this bot, and your dollar amount is $20, and your safety order percent is set to .01 (1%), if the
crypto drops just 10% the script will be stuck, and wont be able to execute any more trades. And also you may have just used all your capital buying
the top 10% of a 95%+ crash. Scary thought.

## What is 'take_profit_in_crypto_percent'?

Whenever a trade is executed, that amount of profit will be kept in the crypto traded at current prices

For example:

Lets say your dollar amount is $100, and your target profit is 1%. Your total profit on the trade would be $1. If you leave this variable at its default
value of 50% (.5), then $0.50 will be kept in the crypto for you to keep and sell at your disgression. 

The purpose of this variable is two-fold. First, every sell order executed is a taxable event. Keeping some of your profit in the asset alleviates the tax burden
by not realizing profit, but more on how to get around this entirely late. Second, this allows individuals to accumulate an appreciating asset at essentially no 
true cost to them. For all you stock market geeks out there, think of this as reinvesting dividends but with less steps because you're not even reinvesting, 
you're just keeping what you own and trading it up.

Feel free to use this variable at your disgression. Some of you may want to take profit 100% in cash in order to scale the bot, and then eventually start taking
profit in crypto. Others may believe firmly that cash is trash and want 100% profit in crypto, and just sell enough crypto to cover the initial buy in. 
Regardless, I set this variable up to give flexibility to you, have fun with it. 




# STRATEGY IDEAS

I've already touched on some of these but here are some quick set up strategies:

# PICK YOUR PAIR_TO_TRADE AT YOUR DISGRESSION. THE MORE VOLATILE THE MORE TRADES THAT WILL BE SUCCESSFUL BUT ALSO MORE RISK
# I STRONGLY RECOMMEND PICKING ANY CRYPTO IN THE TOP 10 BY MARKET CAP IF YOU ARE UNSURE OF WHAT MAKES A GOOD CRYPTO PROJECT

## I DONT HAVE ENOUGH CASH, I WANT CASH TO SCALE MY BOTS, REINVEST ELSEWHERE, OR FOR PERSONAL USE

PROFIT_GOAL: .01-.05
SAFETY_ORDER_PERCENT: .01-.1 (I recommend either matching or doubling your PROFIT_GOAL for this variable. Stay prepared for big corrections so dont make this number too small)
TAKE_PROFIT_IN_CRYPTO_PERCENT: 0 (duh you want cash)

## I LIKE CRYPTO BUT I ALSO WANT CASH TO REINVEST OTHER PLACES OR TO USE PERSONALLY

PROFIT_GOAL: .01-.05
SAFETY_ORDER_PERCENT: 0.1-.1
TAKE_PROFIT_IN_CRYPTO_PERCENT: .5

## I ONLY WANT CRYPTO GIVE ME ALL THE CRYPTO

PROFIT_GOAL: .01-.05
SAFETY_ORDER_PERCENT: 0.1-.1
TAKE_PROFIT_IN_CRYPTO_PERCENT: 1



As you can see, the only difference between each strategy is the **TAKE_PROFIT_IN_CRYPTO_PERCENT**. After watching a similar bot work for a couple months,
I've found (personally) that it doesn't make much of a difference how high you set your profit goal, in fact it could hurt you if you set it too high, and 
an order just barely doesn't get filled. The only thing to be sure of is that every trade's profit is MORE than: (total profit - crypto take profit) - taxes - trading fees. 

This would be a lot easier to calculate if taxes didnt exist, so lets make them disappear.



# The Self-Directed Roth Ira

This financial instrument could potentially save you hundreds of thousands in taxes by retirement. By contributing to this account, and letting this script
trade with the cash in that account, every trade will be tax free, AND when you go to take it out at retirement, THOSE earnings are tax free too. Therefore,
all you need to worry about is being more profitable than the trading fees, allowing you to work profitably with much lower capital - ALTHOUGH YOU WILL NOT
HAVE ACCESS TO THIS MONEY OUTSIDE OF THIS ACCOUNT UNTIL THE AGE OF 65 OR OVER WITHOUT INCURRING POSSIBLY VERY STEEP EARLY WITHDRAWAL FEES.

HOWEVER. The cash profit in this account can easily be reinvested into the stock market, forex markets, and a very large array of alternative investments, as allowed
by the US government. This gives the user the ability to easily re-balance their portfolio after allowing the script to build up some capital without being 
punished by taxes or huge transfer fees.



# FUTURE GOALS FOR THE BOT

As the code stands, you COULD run multiple scripts for multiple crypto pairs. However, as more scripts get added and more orders go into the order book, eventually
the exchange doesnt allow you to have any more orders, and with the dataframes for each crypto across multiple scripts, it would be difficult to define which
order(s) make the most sense to delete. To fix this issue, I plan to integrate multi-crypto trading functionality in a single script, (hopefully) up to 5 or more at a 
time, to allow the user to trade multiple pairs without having to run multiple instances simultaneously. 

I also hope to integrate smart downside protection, to protect capital already invested, and to mitigate the downside of always buying the top. To implement this,
I dont plan to actually 'short' the crypto, as there are added fees and risk to that. Instead, I'll simply have the bot sell a portion of what is already owned,
and place an order to buy it back lower. I think that the short side trades will be implemented with a stop loss, so that we lose out on cash not crypto, however
maybe I'll implement a boolean value to toggle the stop loss on or off. Possibly one for the whole feature, for those people who dont believe in selling crypto.

Eventually I also hope to bring in stock market and forex market options using this strategy, as I think it could work very well in those markets as well if 
implemented properly. Then I'll give the user the ability to select multiple assets across multiple markets to trade using this strategy in the config.py.

Then, once I have all the data from all the markets, I'll probably begin to host a database for the repo to hold my own data and build out an api for the 
instances to retrieve data from. The databases will also hold the users accounts info for each instance, opening the door for things like margin trading, 
which would be extremely useful for the next step when we apply machine learning models to change the dollar amount per trade depending on market conditions.

And finally, I hope to add some machine learning models to the bot to dynamically change the amount bought or sold depending on its confidence that the
trade will be successful. Hopefully this will result in the bot putting more money into trades that are successful quicker, and less money into ones that arent
successful for days or weeks. Going along with these models, if the bot is EXTREMELY confident, it could even use some margin to try and amplify those gains even
more in a quick timeframe. It would probably be smart to have a tight stop loss to take the margin out early as well, but then leave the rest of the position
as the trade.
