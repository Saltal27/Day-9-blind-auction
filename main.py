from replit import clear

from art import logo

print(logo)
print("Welcome to the secret auction program!")
bids = {}

end_of_auction = False

while end_of_auction == False:

    bidder_name = input("What is your name?\n")
    bid_amount = int(input("What is your bid?\n$"))
    bids[bidder_name] = bid_amount

    heighest_bid = 0
    winner = ""
    winners_number = 0
    for bidder in bids:
        if bids[bidder] > heighest_bid:
            heighest_bid = bids[bidder]
            winner = bidder
            winners_number = 1
        elif bids[bidder] == heighest_bid:
            winners_number += 1
            heighest_bid = bids[bidder]
            winner += f", {bidder}"

    other_bidders = input("Are there any other bidders?\n").lower()

    if other_bidders == "yes":
        clear()

    elif other_bidders == "no":
        from art import congrats
        end_of_auction = True
        clear()
        if winners_number == 1:
            print(
                f"The winner is {winner} with a bid of {heighest_bid}$\nCongrats!"
            )
        else:
            print(
                f"The winners are {winner} with a bid of {heighest_bid}$\nCongrats!"
            )
        print(congrats)

    else:
        end_of_auction = True
        print("Invalid info!")
