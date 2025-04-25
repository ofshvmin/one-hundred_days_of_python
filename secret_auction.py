import art

print(art.auction_logo)
print("Welcome to the silent auction")

bids = {}
more_bidders = True

while more_bidders:

    name = input("What is your name?\n")
    bid_amount = int(input(f"How much would you like to bid, {name}?\n$"))
    print(f"your name is {name} and you bid {bid_amount}")

    def add_bid(bidder, amount):
        bids[bidder] = amount
    add_bid(bidder=name, amount=bid_amount)
    more = input("Are there any more bidders?\n").lower()

    if more == 'no':
        more_bidders = False
    else:
        print("\n" * 100)

def evaluate_winner():
    highest_bid = 0
    winner = ""
    for key in bids:
        if bids[key] > highest_bid:
            highest_bid = bids[key]
            winner = key
    print("\n" * 5)
    print(f"{winner} is the winner with a bid of {highest_bid}!")
    print("\n" * 5)

evaluate_winner()