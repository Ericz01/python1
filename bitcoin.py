import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit('Missing command-line argument')
try:
    bitcoins = float(sys.argv[1])
#if argv[1] given is not a number
except:
    sys.exit('Command-line argument is not a number')

#get the url's content
try:
    request = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = request.json()
    coin_value = response['bpi']['USD']['rate_float']
    total_value = bitcoins * coin_value
    print(f'${total_value:,.4f}')
    
except requests.RequestException:
    sys.exit(f'RequestError {response}')
