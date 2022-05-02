from math import *
from random import *
from time import time
from fractions import Fraction as frac


def unique_helper(hand):

    #count the unique values
    unique_list = [[x,0] for x in range(1,6+1)]

    for die in hand:
        for val in unique_list:
                if die == val[0]:
                    val[1] = val[1] + 1

    unique_list.sort(key = lambda x:x[1], reverse=True)

    return unique_list

class player:
    def __init__(self,name):
        self.roll = []
        self.name = str(name)

    def take_turn(self):
        x = [randint(1,6) for x in range(1,6)]
        x.sort(reverse=True)
        self.roll = x
        print(self.name + " rolled a ", x,"!")

    def get_hand(self):
        return self.roll

    def print_hand(self):
        print(self.roll)
 

class check:
    def __init__(self):
        self.yahtzee_count = 0
        self.bonus_points = 0

    
    def __c_(self,hand):
        unique_list = unique_helper(hand)
        unique_list.sort(key = lambda x:x[0])
        print("Upper Scoreboard!")
        print("Upper total (need 63): ",self.bonus_points)

        for thing in unique_list:
            print("Score for ", thing[0], "'s: ", thing[1])

        print("\n\n\n")


    def __c_yahtzee(self,hand):
        x = set(hand)
        if len(hand) == 1:
            print("Yahtzee!")
    

    def __c_three_of_a_kind(self,hand):
        #return values that are more than three
        unique_list = unique_helper(hand)
        ret = []
        for thing in unique_list:
            if thing[1] >= 3:
                ret.append((thing[0],thing[1]))
        if len(ret) == 0:
            return None
        else:
            return ret


    def __c_four_of_a_kind(self,hand):
        #return values that are more than three
        unique_list = unique_helper(hand)
        ret = []
        for thing in unique_list:
            if thing[1] >= 4:
                ret.append((thing[0],thing[1]))

        if len(ret) == 0:
            return None
        else:
            return ret


    def __c_full_house(self,hand):
        #checks if there is a count of 3 and a count of 2
        unique_list = unique_helper(hand)
        three_count = False
        two_count = False

        for thing in unique_list:
            if thing[1] == 3:
                three_count = True
                continue
            if thing[1] == 2:
                two_count = True
                continue

        if three_count and two_count:
            return True


    def __c_large_straight(self,hand):
        #checks for a large straight
        hand.sort(reverse=True)

        #if the difference between the two numbers arent 1, its not sequential
        for i in range(0,(len(hand) - 1) ):
            if (hand[i] - hand[i+1]) != 1:
                return False

        return True



    def __c_small_straight(self,hand):
        #checks for a small straight
        hand = list(set(hand) )
        hand.sort(reverse=True)
        seq_count = 0 
        #if the difference between the two numbers arent 1, its not sequential
        for i in range(0,(len(hand) - 1) ):
            diff = hand[i] - hand[i+1]
            if diff == 1:
                seq_count+=1
            else:
                seq_count = 0


        if seq_count >= 3:
            return True
        else:
            return False



    def __c_chance(self,hand):
        t = 0
        for thing in hand:
            t=t+thing

        return sum(hand)

    def __check_hand(self,hand):
        print("Your Hand!:",hand)
            
        self.__c_(hand)
        print("Yahtzee? ", self.__c_yahtzee(hand))
        print("Three of a kind?", self.__c_three_of_a_kind(hand))
        print("Four of a kind?", self.__c_four_of_a_kind(hand))
        print("Full House?", self.__c_full_house(hand))
        print("Small Straight? ", self.__c_small_straight(hand))
        print("Large Straight?", self.__c_large_straight(hand))
        print("The sum of the dice for chance is: ",self.__c_chance(hand))

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

