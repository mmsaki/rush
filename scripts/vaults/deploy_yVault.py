from brownie import Vault, accounts, network
import click

def deploy_vault():
    click.echo(f"You are using the '{network.show_active()}' network")
    dev = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    click.echo(f"You are using: 'dev' [{dev.address}]")
    print(f"Dev is Deploy yVault ..")
    Vault.deploy({"from": dev})
    return 

def main():
    deploy_vault()
