from rolls import *



class player:
    def __init__(self,name):
        self.rolls = []
        self.name = str(name)

    def take_turn(self):
        x = multi_dice_role(5)
        self.rolls.append(x)

        print(self.name + " rolled a ", x.get_hand(),"!")

    def get_hand(self):
        return self.

 

class check:
    def __init__(self):
        pass


    def __c_three_of_a_kind(hand):

    def __check_hand(self,hand):
        print("Your Hand!:",hand)
            


    def check_hand(self,hand):
        self.__check_hand(hand)

  
class game:
    def __init__(self):
        self.checker = check()

 
    def check_hand(self, hand):
        self.checker.check_hand(hand)



if __name__ == "__main__":

    g = game()
    p_1 = player("Kevin")
    p_1.take_turn()


    g.check_hand(p_1.get_hand())
