from brownie import interface
from scripts.aave.helper_functions import get_account
from brownie import PairFlash
from brownie.network import priority_fee
from brownie.network.gas.strategies import GasNowStrategy
from brownie.network import gas_price

priority_fee("2 gwei")
gas_strategy = GasNowStrategy("fast")
gas_price(gas_strategy)

dev = get_account()
router = interface.IV3SwapRouter("0xE592427A0AEce92De3Edee1F18E0157C05861564")
factory = interface.IUniswapV3Factory("0x1F98431c8aD98523631AE4a59f267346ea31F984")
weth = interface.IWETH9("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
dai = interface.IERC20("0x6B175474E89094C44Da98b954EedeAC495271d0F")
usdc = interface.IERC20("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")
wbtc = interface.IERC20("0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599")

contract = PairFlash.deploy(router, factory, weth, {'from': dev})
amount_dai = 6000 * 10**18


# USDC / ETH 0.05% $1.55k https://info.uniswap.org/#/pools/0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640
# USDC / ETH 0.3% 1 ETH = 1.55k USDC https://info.uniswap.org/#/pools/0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8
# USDC / ETH 0.01% $1546.21 https://info.uniswap.org/#/pools/0xe0554a476a092703abdb3ef35c80e0d76d32939f


# DAI / FRAX 0.05% || 1 DAI = 1.0003 FRAX || 1 FRAX = 0.9997 DAI

# Fails because of trade is not profitable, error: "Too little received"
contract.initFlash([wbtc.address, weth.address, 3000, 1*10**8, 13.4647*10**18, 500, 10000], {'from': dev})
# WBTC / ETH 0.3% || 1 WBTC = 13.4591 ETH || 1 ETH = 0.0743 WBTC
# WBTC / ETH 0.05% || 1 WBTC = 13.4647 ETH || 1 ETH = 0.0743 WBTC
# WBTC / ETH 1% || 1 WBTC = 13.5539 ETH 

# WBTC / USDC 1% || 1 WBTC = 20.78k USDC
# WBTC / USDC 0.3% || 1 WBTC = 20810.62 USDC 
# WBTC / USDC 0.05% || 1 WBTC = 20.83k USDC

# WBTC / BADGER 0.3% || 1 WBTC = 7.83k BADGER 
# WBTC / FUN 0.01% || 1 WBTC = 2.95m FUN
# WBTC / XSGD 0.3% || 1 WBTC = 27.42k XSGD
# ICHI / WBTC 0.01% ||  1 WBTC = 4.59k ICHI
# WBTC / renBTC 0.05% || 1 WBTC = 0.9503 renBTC


