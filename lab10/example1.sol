// SPDX-License-Identifier: MIT
pragma solidity 0.8.10;

contract Example1 {
    string private greet = "Hello World!";
    string public name;

    function store(string memory n) public {
        name = n;
    }

    function retrieve() public view returns(string memory) {
        return name;
    }

    function greetings() public view returns(string memory) {
        if (0 == bytes(name).length) {
            return "Name is not provided.";
        }
        else {
            return string(abi.encodePacked("Hello, ", name));
        }
    }
}