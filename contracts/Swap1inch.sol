// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

import "../interfaces/IERC20.sol";

contract Swap1inch{
	
	address v4router_1inch;
	constructor(address v4router) {
		v4router_1inch = v4router;
	}
	
	function swap(uint256 amountIn, address fromTkn,bytes calldata in_data) external {
		require(amountIn > 0, "Invalid swap");
		IERC20(fromTkn).transferFrom(msg.sender, address(this), amountIn);
                IERC20(fromTkn).approve(v4router_1inch, amountIn);

		(bool succ, bytes memory rt) = address(v4router_1inch).call(in_data);
                if(!succ){
			revert();
		}
	}
}
