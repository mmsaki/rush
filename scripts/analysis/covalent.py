import os
import requests
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd

path = Path('./.env')
load_dotenv(path)

API_KEY = os.getenv('COVALENT_API_KEY')

base_url = 'https://api.covalenthq.com/v1'
chain_id = '1'
contract = "0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9"

## Flashloan Topic
topic = "0x631042c832b07452973831137f2d73e395028b44b250dedc5abb0ee766e168ac"
starting_block = "15010291"
ending_block = "15613530"

def get_flashloan_topics(chain_id, address):
    endpoint = f'/{chain_id}/events/topics/{topic}/?quote-currency=USD&format=JSON&starting-block={starting_block}&ending-block={ending_block}&sender-address={contract}&key={API_KEY}'
    url = base_url + endpoint
    data = requests.get(url).json()
    df = pd.DataFrame(data["data"]["items"])
    del df["decoded"]
    return(df)

# Request
get_flashloan_topics(chain_id, contract)