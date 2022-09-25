from brownie import Registry, accounts, network
import click

click.echo(f"You are using the '{network.show_active()}' network")
dev = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
click.echo(f"You are using: 'dev' [{dev.address}]")
url = "https://goerli-optimism.etherscan.io/tx/{}"

def deploy_registry():
    print(f"Dev is deploying Registry ..")
    tx = Registry.deploy({"from": dev})

    print("View your tx here: " + url.format(tx.txid))
    return tx


def set_gov():
    gov = dev
    tx = Registry[-1].setGovernance(dev, {"from": gov})

    print("View your tx here: " + url.format(tx.txid))
    return tx

def accept_gov():
    gov = dev
    tx = Registry[-1].acceptGovernance({"from": gov})
    
    print("View your tx here: " + url.format(tx.txid))
    return tx


def main():
    deploy_registry()
    set_gov()
    accept_gov()
    ascii_art()

def ascii_art():

    print(f"""
    
                               /$$                                            
                              | $$                                            
  /$$$$$$  /$$   /$$  /$$$$$$$| $$$$$$$           /$$$$$$   /$$$$$$   /$$$$$$ 
 /$$__  $$| $$  | $$ /$$_____/| $$__  $$ /$$$$$$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  \__/| $$  | $$|  $$$$$$ | $$  \ $$|______/| $$  \__/| $$$$$$$$| $$  \ $$
| $$      | $$  | $$ \____  $$| $$  | $$        | $$      | $$_____/| $$  | $$
| $$      |  $$$$$$/ /$$$$$$$/| $$  | $$        | $$      |  $$$$$$$|  $$$$$$$
|__/       \______/ |_______/ |__/  |__/        |__/       \_______/ \____  $$
                                                                     /$$  \ $$
                                                                    |  $$$$$$/
                                                                     \______/ 
    
    
    """)
