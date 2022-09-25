from brownie import accounts, network, RushToken, Registry, yRush
import click


def deploy_y_rush():
    click.echo(f"You are using the '{network.show_active()}' network")
    dev = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    click.echo(f"You are using: 'dev' [{dev.address}]")

    print(f"Dev is deploying yRush ..")
    tx = yRush.deploy(RushToken[-1], Registry[-1], {'from' :dev})
    return tx

def main():
    deploy_y_rush()