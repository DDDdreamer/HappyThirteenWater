from unittest import TestCase
from ThirteenWater import *
import numpy
class TestBest_cards_type(TestCase):
    def test_best_cards_type(self):
        card_dic = []
        for i in ['*','#','&','$']:
            for j in ['2','3','4','5','6','7','8','9','10','J','Q','K','A']:
                card_dic.append(i+j)
        num = 10
        while num :
            cards = ""
            s = copy(card_dic)
            for i in range(13):
                j = numpy.random.randint(0,len(s))
                if i != 12:
                    cards += s[j] + ' '

                else:
                    cards += s[j]
                s.pop(j)
            num -= 1
            # print(cards)
            # print(special_cards_type(cards))
            # print(best_cards_type(cards))
            print(best_cards_type('*4 #4 $4 &4 #2 $3 #5 *6 &6 #8 #9 *10 #A'))