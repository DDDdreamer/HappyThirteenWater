from unittest import TestCase
from compare_cards import *

class TestIsleagle(TestCase):
    def test_isleagle(self):
        print(isleagle(
            {'shangdun': ['#7', '#9', '#10'], 'zhongdun': ['#4', '$5', '$J', '&Q', '&K'],
             'xiadun': ['*2', '*3', '*8', '*10', '*J'], 'type': ['散牌', '散牌', '同花']}
))
        print(isleagle(
            {'shangdun': ['#4', '$5', '#7'], 'zhongdun': ['#9', '#10', '$J', '&Q', '&K'],
             'xiadun': ['*2', '*3', '*8', '*10', '*J'],'type':[]}
))

        print(Compare(
            {'shangdun': ['#7', '#9', '#10'], 'zhongdun': ['#4', '$5', '$J', '&Q', '&K'],
             'xiadun': ['*2', '*3', '*8', '*10', '*J'], 'type': ['散牌', '散牌', '同花']},
            {'shangdun': ['#4', '$5', '#7'], 'zhongdun': ['#9', '#10', '$J', '&Q', '&K'],
             'xiadun': ['*2', '*3', '*8', '*10', '*J'],'type':['散牌', '顺子', '同花']}))