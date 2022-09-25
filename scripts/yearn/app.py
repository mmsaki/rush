from brownie import accounts, network, config
import streamlit as st
from PIL import Image

from web3 import Web3
w3 = Web3()


if st.button("Aave Balances"):
    st.write("Hello")