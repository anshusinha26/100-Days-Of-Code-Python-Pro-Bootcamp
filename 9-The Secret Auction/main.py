# Day 9 Project: The secret auction program

"""this statement imports the auction module"""
import auction

"""this satement imports the os module"""
import os

"""this print statement prints the logo by calling the auction module and accessing the logo attribute"""
print(auction.logo)

"""an empty dictionary is initialised"""
auctionMembers = {}

"""this function statement performs operations like asking for your name, asking for your bid and storing both of them as key value pairs in auction dictionary respectively"""
def auction():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: ₹"))
    auctionMembers[name] = bid

"""function call statement"""
auction()

"""this variable is initialilsed to a false value which means the auction as not ended"""
endOfAuction = False

"""until the endOfAction is false, the auction will run"""
while (endOfAuction == False):
    moreBidders = input("Are there any other bidders? Type 'y' for 'yes' or 'n' for 'no': ").lower()
    if (moreBidders == 'n'):
        endOfAuction = True
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        auction()

"""winner and winningBid variable is initialsied with empty values"""
winner = ''
winningBid = 0

"""this loops checks for the bidder with maximum bid"""
for member in auctionMembers:
    if auctionMembers[member] > winningBid:
        winningBid = auctionMembers[member]
        winner = member

"""if bid amount is less than or equal to zero, than no one is declared as the winner, else the bidder with maximum bid wins the auction"""
if (winningBid <= 0):
    print("No one won the bid!")
else:
    print(f"The winner is {winner} with a bid of ₹{winningBid}")

    
