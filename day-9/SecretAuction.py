import os
def clear():
  os.system('clear')

from art import logo
print(logo)

bid_dictionary = {}
bidding_ongoing = True

while bidding_ongoing == True:
  person_name = input("What is your name?\n")
  person_bid = int(input("What is your bid price?\n$"))        
  bid_dictionary[person_name] = person_bid
  answer = input("Are there any other bidders? Type 'yes or 'no'\n")
  if answer == "no":
    clear()
    bidding_ongoing = False
    max_key = next(iter(bid_dictionary))
    for key in bid_dictionary:
      if bid_dictionary[key] > bid_dictionary[max_key]:
        max_key = key
    print(f"The highest bidder is {max_key} with a bid of ${bid_dictionary[max_key]}")
  else:
    clear()
  