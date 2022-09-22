from brownie import interface
from scripts.helper_functions import get_lending_pool, get_accounts, get_account, get_stable_token, get_variable_token, get_atoken


def pretty_table(rows, column_count, column_spacing=4):
    aligned_columns = []
    for column in range(column_count):
        column_data = list(map(lambda row: row[column], rows))
        aligned_columns.append((max(map(len, column_data)) + column_spacing, column_data))

    for row in range(len(rows)):
        aligned_row = map(lambda x: (x[0], x[1][row]), aligned_columns)
        yield ''.join(map(lambda x: x[1] + ' ' * (x[0] - len(x[1])), aligned_row))

def get_erc20_tokens():
    print(f"=================================================")
    print(f"     Tokens in Account                           ")
    print(f"=================================================")
    acct = get_accounts(0)
    pool = get_lending_pool()
    rows = [['index', 'Token Name', 'balance']]
    tokens = ["AAVE", "DAI", "LINK", "SUSD", "USDC", "USDT", "WETH", "WBTC"]

    for n in range (0, len(tokens)):
        token_name = tokens[n]
        balance = get_atoken(tokens[n]).balanceOf(acct)
        rows.append((str(n), str(token_name), str(balance)))
    for line in pretty_table(rows, 3):
        print(line)

def get_atokens():
    print(f"=================================================")
    print(f"     Interest aTokens in Account                 ")
    print(f"=================================================")
    acct = get_accounts(0)
    pool = get_lending_pool()
    rows = [['index', 'Token Name', 'balance']]
    atokens = ["aAAVE", "aDAI", "aLINK", "aSUSD", "aUSDC", "aUSDT", "aWETH", "aWBTC"]
    
    for n in range (0, len(atokens)):
        token_name = atokens[n]
        balance = get_atoken(atokens[n]).balanceOf(acct)
        rows.append((str(n), str(token_name), str(balance)))
    for line in pretty_table(rows, 3):
        print(line)

def get_stable_tokens():
    print(f"=================================================")
    print(f"     Stable Debt Tokens in Account               ")
    print(f"=================================================")
    acct = get_accounts(0)
    pool = get_lending_pool()
    rows = [['index', 'Token Name', 'balance']]
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
        balance = get_stable_token(stable_tokens[n]).principalBalanceOf(acct)
        rows.append((str(n), str(token_name), str(balance)))
    for line in pretty_table(rows, 3):
        print(line)

def get_variable_tokens():
    print(f"=================================================")
    print(f"     Variable Debt Tokens in Account             ")
    print(f"=================================================")
    acct = get_accounts(0)
    pool = get_lending_pool()
    rows = [['index', 'Token Name', 'balance']]
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
        balance = get_variable_token(variable_tokens[n]).scaledBalanceOf(acct)
        rows.append((str(n), str(token_name), str(balance)))
    for line in pretty_table(rows, 3):
        print(line)

def main ():
    get_erc20_tokens()
    get_atokens()
    get_stable_tokens()
    get_variable_tokens()
