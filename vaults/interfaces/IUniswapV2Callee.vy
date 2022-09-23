# @version ^0.3.3

# IUniswapV2Callee  
# @author deltartificial (@deltartificial)

interface IUniswapV2Callee:

    def uniswapV2Call(
        _sender: address,
        _amount0: uint256,
        _amount1: uint256,
        _data: bytes32
    ): nonpayable