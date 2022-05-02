from math import *
from random import *
from time import time
from fractions import Fraction as frac


class multi_dice_role:
    def __init__(self,num):
        self.hand = []
        if num <= 0:
            raise Exception( "error, non-zero")
            
        
        self.n = num
        for x in range(0,num):
            self.hand.append(randint(1,6))

        self.hand.sort(reverse=True)

    def get_hand(self):
        return self.hand

    def print_hand(self):
        print(self.hand)


    


if __name__ == "__main__":


    for i in range(0,5+1):
        print("Attempting call of mult_dice_role(" + str(i) + ")")
        try:
            a = multi_dice_role(i)
            print("Getting Hand")
            b = a.get_hand()
            print("The hand is: ",b)
            print("printing hand")
            a.print_hand()
            print("Print hand again (should be the same)")
            a.print_hand()
            print("Success with i=" + str(i))

        except:
            print("Ate shit with i=" + str(i) )

        print("\n\n\n")
