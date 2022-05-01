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
        ret = []
        for thing in self.rolls:
            ret.append(thing.get_hand())
        return ret

    
  


if __name__ == "__main__":
    p_1 = player("Kevin")
    p_1.take_turn()

