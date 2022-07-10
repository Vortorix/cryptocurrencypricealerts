import requests
from requests import Request, Session
import json
import pprint
import time
from dhooks import Webhook, Embed
import math

def round_nearest_to(x, a):
    return round(round(x / a) * a, -int(math.floor(math.log10(a))))

alertlogo = 'https://cdn.corporatefinanceinstitute.com/assets/stock-market-crash.jpeg'

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

parameters = {
        "slug": "solana",
        "convert": "USD"
}

headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY':''
    }

hook = Webhook('')

solanalogo = 'https://www.cityam.com/wp-content/uploads/2021/08/Solana-1.jpg'

while True:

    responsecontent = requests.get(url, params= parameters, headers= headers)
    pprint.pprint(json.loads(responsecontent.text))
    price = (json.loads(responsecontent.text)['data']['5426']['quote']['USD']['price'])
    marketcap = (json.loads(responsecontent.text)['data']['5426']['quote']['USD']['market_cap'])
    percentchange24hr = (json.loads(responsecontent.text)['data']['5426']['quote']['USD']['percent_change_24h'])

    price = round_nearest_to(price, 0.01)
    marketcap = round_nearest_to(marketcap, 0.1)
    percentchange24hr = round_nearest_to(percentchange24hr, 0.001)

    if price < 30 and percentchange24hr < -7:
        alertembed = Embed( 
            description= (f'The current price of Solana (SOL) is: **${price}**. This dip may be the beginning of a crash. Use this oppurtunity to sell or buy!'),
            color= 0x5CDBF0,
            timestamp= 'now'
        )
        alertembed.set_author(name= 'SOL Emergency Alert')
        alertembed.set_thumbnail(alertlogo) 
        alertembed.set_footer(text='CoinMarketCap', icon_url = 'https://i.imgur.com/RCdZEvS.png')
        alertembed.add_field(name= 'Market Capitalization:', value= ('$' + str(marketcap)))
        alertembed.add_field(name= '% Change 24hr', value= str(percentchange24hr) + '%')

        hook.send(embed=alertembed)
        time.sleep(1800)
        break
           
    embed = Embed( 
        description= (f'The current price of Solana (SOL) is: **${price}**'),
        color= 0x5CDBF0,
        timestamp= 'now'
        )

    embed.set_author(name= 'SOL Price')
    embed.set_thumbnail(solanalogo)
    embed.set_footer(text='CoinMarketCap', icon_url = 'https://i.imgur.com/RCdZEvS.png')
    embed.add_field(name= 'Market Capitalization:', value= ('$' + str(marketcap)))
    embed.add_field(name= '% Change 24hr', value= str(percentchange24hr) + '%')

    hook.send(embed=embed)
    time.sleep(1800)

