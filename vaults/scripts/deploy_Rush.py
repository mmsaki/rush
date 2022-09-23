from brownie import Registry, accounts, network, RushToken

import click

def deploy_rush_token():
    click.echo(f"You are using the '{network.show_active()}' network")
    dev = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    click.echo(f"You are using: 'dev' [{dev.address}]")

    print(f"Dev is deploying Registry ..")
    tx = deploy_rush_token("Rush®", "®🎠", 6000, dev)
    return tx

def main():
    deploy_rush_token()

def get_registry():
    return Registry[-1]

