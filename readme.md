# Getting Started

First rename the `.env.example` file in this directory to `.env`. Replace the API keys as needed.

After adding your api keys, run the following command from your terminal.

```bash
source .env
```

This command allows brownie config to access your environment variables.

## Scripts to AAVE Token balances

Run the following command to get token balances for all aave tokens in your account.

```bash
brownie run scripts/aave/aave_balances.py
```

Output:

```python
Brownie v1.19.1 - Python development framework for Ethereum

RushProject is the active project.

Running 'scripts/aave/aave_balances.py::main'...
                                                                                
     Tokens in Account   
====================================================================================================
index    Token Name    balance                    address                                       
0        AAVE          100000000000000000000      0x63242B9Bd3C22f18706d5c4E627B4735973f1f07    
1        DAI           10000000000000000000000    0xDF1742fE5b0bFc12331D8EAec6b478DfDbD31464    
2        LINK          1000000000000000000000     0x07C725d58437504CA5f814AE406e70E21C5e8e9e    
3        EURS          1000000                    0xaA63E0C86b531E2eDFE9F91F6436dF20C301963D    
4        USDC          10000000000                0xA2025B15a1757311bfD68cb14eaeFCc237AF5b43    
5        USDT          10000000000                0xC2C527C0CACF457746Bd31B2a698Fe89de2b6d49    
6        WETH          0                          0x2e3A2fb8473316A02b8A297B982498E661E1f6f5    
7        WBTC          200000000                  0x8869DFd060c682675c2A8aE5B21F2cF738A0E3CE    
                                                                                
     Interest aTokens in Account  
====================================================================================================
index    Token Name    balance      address                                       
0        aAAVE         0            0xC4bf7684e627ee069e9873B70dD0a8a1241bf72c    
1        aDAI          0            0x310839bE20Fc6a8A89f33A59C7D5fC651365068f    
2        aLINK         0            0x6A639d29454287B3cBB632Aa9f93bfB89E3fd18f    
3        aEURS         0            0xc31E63CB07209DFD2c7Edb3FB385331be2a17209    
4        aUSDC         0            0x1Ee669290939f8a8864497Af3BC83728715265FF    
5        aUSDT         0            0x73258E6fb96ecAc8a979826d503B45803a382d68    
6        aWETH         0            0x27B4692C93959048833f40702b22FE3578E77759    
7        aWBTC         200000000    0xc0ac343EA11A8D05AAC3c5186850A659dD40B81B    
                                                                                
     Stable Debt Tokens in Account  
====================================================================================================
index    Token Name        balance    address                                       
0        stableDebtAAVE    0          0x4a8aF512B73Fd896C8877cE0Ebed19b0a11B593C    
1        stableDebtDAI     0          0xbaBd1C3912713d598CA2E6DE3303fC59b19d0B0F    
2        stableDebtLINK    0          0x4f094AB301C8787F0d06753CA3238bfA9CFB9c91    
3        stableDebtEURS    0          0x512ad2D2fb3Bef82ca0A15d4dE6544246e2D32c7    
4        stableDebtUSDC    0          0xF04958AeA8b7F24Db19772f84d7c2aC801D9Cf8b    
5        stableDebtUSDT    0          0x7720C270Fa5d8234f0DFfd2523C64FdeB333Fa50    
6        stableDebtWBTC    0          0x15FF4188463c69FD18Ea39F68A0C9B730E23dE81    
7        stableDebtWETH    0          0xCAF956bD3B3113Db89C0584Ef3B562153faB87D5    
                                                                                
     Variable Debt Tokens in Account  
====================================================================================================
index    Token Name          balance               address                                       
0        variableDebtAAVE    0                     0xad958444c255a71C659f7c30e18AFafdE910EB5a    
1        variableDebtDAI     0                     0xEa5A7CB3BDF6b2A8541bd50aFF270453F1505A72    
2        variableDebtLINK    0                     0x593D1bB0b6052FB6c3423C42FA62275b3D95a943    
3        variableDebtEURS    0                     0x257b4a23b3026E04790c39fD3Edd7101E5F31192    
4        variableDebtUSDC    0                     0x3e491EB1A98cD42F9BBa388076Fd7a74B3470CA0    
5        variableDebtUSDT    0                     0x45c3965f6FAbf2fB04e3FE019853813B2B7cC3A3    
6        variableDebtWBTC    0                     0x480B8b39d1465b8049fbf03b8E0a072Ab7C9A422    
7        variableDebtWETH    206270138356159747    0x2b848bA14583fA79519Ee71E7038D0d1061cd0F1    

```

If you set up your .env you should see this from your terminal.

## Deploying Flashloan Contracts

Keep in mind that all the scripts you will be running for this demo are found in [/scripts/aave](./scripts/aave/) directory. Read through them to see what they are doing.

The following script will deploy two flashloan contracts. One will be used to flashloan one token at a time [SimpleFlashLoan](./contracts/rush/flashloan/RushSimpleFlashLoan.sol), the other will be used to combine multiple tokens in one flashloan transaction [FlashLoan](./contracts/rush/flashloan/RushFlashLoan.sol).

```bash
brownie run scripts/aave/deploy_flashloan.py
```

Ouput:

```python
Brownie v1.19.1 - Python development framework for Ethereum

RushProject is the active project.

Running 'scripts/aave/deploy_flashloan.py::main'...
Deploying Simple Rush flashloan receiver contract ...
===============================================
Transaction sent: 0x0a39f260819c1e3a9d71010ccc64ba9bddc4f2d677d0d94b67c5fac9939cb520
  Gas price: 36.756769064 gwei   Gas limit: 541641   Nonce: 90
  FlashLoan.constructor confirmed   Block: 8282174   Gas used: 492401 (90.91%)
  FlashLoan deployed at: 0xD86bF68ADaf5C6389F1e7379700B01217f3f8129

View contract on Optimism Goerli: https://goerli.etherscan.io/address/0xD86bF68ADaf5C6389F1e7379700B01217f3f8129
Transaction was Mined 
---------------------
Tx Hash: 0x0a39f260819c1e3a9d71010ccc64ba9bddc4f2d677d0d94b67c5fac9939cb520
From: 0xFE948CB2122FDD87bAf43dCe8aFa254B1242c199
New FlashLoan address: 0xD86bF68ADaf5C6389F1e7379700B01217f3f8129
Block: 8282174
Gas Used: 492401 / 541641 (90.9%)
                            
```

## Excecuting flashloan transaction

After you deploy your contracts, you are ready to submit transactions. The flashloan contracts will receive and repay your loan. Here's an example:

Run command on terminal.

```bash
brownie run scripts/aave/simple_flashloan.py
```

Output:

```python
Brownie v1.19.1 - Python development framework for Ethereum

RushProject is the active project.

Running 'scripts/aave/simple_flashloan.py::main'...
Transaction sent: 0xe0298379f63293c6bb8ec2bfbd147684c3c73087e5ede19eb7409bcd844fcabb
  Gas price: 33.986319221 gwei   Gas limit: 37951   Nonce: 93
  MintableERC20.transfer confirmed   Block: 8282256   Gas used: 34501 (90.91%)

Transaction sent: 0x58180124eadc669c23c0cfa28053e0c79496b48713f0f160734710ace2b92577
  Gas price: 32.188179381 gwei   Gas limit: 209116   Nonce: 94
  Transaction confirmed   Block: 8282267   Gas used: 165364 (79.08%)

Congrats! You have flipped a flashloan. Check it out! https://goerli.etherscan.io/tx/0x58180124eadc669c23c0cfa28053e0c79496b48713f0f160734710ace2b92577
```

## Publish and Verify Contract on Etherscan

Brownie has a simple way to quickly instantly verify your contract on etherscan. Run the following command.

```python
>>> contract = RushFlashLoan.at("0x9db7BcB878E9b3eFDf8FAfcfbbF11a54d80f089c")
>>> contract
<RushFlashLoan Contract '0x9db7BcB878E9b3eFDf8FAfcfbbF11a54d80f089c'>
>>> RushFlashLoan.publish_source(contract)
Verification submitted successfully. Waiting for result...
Verification complete. Result: Pass - Verified
True
```

## Trasaction breakdown

Here the flashloan contract is requesting 1M from the pool provider.

```python
from brownie import accounts, config, network, interface, RushSimpleFlashLoan
from scripts.aave.helper_functions import get_address_provider, get_token, get_account


tx_url = "https://goerli.etherscan.io/tx/{}"
pool = interface.IPool(get_address_provider().getPool())
flashloan_receiver = RushSimpleFlashLoan[len(RushSimpleFlashLoan) -1]
usdc = get_token("USDC")
usdc_amount = 1_000_000 * 10** usdc.decimals()


def run_flashloan():
    dev = get_account()
    receiver = flashloan_receiver.address
    assets = usdc.address
    amount = usdc_amount
    # 'flashLoanSimple': "0x42b0b77c"
    params = "0x42b0b77c"
    referral = 0
    tx = pool.flashLoanSimple(receiver, assets, amount, params, referral, {"from": dev})
```

## Multi Token Flashloans

If you run this command, you can flashloan over 100M+ in tokens.

```bash
brownie run scripts/aave/multi_flashloan.py 
```

```python
Brownie v1.19.1 - Python development framework for Ethereum

RushProject is the active project.

Running 'scripts/aave/multi_flashloan.py::main'...
Transaction sent: 0x310974980351e66748421d1ef01b3d940202090525a99630e03150cb9aeae859
  Gas price: 4.924637698 gwei   Gas limit: 1578971   Nonce: 83
  Transaction confirmed   Block: 8265853   Gas used: 1113994 (70.55%)

  Transaction confirmed   Block: 8265853   Gas used: 1113994 (70.55%)

Congrats! You have flipped a flashloan. Check it out! https://goerli.etherscan.io/tx/0x310974980351e66748421d1ef01b3d940202090525a99630e03150cb9aeae859

```

Go to [/scripts/aave/multi_flashloan.py](./scripts/aave/multi_flashloan.py) and adjust token amounts. Try it out or yourself.

## Support me

If you want to support me, you can. I accept ETH. Currently struggling to find a job.

ETH: msaki.eth 0x04655832bcb0a9a0be8c5ab71e4d311464c97af5

BTC: bc1qafvljh25wxd7ser9vsawzm95aaju883r9twd0p

DOGE: D5y6zYKN4WsWCr4YmnKhAFqCCFC31AN3We

| :warning: WARNING   |
|:--------------------|
| I should warn you. You will not make any profits from using flashloans in the current state on this repo.
