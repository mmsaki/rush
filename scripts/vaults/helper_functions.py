from brownie import rToken, RushToken, Registry, Vault, network, config, accounts, interface
import click


def get_dev_account():
    click.echo(f"You are using the '{network.show_active()}' network")
    dev = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    click.echo(f"You are using: 'dev' [{dev.address}]")

def get_gov_account():
    click.echo(f"You are using the '{network.show_active()}' network")
    gov = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    click.echo(f"You are using: 'gov' [{gov.address}]")

def deploy_registry(gov):
    return Registry.deploy({"froms": gov})

def get_registry(i):
    return Registry[i]

def set_gov(registry, gov):
    return Registry.setGovernance(gov, {'from': gov})
    
def accept_gov(registry, gov):
    return Registry.acceptGovernance({'from': gov})

def deploy_vault(dev):
    return Vault.deploy({"from": dev})


def new_release(registry, vault, gov):
    return registry.newRelease(vault, {'from': gov})

def new_experimental_vault(token, registry, vault, gov, guardian, rewards, custom_name, custom_symbol, release):
    print(f"{registry.newExperimentalVault.info()}")
    return registry.newExperimentalVault(token, gov, guardian, rewards, custom_name, custom_symbol, release, {'from': gov})

def tag_vault(registry, vault, name, gov):
    return registry.tagVault(vault, name, {'from': gov})


def endorse_vault(registry, vault, gov):
    return registry.endorseVault(vault, 0,{'from': gov})


def new_vault(token, guardian, registry, vault, gov):
    return registry.newVault(vault, {'from': gov})

def deploy_strategy(strategy, vault, gov):
    return strategy.deploy(vault, {'from': gov})

def add_vault_strategy(strategy, vault):
    return 

def get_vault(i):
    return Vault[i]

def get_vaults_address():
    for i in range(0, len(Vault)):
        print(Vault[i])

def intialize_r_vault(vault, token_in, gov, rewards, nameOverride, symbolOverride, guardian, management):
    print(f"{vault.initialize.info()}")
    tx = vault.initialize(token_in, gov, rewards, nameOverride, symbolOverride, guardian, management, {'from': gov})
    return tx

def set_deposit_limit(vault, amount, gov):
    return vault.setDepositLimit(amount, {'from': gov})

def deploy_rush_token(name, symbol, total_supply, dev):
    return RushToken.deploy(name, symbol, total_supply, {"from":  dev})

def get_rush_token(i):
    return RushToken[i]

def get_wrapped_token(i):
    return rToken[i]

def get_token(token_name):
    token_address = config["networks"][network.show_active()][token_name]
    token = interface.IERC20Metadata(token_address)
    return token

def deploy_r_token_wrapper(token, registry, dev):
    return rToken.deploy(token, registry, {'from': dev})

def approve_token_to_vault(token, vault, amount, token_owner):
    return token.approve(vault, amount, {'from': token_owner})

def deposit_to_vault(vault, amount, recipient):
    return vault.deposit(amount, recipient, {'from': recipient})

def withdraw_from_vault(vault, amount, recipient, max_loss):
    return vault.withdraw(amount, recipient, max_loss, {'from': recipient})





