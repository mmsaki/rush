
# Rush ⤽ ⤼ Flashloan Rush
![Rush](./images/rush_flashloans/rush_flashloans.002.jpeg)

## Category for ETHOnline 2022

### **Decentralized Finance (Defi)** 

I created this forex tool to help onboard DeFi users to using flashloans on lending protocols like Aave, all while keeping their debt at zero. With this tool, anyone can learn how to use flashloans, even if they don't have a technical background.

## GitHub Repository
[**Rush Flashloans**](https://github.com/mmsaki/rush)

## Description

Aave v3 Core lending pool allows you to borrow assets using flashloan contracts. If your goal is to stay debt-free, you can borrow crypto assets as needed as long as you can prove that you have enough collateral. You need to understand the risks of financial burdens from borrowing assets and getting liquidated, especially when market movements are volatile and against you. In order to avoid maximum losses, the only strategy you have left is using flashloans.

With this project, my goal is to provide you with a forex tool to help you maximize your borrowing power and debt positions. If you have provided collateral on Aave before, this might be of great use to you. All DeFi users, with or without technical backgrounds, can learn how to use flashloans without any complications. We want to ensure our forex tool provides secure interactions with Aave's lending pools using flashloan receiver smart contracts. You only have to pay a flashloan premium fee, currently at 0.09%.



| :warning: WARNING          |
|:---------------------------|
| I should warn you. You will not make any profits from using flashloans as they are on this repo.      |


## Getting Started

The set up is easy. Rush is an open source project the tool is accessible to everyone. I am in the build process of to make clean up the projects code base. I hope to make flashloans easy for to everyone to understand. See the demo transactions in the next segment. Work in progress...

Check back later. 👷

## Transactions Reference

See examples below of flashloan transations and how they are submitted. From these results aave fees for $1,000,000 flashloan is $500.

- [1 million USDC flashloan - Etherscan](https://goerli-optimism.etherscan.io/tx/0xe7b6883bc925eef37d318efa3353a24a74ef7b04fd9e2ba2a8bdfa1116d8f1a2)
- [100 + million Tokens flashloan - Etherscan](https://goerli-optimism.etherscan.io/tx/0xb096db8fbf39c390f343603d9dc51bd7ed41f51a47124cb6b1bdb3007f7f7a76)

## Aave Flash loan fee

The flash loan fee is initialized at deployment to `0.09%` which is updated via aave Governance Vote.

- Flashloan fee can be shared by the LPs (liquidity providers) and the protocol treasury.

- The `premium_total` represents the total fee paid by the borrowers of which:

  - Fee to LP = `premium_total` - `flashloan_premium_to_protocol`

  - Fee to Protocol = `flashloan_premium_to_protocol`

## Setting Up

- Ensure we have enough funds when flashloaning
- Calculate the profitability of liquidating loans vs gas costs
- Fail safe security by using a testnet like Goerli before moving to mainnet
- You can find Aave contracts annd registries [Testnet Aave Contract Addresses](https://docs.aave.com/developers/deployed-contracts/v3-testnet-addresses)

## ▨Roadmap

- [x] Create Project
    - [Loan Rush](https://ethglobal.com/showcase/rush-8s2mf)
- [ ] Checkin #1
   - Update: We Missed checkin #1
- [x] Create Logo
    - [Rush logo](./images/carousel.png)
- [x] Create Discord
    - [Discord](https://discord.gg/57TA3bHx62)
- [x] Submit Checkin #2 
    - How is the project coming along?
- [x] Create scripts
    - deploy_flashloan.py
    - aave_balances.py
    - run_flashloan.py
    - simple_flashloan.py
    - supply_token.py
    - withdraw_token.py
- [x] Project feedback Session Thu, Sep 15 02:00 PM
- [x] Create Presentation Sun, Sep 18 11:00 AM
- [ ] Bonus
    - Front end landing page
    - Users can connect metamask
    - User can call deposit WETH function
    - User can send flashloan
- [x] Project Check-in #3 Tue, Sep 20 11:00 AM
    - Is everything going as expected?
    - What are some things you need help with?
    - What do you need to complete your project?
- [x] Project feedback Session Wed, Sep 21 02:00 PM
    - Present project for feedback
- [x] ETHOnline Summit Fri, Sep 23 11:00 AM
    - If ready submit project
    - Record Video demonstration on how to use rush
- [x] Submissions Due! Sun, Sep 25 02:00 PM
    - Submit project by 2:00pm
- [x] Project Judging Mon, Sep 26 11:00 AM
    - Present to judges and sponsors
 

## ▧Sponsors
- Aaave

![Optimism Goerli](./images/rush_flashloans/rush_flashloans.012.jpeg)
