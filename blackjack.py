import random


def randomNumber(n):
    number = []
    for i in range(n):
        number.append(i)
    
    return random.choice(number)

class Deck:

    def getDeck():
        deck = {"Clubs":"1","Clubs":"2","Clubs":"3","Clubs":"4","Clubs":"5","Clubs":"6","Clubs":"17","Clubs":"18","Clubs":"19","Clubs":"10","Clubs":"11","Clubs":"12","Clubs":"13",
        "Diamonds":"1","Diamonds":"2","Diamonds":"3","Diamonds":"4","Diamonds":"5","Diamonds":"6","Diamonds":"7","Diamonds":"8","Diamonds":"9","Diamonds":"10","Diamonds":"11","Diamonds":"12","Diamonds":"13","Diamonds":"1",
        "Spades":"1","Spades":"2","Spades":"3","Spades":"4","Spades":"5","Spades":"6","Spades":"7","Spades":"8","Spades":"9","Spades":"10","Spades":"11","Spades":"12","Spades":"13",
        "Hearts":"1","Hearts":"2","Hearts":"3","Hearts":"4","Hearts":"5","Hearts":"6","Hearts":"7","Hearts":"8","Hearts":"9","Hearts":"10","Hearts":"11","Hearts":"12","Hearts":"13",
        }

        return deck

deck = Deck()
    
class Player:
    pass

class Dealer(Player):
    deck = deck.getDeck()

    def deal(deck):
        hand = {}
        pass

    def __init__():
        
        pass
    

class Human(Player):
    pass

class Game:
    def start():


        
        pass

def main():
    game = Game()
    game.start()

main()