from web3 import Web3
import json, datetime, urllib.request, os
from dotenv import load_dotenv
import streamlit as st
from PIL import Image

load_dotenv()
w3 = Web3(Web3.HTTPProvider(os.environ["WEB3_PROVIDER_URI"]))

# Contracts setup
# ABIs
def load_contract():
    with open('build/contracts/Vault.json') as abi_json:
        projects_abi = json.load(abi_json)

    # V2 Addresses
    rush_vault = '0x8B2ec9170DcCF3D11ec43B434aEc8f4070288d95'
    rush_vault = Web3.toChecksumAddress(rush_vault)
        

    # Adding contracts
    contract = w3.eth.contract(rush_vault, abi = projects_abi["abi"])

contract = load_contract()


# image = Image.open('./images/rush_flashloans/rush_flashloans.002.jpeg')
# st.image(image)


st.markdown("# Deploy Vault")

with st.sidebar:
    image = Image.open('./images/carousel.png')
    st.image(image)
    if st.button("name"):
        tx = contract.functions.deploy().call()
        st.write(tx)

#########
#########
###### Wallet connect

from pywalletconnect import WCClient, WCClientInvalidOption
# Input the wc URI
string_uri = input("Input the WalletConnect URI : ")
WCClient.set_wallet_metadata(WALLET_METADATA)  # Optional, else identify pyWalletConnect as wallet
WCClient.set_project_id(WALLETCONNECT_PROJECT_ID)  # Required for v2
try:
    wallet_dapp = WCClient.from_wc_uri(string_uri)
except WCClientInvalidOption as exc:
    # In case error in the wc URI provided
    wallet_dapp.close()
    raise InvalidOption(exc)
# Wait for the sessionRequest info
# Can throw WCClientException "sessionRequest timeout"
req_id, req_chain_id, request_info = wallet_dapp.open_session()
if req_chain_id != account.chainID:
    # Chain id mismatch
    wallet_dapp.close()
    raise InvalidOption("Chain ID from Dapp is not the same as the wallet.")
# Display to the user request details provided by the Dapp.
user_ok = input(f"WalletConnect link request from : {request_info['name']}. Approve? [y/N]")
if user_ok.lower() == "y":
    # User approved
    wallet_dapp.reply_session_request(req_id, account.chainID, account.address)
    # Now the session with the Dapp is opened
else:
    # User rejected
    wclient.reject_session_request(req_id)
    wallet_dapp.close()
    raise UserInteration("user rejected the dapp connection request.")