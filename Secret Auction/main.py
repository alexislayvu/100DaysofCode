import art
import os

print(art.logo)
print("Welcome to the Secret Auction.")

auction_dictionary = {}
max_bidder = ""
max_bid_amount = 0

play_again = True
while play_again:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    auction_dictionary[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if other_bidders == 'yes':
        os.system('cls')
    if other_bidders == 'no':
        for key in auction_dictionary:
            if auction_dictionary[key] > max_bid_amount:
                max_bid_amount = auction_dictionary[key]
                max_bidder = key

        max_bid_text = str(max_bid_amount)
        print("The winner is " + max_bidder + " with a bid of $" + max_bid_text)
        play_again = False
