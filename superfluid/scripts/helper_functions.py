from brownie import config, interface, network, accounts

def get_account():
    account = accounts.add(config["wallets"]["from_key"]) 
    return account

def get_accounts(i):
    my_accounts = accounts.from_mnemonic(config["wallets"]["from_mnemonic"], 10)
    return my_accounts[i]

def get_host():
    host = interface.ISuperfluid(config["networks"][network.show_active()]["Host"])
    return host

def get_supertoken_factory():
    supertoken_factory = interface.ISuperApp(config["networks"][network.show_active()]["SuperTokenFactory"])
    return supertoken_factory

def get_resolver():
    resolver = interface.IResolver(config["networks"][network.show_active()]["Resolver"])
    return resolver

def get_CFAv1():
    CFAv1 = interface.IConstantFlowAgreementV1(config["networks"][network.show_active()]["CFAv1"])
    return CFAv1

def get_IDAv1():
    IDAv1 = interface.IInstantDistributionAgreementV1(config["networks"][network.show_active()]["IDAv1"])
    return IDAv1

def gets_balance(token_name, account):
    token = get_token(token_name)
    balance = token.balanceOf(account)
    return balance

def get_super_token(token_name):
    token = interface.ISuperToken(config["networks"][network.show_active()][token_name])
    return token