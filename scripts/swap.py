from brownie import *
import requests

def main():
    tokenIn = config['networks']['mainnet-fork']['tokenIn']
    tokenOut = config['networks']['mainnet-fork']['tokenOut']

    amount = config['networks']['mainnet-fork']['amount']

    u_acc = accounts.at(config['networks']['mainnet-fork']['u_acc'], force=True)
    swap_contract = Swap1inch[0]

    slippage = config['networks']['mainnet-fork']['slippage']

    api_1inch = f'https://api.1inch.io/v4.0/1/swap?fromTokenAddress={tokenIn}&toTokenAddress={tokenOut}&amount={amount}&fromAddress={u_acc}&slippage={slippage}&destReceiver={u_acc}'
    res = requests.get(api_1inch)
    print(res.json())
    data = res.json()['tx']['data']

    interface.IERC20(tokenIn).approve(swap_contract, amount, {'from':u_acc})

    print("out token balance before swap:",interface.IERC20(tokenOut).balanceOf(u_acc,{'from':u_acc}))

    tx = swap_contract.swap(amount,tokenIn,data,{'from':u_acc})
    print(tx.info())

    print("out token balance after swap:",interface.IERC20(tokenOut).balanceOf(u_acc,{'from':u_acc}))
