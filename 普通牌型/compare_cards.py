#牌型大小：同花顺 > 炸弹 > 葫芦 > 同花 > 顺子 > 三条 > 两对 > 一对 > 散牌
from shunzi_judge import *
from copy import *
def quhuase(cards):#去花色
    new_cards = []
    for card in cards:
        card = card.strip('*')
        card = card.strip('#')
        card = card.strip('$')
        card = card.strip('&')
        new_cards.append(card)
    return new_cards

def isyidui(cards, l):          #是否为一对
    card_dic = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
    duizi = []
    danpai = []
    danpai_num = 0
    duizi_num = 0
    for card in cards:
        card = card.strip('*')
        card = card.strip('#')
        card = card.strip('$')
        card = card.strip('&')
        card_dic[card] += 1
        if card_dic[card] == 1:
            danpai.append(card)
            danpai_num += 1
        elif card_dic[card] == 2:
            danpai.pop(-1)
            danpai_num -= 1
            duizi_num += 1
            duizi.append(card)
        elif card_dic[card] > 2:
            return [False, duizi, danpai]
    if l == 3:
        if danpai_num == 1 and duizi_num == 1:
            return [True, duizi, danpai]
    elif l == 5:
        if danpai_num == 3 and duizi_num == 1:
            return [True, duizi, danpai]
    return [False, duizi, danpai]

def isliangdui(cards):
    card_dic = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
    duizi = []
    danpai = []
    danpai_num = 0
    duizi_num = 0
    for l in cards:
        l = l.strip('*')
        l = l.strip('#')
        l = l.strip('$')
        l = l.strip('&')
        card_dic[l] += 1
        if card_dic[l] == 1:
            danpai.append(l)
            danpai_num += 1
        elif card_dic[l] == 2:
            danpai.pop(-1)
            danpai_num -= 1
            if l in duizi:
                return [False, duizi, danpai]
            else:
                duizi_num += 1
                duizi.append(l)
        elif card_dic[l] > 2:
            return [False, duizi, danpai]
    if duizi_num == 2 and danpai_num == 1:
        return [True, duizi, danpai]
    return [False, duizi, danpai]

def issantiao(cards, l):       #是否为三条
    card_dic = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
    danpai = []
    santiao = []
    danpai_num = 0
    santiao_num = 0
    for card in cards:
        card = card.strip('*')
        card = card.strip('#')
        card = card.strip('$')
        card = card.strip('&')

        card_dic[card] += 1
        if card_dic[card] == 1:
            danpai.append(card)
            danpai_num += 1
        elif card_dic[card] == 3:
            danpai.pop(-1)
            danpai_num -= 1
            santiao.append(card)
            santiao_num += 1
        elif card_dic[card] > 3:
            return [False, santiao, danpai]

    if l == 3:
        if santiao_num == 1 and danpai_num == 0:
            return [True, santiao, danpai]
    elif l == 5:
        if santiao_num == 1 and danpai_num == 2:
            return [True, santiao, danpai]
    return [False, santiao, danpai]

def isshunzi(cards):            #判断是否为顺子
    pai = ""
    for card in cards:
        card = card.strip('*')
        card = card.strip('#')
        card = card.strip('$')
        card = card.strip('&')
        pai += card
    if ShunZi_Judge(pai,len(cards)) > 0:
        return True
    return False

def istonghua(cards):           #是否为同花
    huase = []
    for card in cards:
        if card[0] not in huase:
            if len(huase) == 0:
                huase.append(card[0])
            else:
                return False
    return True

def ishulu(cards):              #判断是否为葫芦
    card_dic = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
    duizi = []
    santiao = []
    duizi_num = 0
    santiao_num = 0
    for l in cards:
        l = l.strip('*')
        l = l.strip('#')
        l = l.strip('$')
        l = l.strip('&')
        card_dic[l] += 1
        if card_dic[l] == 2:
            duizi.append(l)
            duizi_num += 1
        elif card_dic[l] == 3:
            duizi.pop(-1)
            duizi_num -= 1
            santiao.append(l)
            santiao_num += 1
        elif card_dic[l] > 3:
            return [False, santiao, duizi]

    if santiao_num == 1 and duizi_num == 1:
        return [True, santiao, duizi]
    return [False, santiao, duizi]

def isboom(cards):              #判断是否为炸弹
    card_dic = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
    danpai = []
    boom = []
    danpai_num = 0
    boom_num = 0
    for l in cards:
        l = l.strip('*')
        l = l.strip('#')
        l = l.strip('$')
        l = l.strip('&')
        card_dic[l] += 1
        if card_dic[l] == 1:
            danpai.append(l)
            danpai_num += 1
        elif card_dic[l] == 4:
            danpai.pop(-1)
            danpai_num -= 1
            boom.append(l)
            boom_num += 1

    if boom_num == 1 and danpai_num == 1:
        return [True, boom, danpai]
    return [False, boom, danpai]

def istonghuashun(cards):       #判断是否为同花顺
    huase_dic = {'*':'','#':'','$':'','&':''}
    len_huase = {'*':0,'#':0,'$':0,'&':0}
    for card in cards:
        if card.find('*'):
            huase_dic['*'] += card.strip('*')
            len_huase['*'] += 1
        elif card.find('#'):
            huase_dic['#'] += card.strip('#')
            len_huase['#'] += 1
        elif card.find('$'):
            huase_dic['$'] += card.strip('$')
            len_huase['$'] += 1
        else:
            huase_dic['&'] += card.strip('&')
            len_huase['&'] += 1

    for key in huase_dic:
        if huase_dic[key] != '':
            if ShunZi_Judge(huase_dic[key],len_huase[key]):
                return True
    return False

def cards_type(cards):      #判断每墩牌型
    if len(cards) == 3:
        #判断是否为三条
        case1 = issantiao(cards, 3)
        if case1[0]:
            return ["三条", case1[1], case1[2]]

        # 判断是否为一对
        case2 = isyidui(cards, 3)
        if case2[0]:
            return ["一对", case2[1], case2[2]]
        #其余情况为散牌
        return ["散牌",cards]
    else:
        if istonghuashun(cards):
            return ["同花顺", cards]

        case1 = isboom(cards)
        if case1[0]:
            return ["炸弹", case1[1], case1[2]]

        case2 = ishulu(cards)
        if case2[0]:
            return ["葫芦", case2[1], case2[2]]

        if istonghua(cards):
            return ["同花",cards]

        if isshunzi(cards):
            return ["顺子",cards]

        case3 = issantiao(cards, 5)
        if case3[0]:
            return ["三条", case3[1], case3[2]]

        case4 = isliangdui(cards)
        if case4[0]:
            return ["两对", case4[1], case4[2]]

        case5 = isyidui(cards, 5)
        if case5[0]:
            return ["一对", case5[1], case5[2]]

        return ["散牌", cards]

def cards_cmp(cards1,cards2):  #牌型相同比较牌面大小
    card_dic = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'J':10,'Q':11,'K':12,'A':13}
    cards1 = quhuase(cards1)
    cards2 = quhuase(cards2)
    l = min(len(cards1),len(cards2))
    for i in range(l - 1, -1, -1):
        if card_dic[cards1[i]] > card_dic[cards2[i]]:
            return -1
        elif card_dic[cards1[i]] < card_dic[cards2[i]]:
            return 1
    if len(cards1) > len(cards2):#较小墩牌较大
        return -1
    elif len(cards1) < len(cards2):#较小墩牌较小
        return 1
    return 0    #牌型相等

def liangdui_cmp(zhongdun_type,xiadun_type):#考虑连对情形
    res = 0
    zhongdun_duizi = []         #中墩对子
    xiadun_duizi = []           #下墩对子
    for duizi in zhongdun_type[1]:
        zhongdun_duizi.append(duizi[1:])
    for duizi in xiadun_type[1]:
        xiadun_duizi.append(duizi[1:])

    if zhongdun_duizi in [['2','3'],['3','4'],['4','5'],['5','6'],['6','7'],['7','8'],['8','9'],['9','10'],['10','J'],['J','Q'],['Q','K'],['K','J']]:
        if xiadun_duizi in [['2','3'],['3','4'],['4','5'],['5','6'],['6','7'],['7','8'],['8','9'],['9','10'],['10','J'],['J','Q'],['Q','K'],['K','J']]:
            if zhongdun_duizi == xiadun_duizi:  #连对相同比散牌
                res = cards_cmp(zhongdun_type[2],xiadun_type[2])
            else:                               #连对不相同比连对
                res = cards_cmp(zhongdun_type[1],xiadun_type[1])
        else:
            res = -1

    elif xiadun_duizi in [['2','3'],['3','4'],['4','5'],['5','6'],['6','7'],['7','8'],['8','9'],['9','10'],['10','J'],['J','Q'],['Q','K'],['K','J']]:
            res = 1
    else:
        cards1 = zhongdun_type[2]
        for card in zhongdun_type[1]:
            cards1.append(card)
        cards2 = xiadun_type[2]
        for card in xiadun_type[1]:
            cards2.append(card)
        res = cards_cmp(cards1, cards2)
    return res

#判断牌型是否合法，合法返回True及各墩牌型，否则返回False
def isleagle(cards):
    cards_order = {'散牌':0, '一对':1, '两对':2, '三条':3, '顺子':4, '同花':5, '葫芦':6, '炸弹':7, '同花顺':8}
    shangdun_type = cards_type(cards['shangdun'])
    zhongdun_type = cards_type(cards['zhongdun'])
    xiadun_type = cards_type(cards['xiadun'])

    if cards_order[shangdun_type[0]] < cards_order[zhongdun_type[0]]:
        res = 0
        if cards_order[zhongdun_type[0]] < cards_order[xiadun_type[0]]:
            return [True,[shangdun_type[0], zhongdun_type[0], xiadun_type[0]]]
        elif cards_order[zhongdun_type[0]]> cards_order[xiadun_type[0]]:
            return [False, []]
        else:
            cards1 = []
            cards2 = []
            if zhongdun_type[0] == "同花顺" or zhongdun_type[0] == "同花" or zhongdun_type[0] == "顺子" or zhongdun_type[0] == "散牌":
                cards1 = cards['zhongdun']
                cards2 = cards['xiadun']
                res = cards_cmp(cards1,cards2)
            elif zhongdun_type[0] != '两对':
                cards1 = zhongdun_type[2]
                for card in zhongdun_type[1]:
                    cards1.append(card)
                cards2 = xiadun_type[2]
                for card in xiadun_type[1]:
                    cards2.append(card)
                res = cards_cmp(cards1, cards2)
            else:
                res = liangdui_cmp(zhongdun_type,xiadun_type)

            if res == -1 or res == 0:
                return [False,[]]
            else:
                return [True, [shangdun_type[0], zhongdun_type[0], xiadun_type[0]]]

    elif cards_order[shangdun_type[0]] == cards_order[zhongdun_type[0]]:
        cards1 = copy(shangdun_type[1])
        cards2 = copy(zhongdun_type[1])
        if cards_cmp(cards1,cards2) == 1:
            if cards_order[zhongdun_type[0]] < cards_order[xiadun_type[0]]:
                return [True, [shangdun_type[0], zhongdun_type[0], xiadun_type[0]]]
            elif cards_order[zhongdun_type[0]] > cards_order[xiadun_type[0]]:
                return [False,[]]
            else:
                if zhongdun_type[0] == "同花顺" or zhongdun_type[0] == "同花" or zhongdun_type[0] == "顺子" or zhongdun_type[0] == "散牌":
                    cards1 = cards['zhongdun']
                    cards2 = cards['xiadun']
                    res = cards_cmp(cards1, cards2)
                elif zhongdun_type[0] != '两对':
                    cards1 = zhongdun_type[2]
                    for card in zhongdun_type[1]:
                        cards1.append(card)
                    cards2 = xiadun_type[2]
                    for card in xiadun_type[1]:
                        cards2.append(card)
                    res = cards_cmp(cards1, cards2)
                else:
                    res = liangdui_cmp(zhongdun_type, xiadun_type)
                if res == -1 or res == 0:
                    return [False, []]
                else:
                    return [True, [shangdun_type[0], zhongdun_type[0], xiadun_type[0]]]
        else:
            return [False, []]
    return [False,[]]

def Compare(old, new):
    cards_order = {'散牌':0, '一对':1, '两对':2, '三条':3, '顺子':4, '同花':5, '葫芦':6, '炸弹':7, '同花顺':8}

    leagle_new = isleagle(new)#判断牌型是否合法
    if not leagle_new[0]:#牌型不合法
        return [False,[]]
    else:
        new['type'] = leagle_new[1]
        type_old = old['type']
        type_new = new['type']

        #计算牌型净利润
        profit = 0

        # 计算下墩盈利
        if cards_order[type_old[2]] < cards_order[type_new[2]]:
            if type_new[2] == '同花顺':
                profit += 5
            elif type_new[2] == "炸弹":
                profit += 4
            else:
                profit += 1
        elif cards_order[type_old[2]] > cards_order[type_new[2]]:
            if type_new[2] == '同花顺':
                profit -= 5
            elif type_new[2] == "炸弹":
                profit -= 4
            else:
                profit -= 1
        else:
            res = 0
            card1 = cards_type(old['xiadun'])
            card2 = cards_type(new['xiadun'])
            if card1[0] == '两对':
                if card1[1] in [['2', '3'], ['3', '4'], ['4', '5'], ['5', '6'], ['6', '7'], ['7', '8'], ['8', '9'],
                                ['9', '10'], ['10', 'J'], ['J', 'Q'], ['Q', 'K'], ['K', 'J']]:
                    if card2[1] in [['2', '3'], ['3', '4'], ['4', '5'], ['5', '6'], ['6', '7'], ['7', '8'], ['8', '9'],
                                    ['9', '10'], ['10', 'J'], ['J', 'Q'], ['Q', 'K'], ['K', 'J']]:
                        res1 = cards_cmp(card1[1], card2[1])
                        if res1 == 0:
                            res = cards_cmp(card2[2], card1[2])
                        else:
                            res = res1
                    else:
                        res = -1
                else:
                    if card1[1] == card2[1]:
                        res = cards_cmp(card2[2], card1[2])
                    else:
                        res = cards_cmp(card1[1], card2[1])
            elif card1[0] == '三条' or card1[0] == '葫芦' or card1[0] == '炸弹':
                if card1[1] == card2[1]:
                    res = cards_cmp(card2[2], card1[2])
                else:
                    res = cards_cmp(card1[1], card2[1])
            else:
                res = cards_cmp(old['xiadun'], new['xiadun'])
            #res = cards_cmp(old['xiadun'], new['xiadun'])
            if res > 0:
                if type_new[1] == '同花顺':
                    profit += 10
                elif type_new[1] == "炸弹":
                    profit += 8
                elif type_new[1] == "葫芦":
                    profit += 2
                else:
                    profit += 1
            elif res < 0:
                if type_new[1] == '同花顺':
                    profit -= 10
                elif type_new[1] == "炸弹":
                    profit -= 8
                elif type_new[1] == "葫芦":
                    profit -= 2
                else:
                    profit -= 1

        # 计算中墩盈利
        if cards_order[type_old[1]] < cards_order[type_new[1]]:
            if type_new[1] == '同花顺':
                profit += 10
            elif type_new[1] == "炸弹":
                profit += 8
            elif type_new[1] == "葫芦":
                profit += 2
            else:
                profit += 1
        elif cards_order[type_old[1]] > cards_order[type_new[1]]:
            if type_new[1] == '同花顺':
                profit -= 10
            elif type_new[1] == "炸弹":
                profit -= 8
            elif type_new[1] == "葫芦":
                profit -= 2
            else:
                profit -= 1
        else:
            res = 0
            card1 = cards_type(old['zhongdun'])
            card2 = cards_type(new['zhongdun'])
            if card1[0] == '两对':
                if card1[1] in [['2', '3'], ['3', '4'], ['4', '5'], ['5', '6'], ['6', '7'], ['7', '8'],
                                ['8', '9'],
                                ['9', '10'], ['10', 'J'], ['J', 'Q'], ['Q', 'K'], ['K', 'J']]:
                    if card2[1] in [['2', '3'], ['3', '4'], ['4', '5'], ['5', '6'], ['6', '7'], ['7', '8'],
                                    ['8', '9'],
                                    ['9', '10'], ['10', 'J'], ['J', 'Q'], ['Q', 'K'], ['K', 'J']]:
                        res1 = cards_cmp(card1[1], card2[1])
                        if res1 == 0:
                            res = cards_cmp(card2[2], card1[2])
                        else:
                            res = res1
                    else:
                        res = -1
                else:
                    if card1[1] == card2[1]:
                        res = cards_cmp(card2[2], card1[2])
                    else:
                        res = cards_cmp(card1[1], card2[1])
            elif card1[0] == '三条' or card1[0] == '葫芦' or card1[0] == '炸弹':
                if card1[1] == card2[1]:
                    res = cards_cmp(card2[2], card1[2])
                else:
                    res = cards_cmp(card1[1], card2[1])
            else:
                res = cards_cmp(old['zhongdun'], new['zhongdun'])

            #res = cards_cmp(old['zhongdun'],new['zhongdun'])
            if res > 0:
                if type_new[1] == '同花顺':
                    profit += 10
                elif type_new[1] == "炸弹":
                    profit += 8
                elif type_new[1] == "葫芦":
                    profit += 2
                else:
                    profit += 1
            elif res < 0:
                if type_new[1] == '同花顺':
                    profit -= 10
                elif type_new[1] == "炸弹":
                    profit -= 8
                elif type_new[1] == "葫芦":
                    profit -= 2
                else:
                    profit -= 1

        #计算上墩盈利
        if cards_order[type_old[0]] < cards_order[type_new[0]]:
            profit += 1
        elif cards_order[type_old[0]] > cards_order[type_new[0]]:
            profit -= 1
        else:
            profit += cards_cmp(old['shangdun'], new['shangdun'])

        if profit > 0:
            return [True,new]
        else:
            return [False,[]]