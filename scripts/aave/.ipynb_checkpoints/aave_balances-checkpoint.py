from brownie import interface
from scripts.aave.helper_functions import get_lending_pool, get_accounts, get_account, get_stable_token, get_variable_token, get_atoken, get_token


def pretty_table(rows, column_count, column_spacing=4):
    aligned_columns = []
    for column in range(column_count):
        column_data = list(map(lambda row: row[column], rows))
        aligned_columns.append((max(map(len, column_data)) + column_spacing, column_data))

    for row in range(len(rows)):
        aligned_row = map(lambda x: (x[0], x[1][row]), aligned_columns)
        yield ''.join(map(lambda x: x[1] + ' ' * (x[0] - len(x[1])), aligned_row))

def get_erc20_tokens():
    print(f"{'    ' * 20}")
    print(f"     Tokens in Account   ")
    print(f"{'=====' * 20}")
    dev = get_accounts(0)
    pool = get_lending_pool()
    rows = [['index', 'Token Name', 'balance', 'address']]
    tokens = ["AAVE", "DAI", "LINK", "SUSD", "USDC", "USDT", "WETH", "WBTC"]

    for n in range (0, len(tokens)):
        token_name = tokens[n]
        balance = get_token(tokens[n]).balanceOf(dev)
        address = get_token(tokens[n]).address
        rows.append((str(n), str(token_name), str(balance), str(address)))
    for line in pretty_table(rows, 4):
        print(line)

def get_atokens():
    print(f"{'    ' * 20}")
    print(f"     Interest aTokens in Account  ")
    print(f"{'=====' * 20}")
    dev = get_accounts(0)
    pool = get_lending_pool()
    rows = [['index', 'Token Name', 'balance', 'address']]
    atokens = ["aAAVE", "aDAI", "aLINK", "aSUSD", "aUSDC", "aUSDT", "aWETH", "aWBTC"]
    
    for n in range (0, len(atokens)):
        token_name = atokens[n]
        balance = get_atoken(atokens[n]).balanceOf(dev)
        address = get_atoken(atokens[n]).address
        rows.append((str(n), str(token_name), str(balance), str(address)))
    for line in pretty_table(rows, 4):
        print(line)

def get_stable_tokens():
    print(f"{'    ' * 20}")
    print(f"     Stable Debt Tokens in Account  ")
    print(f"{'=====' * 20}")
    dev = get_accounts(0)
    pool = get_lending_pool()
    rows = [['index', 'Token Name', 'balance', 'address']]
    stable_tokens = [
        "stableDebtAAVE", 
        "stableDebtDAI", 
        "stableDebtLINK",
        "stableDebtSUSD", 
        "stableDebtUSDC", 
        "stableDebtUSDT", 
        "stableDebtWBTC", 
        "stableDebtWETH"
        ]
    
    for n in range (0, len(stable_tokens)):
        token_name = stable_tokens[n]
        balance = get_stable_token(stable_tokens[n]).principalBalanceOf(dev)
        address = get_stable_token(stable_tokens[n]).address
        rows.append((str(n), str(token_name), str(balance), str(address)))
    for line in pretty_table(rows, 4):
        print(line)

def get_variable_tokens():
    print(f"{'    ' * 20}")
    print(f"     Variable Debt Tokens in Account  ")
    print(f"{'=====' * 20}")
    dev = get_accounts(0)
    pool = get_lending_pool()
    rows = [['index', 'Token Name', 'balance', 'address']]
    variable_tokens = [
        "variableDebtAAVE", 
        "variableDebtDAI", 
        "variableDebtLINK",
        "variableDebtSUSD", 
        "variableDebtUSDC", 
        "variableDebtUSDT", 
        "variableDebtWBTC", 
        "variableDebtWETH"
        ]
    
    for n in range (0, len(variable_tokens)):
        token_name = variable_tokens[n]
        balance = get_variable_token(variable_tokens[n]).scaledBalanceOf(dev)
        address = get_variable_token(variable_tokens[n]).address
        rows.append((str(n), str(token_name), str(balance), str(address)))
    for line in pretty_table(rows, 4):
        print(line)

def main ():
    get_erc20_tokens()
    get_atokens()
    get_stable_tokens()
    get_variable_tokens()
