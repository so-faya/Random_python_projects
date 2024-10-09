import Day9_art

print(Day9_artart.logo)
print("Welcome to the Blind Auction Program")


name = input("Enter bidder's name:")
bid_amount = int(input("Enter your bid:"))

bidding_dictionary = {
    name : bid_amount,
}
bidding_continue = True
while bidding_continue:
    # ask user whether there are still any bidder left
    question = input("Are there any bidders left? if yes type 'Y' else no type 'N':").lower()
    if question == "y":
        print("\n" * 100)
        name = input("Enter bidder's name:")
        bid_amount = int(input("Enter your bid:"))
        bidding_dictionary[name] = bid_amount
    else:
        bidding_continue = False
        max_num = 0
        for key,value in bidding_dictionary.items():
            if value > max_num:
                max_num = value
                max_bidder = key
        print(f"{max_bidder} is the highest bidder with the amount {max_num} ")


