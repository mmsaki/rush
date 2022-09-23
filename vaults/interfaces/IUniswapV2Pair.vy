# @version ^0.3.3

# IUniswapV2Pair
# @author deltartificial (@deltartificial)

interface IUniswapV2Pair:

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

    def MINIMUM_LIQUIDITY() -> uint256: pure
    def factory() -> address: view
    def token0() -> address: view
    def token1() -> address: view
    def getReserves() -> (uint112, uint112, uint32): view
    def price0CumulativeLast() -> uint256: view
    def price1CumulativeLast() -> uint256: view
    def kLast() -> uint256: view

    def mint(_to: address) -> uint256: nonpayable
    def burn(_to: address) -> (uint256, uint256): nonpayable
    def swap(
        _amount0Out: uint256, 
        _amount1Out: uint256, 
        _to: address, 
        _data: bytes32): nonpayable
    def skim(_to: address): nonpayable
    def sync(): nonpayable

    def initialize(_token0: address, _token1: address): nonpayable