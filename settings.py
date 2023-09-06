from random import choice

active_breweries = 'active_breweries.json'
inactive_breweries = 'inactive_breweries.json'
active_breweries_details = 'active_breweries_details.json'
inactive_breweries_details = 'inactive_breweries_details.json'

# list of user agents for randomising
useragent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

headers = {
    'User-Agent': choice(useragent_list),
    'Content-Type': 'text/plain; charset=utf-8',
    'Accept-Language': 'en-GB,en;q=0.5',
}

base_url = 'https://www.ratebeer.com'

countries = [

    {
        'name': 'Northern Ireland',
        'code': '238'
    },
    {
        'name': 'England',
        'code': '240'
    },
    {
        'name': 'Scotland',
        'code': '241'
    },
    {
        'name': 'Wales',
        'code': '239'
    },
]
