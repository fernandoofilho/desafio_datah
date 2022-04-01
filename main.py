class Card():

    def __init__(self, p):
        number = p[0]
        suit = p[1]

        self.number = number
        self.suit = suit

    def get_card(self):
        return self.number + self.suit


class PokerHand():

    def __init__(self, string):

        self.hand = []

        for k in string.split(" "):

            self.hand.append(Card(k))

    def bubble_cards(self, cards=[]):
        if cards == []:
            cards = self.get_hand(False)

        numbers = [i[0] for i in cards]

        ord = {"A": 13, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11,
               "K": 12}

        for number in range(len(numbers)):
            for k in range(number, len(numbers)):
                if ord[numbers[number]] > ord[numbers[k]]:
                    aux = numbers[number]
                    numbers[number] = numbers[k]
                    numbers[k] = aux
        return numbers

    def get_high_card(self):

        c = self.bubble_cards()

        return c[4]

    def get_hand(self, pt= True):
        if pt:
            for k in self.hand:

                print(k.get_card())

        cards = [i.get_card() for i in self.hand]

        return cards

    def is_same_suit(self, cards= []):

        if cards == []:

            cards = self.get_hand(False)

        s = cards[0][1]

        for card in cards:

            if card[1] != s:

                return False

        return True

    def is_high_cards(self, cards= []):

        if cards == []:

            cards = self.get_hand(False)

        high_cards = ['A', 'K', 'Q', 'J', '10']

        for card in cards:

            if card[0] not in high_cards:

                return False

        return True


    def is_a_sequence(self, cards = []):

        ord = {"A": 13, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11,
               "K": 12}

        if cards == []:
            numbers = self.bubble_cards()

        else:
            numbers = self.bubble_cards(cards)



        for n in range(len(numbers) - 1):

            if ord[numbers[n+1]] -1 != ord[numbers[n]]:
                return False

        return True


    def how_many_same_numbers(self, cards = []):

        if cards == []:

            cards = self.get_hand(False)

        numbers= {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, 'T':0,'J':0, 'Q':0, 'K':0, 'A':0}

        for card in cards:

            numbers[card[0]]+=1

        return numbers

    def how_many_same_suits(self, cards= []):

        if cards == []:

            cards = self.get_hand(False)

        numbers= {'S':0, 'H':0, 'D':0, 'C':0}

        for card in cards:

            numbers[card[0]] += 1

        return numbers

    def is_royalStraingFlush(self):

        if not (self.is_same_suit()):

            return False

        if not(self.is_high_cards()):

            return False

        return True

    def is_straing_flush(self):
        if not self.is_a_sequence():
            return False

        if not self.is_same_suit():
            return False

        return True

    def is_four_of_a_kind(self):
        if self.is_same_suit():
            return False
        c = self.how_many_same_numbers()

        for card in c.keys():

            if c[card] == 4:

                return True
    def is_full_house(self):
        if self.is_same_suit():
            return False
        c = self.how_many_same_numbers()
        a1 = a2 = False
        for card in c.keys():

            if c[card] == 2:

                a1= True

            if c[card] == 3:
                a2 = True

        return a1 and a2

    def is_flush(self):
        if self.is_same_suit() and not(self.is_royalStraingFlush()) and not self.is_straing_flush():
            return True
        return False

    def straight(self):
        if self.is_a_sequence() and not self.is_straing_flush():
            return True

    def is_three_of_a_kind(self):

        if self.is_same_suit():
            return False

        if self.is_full_house():

            return False

        c = self.how_many_same_numbers()

        for card in c.keys():
            if c[card] == 3:
                return True

        return False

    def is_two_pair(self):
        n = self.how_many_same_numbers()
        a1, a2 = False, False
        for card in n.keys():
            if n[card] == 2:
                typ = card
                a1 = True
        for card in n.keys():
            if n[card] == 2 and card != typ:
                a2= True
        return a1 and a2

    def is_one_pair(self):

        if self.is_two_pair() or self.is_full_house():

            return False

        n = self.how_many_same_numbers()

        for card in n.keys():
            if n[card] == 2:

                return True

        return False

    def is_straight(self):

        if not self.is_a_sequence():
            return False
        if self.is_flush():
            return False
        return True

    def points(self):
        p = {10: self.is_royalStraingFlush(), 9:self.is_straight(), 8: self.is_straing_flush(),
             7:self.is_three_of_a_kind(), 6:self.is_four_of_a_kind(), 5:self.is_two_pair(),
             4:self.is_full_house(), 3:self.is_one_pair(), 2:self.is_flush()}
        for point in p.keys():
            if(p[point]):
                return point

        return 0
    def compare_with(self, ph2):

        ph1_points = self.points()
        ph2_points = ph2.points()

        if ph1_points > ph2_points:
            return 'W'
        else:
            return 'F'

class Result():

    def __init__(self):
        Result.WIN = 'W'
        Result.LOSS = 'L'

    def assertTrue(self, result):
        if result == 'W':
            return 'W'
        else:
            return 'L'


    def test(self):
        cases = [
        self.assertTrue(PokerHand("TC TH 5C 5H KH").compare_with(PokerHand("9C 9H 5D 5S AC")) == Result.WIN),

        self.assertTrue(PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JD AS KC TH")) == Result.LOSS),


        self.assertTrue(PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7S JH TH 6D")) == Result.WIN),


        self.assertTrue(PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7H 5H 5C JS")) == Result.LOSS),


        self.assertTrue(PokerHand("AS AC KH 7D 3D").compare_with(PokerHand("AD AH KD 7C 4S")) == Result.LOSS),


        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("9C 9H 9S 9D KH")) == Result.WIN),


        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JD QC KC AC")) == Result.WIN),


        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QC QD AD 8H")) == Result.WIN),


        self.assertTrue(PokerHand("AC AH AS AD KS").compare_with(PokerHand("9C TC JS QC KS")) == Result.WIN),


        self.assertTrue(PokerHand("AC AH AS AD KS").compare_with(PokerHand("QH QS QC KD 8H")) == Result.WIN),


        self.assertTrue(PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QD AS 8H")) == Result.WIN),


        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("KH KC KS KD TD")) == Result.WIN),


        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4C 5C 9C TC JC")) == Result.WIN),


        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9S TC JC")) == Result.WIN),


        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("TS TC TD JC JD")) == Result.WIN),


        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JC JD TD TC 4C")) == Result.WIN),


        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("4H 5H 9H QH KH")) == Result.WIN),


        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("5C 6S 7H 8H 9H")) == Result.WIN),


        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("TS TC TD KH KD")) == Result.WIN),


        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("QH QD TD TC 4C")) == Result.WIN),


        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("7C 8S 9D TD JC")) == Result.WIN),


        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("TS TC TD JC JD")) == Result.LOSS),


        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("JH JD TS TC 4C")) == Result.WIN),


        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("TS TC TD JC JD")) == Result.LOSS),


        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("JC JD TS TC 4C")) == Result.WIN),


        self.assertTrue(PokerHand("TS TH TD JH JD").compare_with(PokerHand("JS JC KC KC 4C")) == Result.WIN)
        ]
        for case in cases:
            if case == False:
                print(f"Casso {case} errado")
        print("Todos os casos estão certos")


Result().test()

