import os
from secret_auction_program_art import logo

print(logo)

bids = {}
end_bidding = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_price = bidding_record[bidder]
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bidder
            if bid_price == highest_bid:
                os.system("clear")
                print(logo)
                print("Some bids are the same, please re-bid.")
            else:
                print(f"The winner is {winner} with a bid of ${highest_bid}!")

while not end_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price

    bidders = input("Are any other bidders? Enter 'yes' or 'no'. ").lower()
    if bidders == "no":
        end_bidding = True
        highest_bidder(bids)

    else:
        os.system("clear")
        print(logo)
