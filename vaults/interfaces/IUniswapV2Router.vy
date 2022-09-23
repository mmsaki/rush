# @version ^0.3.3

# IUniswapV2Router (01 & 02)
# @author deltartificial (@deltartificial)

# IUniswapV2Router01 :
interface IUniswapV2Router01:
    def factory() -> address: view
    def WETH() -> address: view

    def addLiquidity(
        _tokenA: address,
        _tokenB: address,
        _amountADesired: uint256,
        _amountBDesired: uint256,
        _amountAMin: uint256,
        _amountBMin: uint256,
        _to: address,
        _deadline: uint256
    ) -> (uint256, uint256, uint256): nonpayable

    def addLiquidityETH(
        _token: address,
        _amountTokenDesired: uint256,
        _amountTokenMin: uint256,
        _amountETHMin: uint256,
        _to: address,
        _deadline: uint256
    ) -> (uint256, uint256, uint256): payable

    def removeLiquidity(
        _tokenA: address,
        _tokenB: address,
        _liquidity: uint256,
        _amountAMin: uint256,
        _amountBMin: uint256,
        _to: address,
        _deadline: uint256
    ) -> (uint256, uint256): nonpayable

    def removeLiquidityETH(
        _token: address,
        _liquidity: uint256,
        _amountTokenMin: uint256,
        _amountETHMin: uint256,
        _to: address,
        _deadline: uint256
    ) -> (uint256, uint256): payable

    def removeLiquidityWithPermit(
        _tokenA: address,
        _tokenB: address,
        _liquidity: uint256,
        _amountAMin: uint256,
        _amountBMin: uint256,
        _to: address,
        _deadline: uint256,
        _approveMax: bool,
        _v: uint8,
        _r: bytes32,
        _s: bytes32
    ) -> (uint256, uint256): nonpayable

    def removeLiquidityETHWithPermit(
        _token: address,
        _liquidity: uint256,
        _amountTokenMin: uint256,
        _amountETHMin: uint256,
        _to: address,
        _deadline: uint256,
        _approveMax: bool,
        _v: uint8,
        _r: bytes32,
        _s: bytes32
    ) -> (uint256, uint256): nonpayable

    def swapExactTokensForTokens(
        _amountIn: uint256,
        _amountOutMin: uint256,
        _path: address[3],
        _to: address,
        _deadline: uint256
    ) -> uint256[3]: nonpayable

    def swapTokensForExactTokens(
        _amountOut: uint256,
        _amountInMax: uint256,
        _path: address[3],
        _to: address,
        _deadline: uint256
    ) -> uint256[3]: nonpayable

    def swapExactETHForTokens(
        _amountOutMin: uint256,
        _path: address[3],
        _to: address,
        _deadline: uint256
    ) -> uint256[3]: payable

    def swapTokensForExactETH(
        _amountOut: uint256,
        _amountInMax: uint256,
        _path: address[3],
        _to: address,
        _deadline: uint256
    ) -> uint256[3]: nonpayable

    def swapExactTokensForETH(
        _amountIn: uint256,
        _amountOutMin: uint256,
        _path: address[3],
        _to: address,
        _deadline: uint256
    ) -> uint256[3]: nonpayable

    def swapETHForExactTokens(
        _amountOut: uint256,
        _path: address[3],
        _to: address,
        _deadline: uint256
    ) -> uint256[3]: payable

    def quote(
        _amountA: uint256,
        _reserveA: uint256,
        _reserveB: uint256
    ) -> uint256: pure

    def getAmountOut(
        _amountIn: uint256,
        _reserveIn: uint256,
        _reserveOut: uint256
    ) -> uint256: pure

    def getAmountIn(
        _amountOut: uint256,
        _reserveIn: uint256,
        _reserveOut: uint256
    ) -> uint256: pure
    
    def getAmountsOut(
        _amountIn: uint256,
        _path: address[2]
    ) -> uint256[2]: view

    def getAmountsIn(
        _amountOut: uint256,
        _path: address[2]
    ) -> uint256[2]: view

    # IUniswapV2Router02 :

    def removeLiquidityETHSupportingFeeOnTransferTokens(
        _token: address,
        _liquidity: uint256,
        _amountTokenMin: uint256,
        _amountETHMin: uint256,
        _to: address,
        _deadline: uint256
    ) -> uint256: nonpayable

    def removeLiquidityETHWithPermitSupportingFeeOnTransferTokens(
        _token: address,
        _liquidity: uint256,
        _amountTokenMin: uint256,
        _amountETHMin: uint256,
        _to: address,
        _deadline: uint256,
        _approveMax: bool,
        _v: uint8,
        _r: bytes32,
        _s: bytes32
    ) -> uint256: nonpayable

    def swapExactTokensForTokensSupportingFeeOnTransferTokens(
        _amountIn: uint256,
        _amountOutMin: uint256,
        _path: address[3],
        _to: address,
        _deadline: uint256
    ): nonpayable

    def swapExactETHForTokensSupportingFeeOnTransferTokens(
        _amountOutMin: uint256,
        _path: address[3],
        _to: address,
        _deadline: uint256
    ): payable

    def swapExactTokensForETHSupportingFeeOnTransferTokens(
        _amountIn: uint256,
        _amountOutMin: uint256,
        _path: address[3],
        _to: address,
        _deadline: uint256
    ): nonpayable



