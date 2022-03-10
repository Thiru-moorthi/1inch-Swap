from brownie import *

def main():
    u_acc = accounts.at(config['networks']['mainnet-fork']['u_acc'],force=True)
    swap = Swap1inch.deploy(config['networks']['mainnet-fork']['router'],{'from':u_acc})
    run('swap')

