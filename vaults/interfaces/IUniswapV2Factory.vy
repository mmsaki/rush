# @version ^0.3.3

# IUniswapV2Factory
# @author deltartificial (@deltartificial)

interface IUniswapV2Factory:

    def feeTo() -> address: view
    def feeToSetter() -> address: view

    def getPair(
        _tokenA: address,
        _tokenB: address
    ) -> address: view

    def allPairs(_x: uint256) -> address: view 
    def allPairsLength() -> uint256: view

    def createPair(
        _tokenA: address,
        _tokenB: address
    ) -> address: nonpayable

    def setFeeTo(_to: address) : nonpayable
    def setFeeToSetter(_to: address) : nonpayable
    


