# Get price from Chainlink Data Feed
from brownie import interface, config

symbol = "ETH-USD"

def main():
  token = config["networks"]["mainnet"][symbol]

  aggregator = interface.AggregatorV3Interface(token)

  decimals = aggregator.decimals()
  price = aggregator.latestRoundData()[1] / 10 ** decimals

  print(f"The price of ETH is {price} USD")

if __name__ == "__main__":
  main()