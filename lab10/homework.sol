// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Homework
 * @dev Create own token MOK
 */
contract MOKToken {
    mapping (address => uint256) private _balances;
    mapping (address => mapping (address => uint256)) private _allowances;
    string private _name;
    string private _symbol;
    uint8 private _decimals;
    uint256 private _totalSupply = 150000;

    constructor(string memory name_, string memory symbol_, uint8 decimals_) {
        _name = name_;
        _symbol = symbol_;
        _decimals = decimals_;

        _balances[msg.sender] = _totalSupply;
    }

    event Approval(address indexed tokenOwner, address indexed spender, uint tokens);
    event Transfer(address indexed _from, address indexed _to, uint256 _value);

    function name() public view returns (string memory) {
        return _name;
    }

    function symbol() public view returns (string memory) {
        return _symbol;
    }

    function decimals() public view returns (uint8) {
        return _decimals;
    }

    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address _owner) public view returns (uint256) {
        return _balances[_owner];
    }

    function transfer(address _to, uint256 _value) public returns (bool) {
        require(balanceOf(msg.sender) >= _value, "Not enough tokens in your wallet to send them to someone else.");
        require(msg.sender != _to, "You cannot send tokens to yourself.");
        
        _balances[msg.sender] = _balances[msg.sender] - _value;
        _balances[_to] = _balances[_to] + _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function approve(address _delegate, uint256 _numOfTokens) public returns (bool) {
        require(balanceOf(msg.sender) >= _numOfTokens, "You cannot delegate more tokens than you own.");
        _allowances[msg.sender][_delegate] = _numOfTokens;

        emit Approval(msg.sender, _delegate, _numOfTokens);
        return true;
    }

    function allowance(address _owner, address _spender) public view returns (uint256) {
        return _allowances[_owner][_spender];
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_value <= _balances[_from], "The owner does not have this much tokens.");
        require(_value <= _allowances[_from][msg.sender], "You are not allowed to spend this much tokens.");

        _balances[_from] = _balances[_from] - _value;
        _allowances[_from][msg.sender] = _allowances[_from][msg.sender] - _value;
        _balances[_to] = _balances[_to] + _value;

        emit Transfer(_from, _to, _value);
        return true;
    }
}
