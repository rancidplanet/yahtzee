class return_prob(object):
    def __init__(self):
        self.vals = [1,2,3,4,5,6]


    def _prob_full_house(self,hand):
        print("checking full house prob")
        #needs 2 of one kind and three of one kind
        # will score 25 points regardless

        counts = {  "1": 0,
                    "2": 0,
                    "3": 0,
                    "4": 0,
                    "5": 0,
                    "6": 0}

        for thing in hand:
            counts[str(thing)]+=1


        #see if close
        condition_pair_count = 0
        condition_triple = False
        for count in counts.values():
            if count == 2: condition_pair_count+=1
            if count == 3: condition_triple = True

        if condition_pair_count == 1 and condition_triple: return 1


        if condition_pair_count == 1 and not condition_triple:
            return (1/6) * (1/6) * (1/6)

        elif condition_pair_count == 2:
            #always a higher chance to re-roll 1 and match instead of roll a pair
            return (1/6) 


        print(counts)
        return counts

    def check(self,hand):
        print("Checking the probabilities")

        return self._prob_full_house(hand)


if __name__=="__main__":
    c= return_prob()

    #Check for full house
    hand = [1,1,2,2,2]
    print(c.check(hand))


    hand = [1,1,2,3,4]
    print(c.check(hand))

    hand = [1,1,1,3,4]
    print(c.check(hand))


    hand = [1,1,2,2,3]
    print(c.check(hand))


