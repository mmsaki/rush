from brownie import config, interface, network, accounts


def get_account():
    account = accounts.add(config["wallets"]["from_key"])
    return account


def get_accounts(i):
    my_accounts = accounts.from_mnemonic(config["wallets"]["from_mnemonic"], 10)
    return my_accounts[i]


def get_weth(token_name):
    token = interface.IWETH(config["networks"][network.show_active()][token_name])
    return token


def get_token(token_name):
    token = interface.IERC20(
        config["networks"][network.show_active()][token_name]
    )
    return token


def get_address_provider():
    address_provider = interface.IPoolAddressesProvider(
        config["networks"][network.show_active()]["PoolAddressesProvider"]
    )
    return address_provider


def get_lending_pool():
    address_provider = get_address_provider()
    lending_pool = interface.IPool(address_provider.getPool())
    return lending_pool


def check_balance(token_name, account):
    token = get_token(token_name)
    balance = token.balanceOf(account)
    return balance


def get_borrowed_amount(account):
    lending_pool = get_lending_pool()
    amount = lending_pool.getUserAccountData(account)[1]
    return amount


def get_variable_token(token_name):
    # variableDebtAAVE, variableDebtDAI, variableDebtLINK, variableDebtSUSD etc...
    token = interface.IVariableDebtToken(
        config["networks"][network.show_active()][token_name]
    )
    return token


def get_stable_token(token_name):
    # stableDebtAAVE, stableDebtDAI, stableDebtLINK, stableDebtSUSD etc...
    token = interface.IStableDebtToken(
        config["networks"][network.show_active()][token_name]
    )
    return token


def get_atoken(token_name):
    token = interface.IAToken(config["networks"][network.show_active()][token_name])
    return token
