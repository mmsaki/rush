import os
import requests
from dotenv import load_dotenv
from pathlib import Path

path = Path('./.env')
load_dotenv(path)

API_KEY = os.getenv('COVALENT_API_KEY')

base_url = 'https://api.covalenthq.com/v1'
blockchain_chain_id = '420'
demo_address = "0x2a33a67E6e11F43256B36f57F55F273Ea864052d"

def get_wallet_balance(chain_id, address):
    endpoint = f'/{chain_id}/address/{address}/balances_v2/?key={API_KEY}'
    url = base_url + endpoint
    result = requests.get(url).json()
    data = result["data"]
    print(data)
    return(data)


# Example address request
get_wallet_balance(blockchain_chain_id, demo_address)