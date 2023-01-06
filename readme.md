# Getting Started

First rename the `.env.example` file in this directory to `.env`. Replace the API keys as needed.

After adding your api keys run the following command on your terminal. this allows you environment variables to be accessed by brownie networks.

```bash
source .env
```

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
RushProject is the active project.

Running 'scripts/aave/deploy_flashloan.py::main'...
Deploying Rush flashloan receiver contract ...
===============================================
Transaction sent: 0x10ca1b6c6286d141dded7e21d17dc392a120778d5c7b23fd51f4431e2a289c98
  Gas price: 5.733639427 gwei   Gas limit: 626919   Nonce: 76
  RushFlashLoan.constructor confirmed   Block: 8265347   Gas used: 569927 (90.91%)
  RushFlashLoan deployed at: 0x9db7BcB878E9b3eFDf8FAfcfbbF11a54d80f089c

View contract on Optimism Goerli: https://goerli.etherscan.io/address/0x9db7BcB878E9b3eFDf8FAfcfbbF11a54d80f089c
Transaction was Mined 
---------------------
Tx Hash: 0x10ca1b6c6286d141dded7e21d17dc392a120778d5c7b23fd51f4431e2a289c98
From: 0xFE948CB2122FDD87bAf43dCe8aFa254B1242c199
New RushFlashLoan address: 0x9db7BcB878E9b3eFDf8FAfcfbbF11a54d80f089c
Block: 8265347
Gas Used: 569927 / 626919 (90.9%)

Deploying Simple Rush flashloan receiver contract ...
===============================================
Transaction sent: 0x32ab837f8413fa05c927df8d37a9129dc7bfe439cf84377b446f99e3691767f2
  Gas price: 5.720037097 gwei   Gas limit: 437684   Nonce: 77
  RushSimpleFlashLoan.constructor confirmed   Block: 8265348   Gas used: 397895 (90.91%)
  RushSimpleFlashLoan deployed at: 0xA2C4ab618Ad699372D067473D57cbb8371E61Cb4

View contract on Optimism Goerli: https://goerli.etherscan.io/address/0xA2C4ab618Ad699372D067473D57cbb8371E61Cb4
Transaction was Mined 
---------------------
Tx Hash: 0x32ab837f8413fa05c927df8d37a9129dc7bfe439cf84377b446f99e3691767f2
From: 0xFE948CB2122FDD87bAf43dCe8aFa254B1242c199
New RushSimpleFlashLoan address: 0xA2C4ab618Ad699372D067473D57cbb8371E61Cb4
Block: 8265348
Gas Used: 397895 / 437684 (90.9%)

       
     ___           ___   ____    ____  _______ 
    /   \         /   \  \   \  /   / |   ____|
   /  ^  \       /  ^  \  \   \/   /  |  |__   
  /  /_\  \     /  /_\  \  \      /   |   __|  
 /  _____  \   /  _____  \  \    /    |  |____ 
/__/     \__\ /__/     \__\  \__/     |_______|
                                               
                
                      )     
    )           )  ( /( (   
   (     (   ( /(  )\()))\  
   )\  ' )\  )(_))((_)\((_) 
 _((_)) ((_)((_)_ | |(_)(_) 
| '  \()(_-</ _` || / / | | 
|_|_|_| /__/\__,_||_\_\ |_| 
                            
```

## Sending flashloan transaction

After you deploy your contract, you area ready to sebmit flashloan transactions. Here's an example:

Run command on terminal.

```bash
brownie run scripts/aave/simple_flashloan.py
```

Output:

```python
Brownie v1.19.1 - Python development framework for Ethereum

RushProject is the active project.

Running 'scripts/aave/simple_flashloan.py::main'...
Transaction sent: 0x466a3dcefcefc8160da2b57cb72b850705e0c8b99fb2c58da0ac02e5770c368b
  Gas price: 8.81757279 gwei   Gas limit: 245586   Nonce: 82
  Transaction confirmed   Block: 8265573   Gas used: 177590 (72.31%)

Congrats! You have flipped a flashloan. Check it out! https://goerli.etherscan.io/tx/0x466a3dcefcefc8160da2b57cb72b850705e0c8b99fb2c58da0ac02e5770c368b
```

## Trasaction breakdown

Here is the code breakdown for the flashloan contract I just submitted.

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

| :warning: WARNING   |
|:--------------------|
| I should warn you. You will not make any profits from using flashloans in the current state on this repo.

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

## Gif Video

![Video showing deployment scripts](./images/flippa-loans.gif)