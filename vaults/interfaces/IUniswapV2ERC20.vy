# @version ^0.3.3

# IUniswapV2ERC20 
# @author deltartificial (@deltartificial)

interface IUniswapV2ERC20:

    def name() -> String[10]: pure
    def symbol() -> String[10]: pure
    def decimals() -> uint8: pure
    def totalSupply() -> uint256: view
    def balanceOf(_owner: address) -> uint256: view
    def allowance(_owner: address, _spender: address) -> uint256: view

    def approve(_spender: address, _value: uint256) -> bool: nonpayable
    def transfer(_to: address, _value: uint256) -> bool: nonpayable
    def transferFrom(_from: address, _to: address, _value: uint256) -> bool: nonpayable

    def DOMAIN_SEPARATOR() -> bytes32: view
    def PERMIT_TYPEHASH() -> bytes32: pure
    def nonces(_owner: address) -> uint256: view

    def permit(
        _owner: address,
        _spender: address,
        _value: uint256,
        _deadline: uint256,
        _v: uint8,
        _r: bytes32,
        _s: bytes32
    ): nonpayable
