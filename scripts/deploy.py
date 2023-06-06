from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_Mock, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()
    # pass price feed address to our fund me contract

    # if we are on a persistent network like sepolia, use the associated address
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else : 
        # deploy a mock : our own version of price feed contract
        deploy_Mock()
        price_feed_address = MockV3Aggregator[-1].address
        print("Mocks Deployed!")
        

    fund_me = FundMe.deploy(price_feed_address, {"from": account}) #, publish_source=True
    print(f"Contract deployed to {fund_me.address} by {account.address}")
    return fund_me

def main():
    deploy_fund_me()