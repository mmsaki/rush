# @version ^0.3.3

# IWETH
# @author deltartificial (@deltartificial)

interface IWETH:

    def deposit(): payable
    def transfer(
        _to: address, 
        _value: uint256
    ) -> bool: nonpayable
    def withdraw(_value: uint256): nonpayable