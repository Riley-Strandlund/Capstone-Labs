import requests
from pprint import pprint

coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

def main():
    data = get_api()
    print(data)
    bitcoin_amount = user_input()
    exchange_rate = identify_exchange_rate(data)
    bitcoin_amount_in_dollars = dollar_value_of_bitcoin(exchange_rate, bitcoin_amount)
    ux(bitcoin_amount, bitcoin_amount_in_dollars)

def get_api():
    return requests.get(coindesk_url).json()


def identify_exchange_rate(data):
    return data['bpi']['USD']['rate_float']

def user_input():
    while True:
        try:
            bitcoin_amount = float(input('Enter the number of bitcoins: '))
            if bitcoin_amount > 0:
                return bitcoin_amount
            else:
                print('Enter positive number.')
        except ValueError:
            print('Is this ^ even a number?')

def dollar_value_of_bitcoin(bitcoin_amount, exchange_rate):
    return bitcoin_amount * exchange_rate

def ux(bitcoin_amount, bitcoin_amount_in_dollars):
    print(f'{bitcoin_amount} Bitcoin is equivalent to ${bitcoin_amount_in_dollars}')


if __name__ == '__main__':
    main()