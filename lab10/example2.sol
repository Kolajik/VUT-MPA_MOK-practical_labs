// SPDX-License-Identifier: MIT
pragma solidity 0.8.3;

contract Example2 {
    uint256 public capital;
    uint256 internal lastRun;

    constructor() {
        capital = 100000;
    }

    function addCapital(uint256 x) public {
        require(x <= 10000, "Transaction cannot be higher than 10000 CZK.");
        capital = capital + x;
    }

    function withdrawCapital(uint256 y) public {
        uint256 maxWithdraw = (20 * capital) / 100;
        require(y <= maxWithdraw, "You cannot withdraw more than 20% of capital.");
        require(block.timestamp - lastRun > 1 minutes, "You have to wait 1 minute until next withdrawal.");

        capital = capital - y;
        lastRun = block.timestamp;
    }
}