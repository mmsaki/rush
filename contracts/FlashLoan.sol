// SPDX-License-Identifier: MIT

pragma solidity 0.8.10;

import {IERC20} from "@aave/contracts/dependencies/openzeppelin/contracts/IERC20.sol";
import {FlashLoanSimpleReceiverBase} from "@aave/contracts/flashloan/base/FlashLoanSimpleReceiverBase.sol";
import {IPoolAddressesProvider} from "@aave/contracts/interfaces/IPoolAddressesProvider.sol";
import {SafeMath} from "@aave/contracts/dependencies/openzeppelin/contracts/SafeMath.sol";
import {IUniswapV3Factory} from "@uniswap/contracts/interfaces/IUniswapV3Factory.sol";


contract FlashLoan is FlashLoanSimpleReceiverBase {
    address payable public owner;

    constructor(address provider) FlashLoanSimpleReceiverBase(IPoolAddressesProvider(provider)) {
        owner = payable(msg.sender);
    }

    function executeOperation(
        address asset,
        uint256 amount,
        uint256 premium,
        address initiator,
        bytes memory params
    ) public override returns (bool) {
        // Do something with the loaned amount
        // ...
        uint256 amountOwed = amount + premium;
        IERC20(asset).approve(address(POOL), amountOwed);

        return true;
    }

    function requestFlashLoan(address _token, uint256 _amount) public {
        address receiverAddress = address(this);
        address asset = _token;
        uint256 amount = _amount;
        bytes memory params = "";
        uint16 referralCode = 0;

        POOL.flashLoanSimple(receiverAddress, asset, amount, params, referralCode);
    }

    function getBalance(address _tokenAddress) external view returns (uint256) {
        return IERC20(_tokenAddress).balanceOf(address(this));
    }
    
    function withdraw(address _tokenAddress) external onlyOwner {
        IERC20(_tokenAddress).transfer(owner, IERC20(_tokenAddress).balanceOf(address(this)));
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    receive() external payable {}
}
