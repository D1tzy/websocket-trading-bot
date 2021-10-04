try:
    import local
except:
    None

####################################################################
# IF YOU ARE NOT FROM THE US
# set tld to 'com' below
# Some countries still require a regional tld, such as Japan
# It is up to you to figure out if this is required for your region
####################################################################

tld = 'us'


# Link to the Binance data stream
# DO NOT CHANGE THIS LINE
BINANCE_WS_STREAM = f"wss://stream.binance.{tld}:9443/ws/"

# Crypto pair to trade
# MUST be lowercase with no special characters
# If the bot fails to start, try switching the order of your pairing
# For example:
# btcusdt is valid but usdtbtc wont return any data
# Default: Bitcoin-USDT pairing
PAIR_TO_TRADE = "btcusdt"

# Dollar amount to be used per trade
# Default: $20
DOLLAR_AMOUNT = 100

# Percent profit goal per trade
# Default: 1%
PROFIT_GOAL = .0001

# Percent the bot will place the next limit order below last filled price
# For example: 
# Last trade price is 50000. A safety order percent of 1% would mean the bot places the order at 49,500
# If that order gets filled, the bot places a new limit order 1% below that, so 49005, etc
# Default: 1%
SAFETY_ORDER_PERCENT = .0001

# Percentage of profit to be kept in crypto
# For example:
# Lets say your 'dollar_profit_amount' for the trade is $1
# If this is set to 50%, the bot will keep $0.5 of the crypto at the current rates and sell the rest
# Default: 50%
TAKE_PROFIT_IN_CRYPTO_PERCENT = .5

# Maximum active trades your bot will have open at a time
# Use this value as a pseudo stop-loss to prevent your bot from buying every
# dip in the event of a major crash or correction
# Default: 20 trades
MAX_ACTIVE_TRADES = 20

# Change these values to your API keys
# Make sure not to get them switched up
API_KEY = local.API_KEY
API_SECRET_KEY = local.API_SECRET_KEY
