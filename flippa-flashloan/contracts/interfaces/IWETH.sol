// SPDX-License-Identifier: AGPL-3.0
pragma solidity ^0.8.0;

interface IWETH {
  function balanceOf(address) external view returns (uint256);
  function totalSupply() external view returns (uint256);
  function deposit() external payable;
  function withdraw(uint256) external;
  function approve(address spender, uint256 amount) external returns (bool);
  function allowance(address owner, address spender) external view returns (uint256);
  function name() external view returns (string memory);
  function symbol() external view returns (string memory);
  function decimals() external view returns (uint8);
  function transferFrom(address from, address to, uint256 amount) external returns (bool);
}
