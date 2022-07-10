# CryptoPriceAlerts
Price alerts for various cryptocurrencies through the CoinMarketCap Api.

**Features:**
- **Regular updates every 30 minutes** on the price of ETH, BTC, ADA, SOL, XRP, MATIC.
- Added **emergency alerts** - when the price and 24hr percentage change drop below a certain threshold, e.g. Ethereum threshold is $1000, and 24hr % change must be below 7%,(both conditions must be met) an emergency alert will be sent. No typical price alert will be sent after the emergency alert. (exemplar attached below)
- **Price** will be rounded to 0.01, **Market Cap** will be rounded to 0.1, **% Change 24hr** will be rounded to 0.001

**To fix:**
- Finding a fix to constant downtime
