from scripts.vaults.helper_functions import *
from brownie import Vault, RushToken, rToken, Strategy, Registry, RushSimpleFlashLoan, RushFlashLoan


def all_vaults():
    print(f" {'====='*10} ")
    print(f"Rush Vault Tokens")
    for i in range(0, len(Vault)):
        print(f"{Vault[i]} {' '*5} {Vault[i].name()} {' '*5} {Vault[i].symbol()} ")

def all_rush_tokens():
    print(f" {'====='*10} ")
    print(f"Native Rush Tokens ")
    for i in range(0, len(RushToken)):
        print(f"{RushToken[i]} {' '*5} {RushToken[i].name()} {' '*5} {RushToken[i].symbol()}")

def all_r_tokens():
    for i in range(0, len(rToken)):
        print(f"{rToken[i]} {' '*5} {rToken[i].name()} {' '*5} {rToken[i].symbol()}")

def strategy():
    print(f" {'====='*10} ")
    print(f"Strategy")
    for i in range(0, len(Strategy)):
        print(f"{Strategy[i]}")

def registries():
    print(f" {'====='*10} ")
    print(f"Registry addressses")
    for i in range(0, len(Registry)):
        print(f"{Registry[i]} {' '*5} ")

def flashloan_multi_contracts():
    print(f" {'====='*10} ")
    print(f"Flashloan Contracts")
    for i in range(0, len(RushFlashLoan)):
        print(f"{RushFlashLoan[i].address} {' '*5}")

def flashloan_simple_contracts():
    for i in range(0, len(RushSimpleFlashLoan)):
        print(f"{RushSimpleFlashLoan[i].address} {' '*5}")

def main():
    all_rush_tokens()
    all_vaults()
    all_r_tokens()
    flashloan_multi_contracts()
    flashloan_simple_contracts()
    strategy()
    registries()