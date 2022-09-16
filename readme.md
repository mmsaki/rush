
# Defi Loan Flippa
![Flippa Logo](./logo.jpg)

## What Category does your project belong to?
- **Defi**

## Emoji
- **🧑‍🌾 🌾**

## GitHub Repository
- [**Loan Flipper**](https://github.com/mmsaki/eth-online-2022)

## Short Description
- **Loan Flippa** is a service that interacts with **Aave  v3 Lending pools** to supply and borrow assets using its **flashloan contracts**.

## Long Description

- Defi users should rely on simple tools to trade their assets. Sometimes trading assests can cause major shifts in prices. Defi users who **borrow assets** are sometimes forced to **liquiditate automatically** to pay off their debt. This can lead to **max losses**. Flippa Flashloans provides an easy way to  liquidate positions from outstanding **debts on aave**. We also want common Defi users without any technical backgrounds to use flashloans when they need to. We want to offer **stability** with **volatile assest swapping**, and debt payoff with a **better rates** without incurring maximum losses.

## How It's Made
*Tell us about how you built this project; the nitty-gritty details. What technologies did you use? How are they pieced together? If you used sponsor technology how did it benefit your project? Did you do anything particuarly hacky that's notable and worth mentioning? How did you impress yourself which what your team built?*

- How to use our Flippa Flashloan Contracts on this project
    - You need to use **Optimism Goerli Testnet**
    - Get weth by swapping ETH for **WETH** 
    - Deposit WETH into aave to receive **aWETH tokens**
    - Deploy `FlashloanAttacker` contract
    - `SupplyAssest` to WETH **pool address**
    - `Approve` **spender**
    - `executeOperation` on receiver contract

![](./flippa-loans.gif)

- Earning Flash loan fee
    - The flash loan fee is **initialized at deployment** to `0.09%` and can be updated via Governance Vote. Use `FLASHLOAN_PREMIUM_TOTA`L to get current value.
    - Flashloan fee can be shared by the LPs (liquidity providers) and the **protocol treasury**. The `FLASHLOAN_PREMIUM_TOTAL` represents the total fee paid by the borrowers of which:
        - Fee to LP: `FLASHLOAN_PREMIUM_TOTAL - FLASHLOAN_PREMIUM_TO_PROTOCOL`
        - Fee to Protocol: `FLASHLOAN_PREMIUM_TO_PROTOCOL`

- Setting Up
    - Ensure we have enough funds when liquidating
    - Calculate the profitability of liquidating loans vs gas costs
    - Ensure we have access toe the latest protocol user data
    - Fail safe security 
- Aave contracts and registry on Optimism 
    - [V3 Testnet Aave Address on Optimism Görli](https://docs.aave.com/developers/deployed-contracts/v3-testnet-addresses)


## Project Roadmap

- [x] Create Project 
    - [Loan Flippa](https://ethglobal.com/showcase/loan-flippa-8s2mf)
- [ ] Checkin #1
    - Update: We Missed checkin #1
- [x] Create Logo
    - [flippa logo](./logo.jpg)
- [x] Create Discord
    - [Discord](https://discord.gg/57TA3bHx62)
- [x] Submit Checkin #2 
    - Update: Done
- [ ] Create test scripts
- [ ] Project feedback Session Thu, Sep 15 02:00 PM
- [ ] Create Presentation Sun, Sep 18 11:00 AM
- [ ] Create Live Demo URL Mon Sep 19 11:00 AM
- [ ] Project Check-in #3 Tue, Sep 20 11:00 AM
- [ ] Project feedback Session Wed, Sep 21 02:00 PM
- [ ] ETHOnline Summit Fri, Sep 23 11:00 AM
- [ ] Submissions Due! Sun, Sep 25 02:00 PM
- [ ] Project Judging Mon, Sep 26 11:00 AM
 