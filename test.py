from math import *
from random import *
from time import time
from fractions import Fraction as frac


class one_dice_role:
    def __init__(self):
        self.val = randint(1,6)

    def print_val(self):
        print(self.val)

    def get_val(self):
        return self.val

class mult_dice_role:
    def __init(self,num):
        if num >= 0:
            return "error, non-zero"

        for x in range(0,num-1):
            print(x)



if __name__ == "__main__":
    mult_dice_role(0)
    mult_dice_role(1)
    mult_dice_role(2)
    mult_dice_role(5)


class turn

def divide(num,den):
    num = int(num)
    den = int(den)
    print((frac(num,den)),(num/den))

print("Testing the division")
divide(3,6)
divide(1,6)

print(time())

#seed(time())

print(randint(1,6))

#three of a kind

def three_of_a_kind():
    oneRoll = (1/6)
    print(oneRoll)
    num_0 = 1 * 1 * 1 * 6 * 6 
    num_1 = 1 * 1 * 1 * 1 * 6
    num_2 = 1 * 1 * 1 * 1 * 1
    denominator = pow(6,5)

    fin_num = num_0 + num_1 + num_2
    print("fin_num: ",fin_num)
    print("denominator: ", denominator)
    print("Chance of a three of a kind in one roll of 5 dice")
    divide(fin_num,denominator)


three_of_a_kind()


'''
x = pow(6,5)
y = pow(6,5)

divide(x,y)
'''









