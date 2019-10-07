from shunzi_judge import  *
tonghuashun_of_3cards_count = 0     #3张顺子牌型个数
tonghuashun_of_5cards_count = 0     #5张顺子牌型个数

def num_count(num):
    if num == 0:
        return
    global tonghuashun_of_5cards_count
    global tonghuashun_of_3cards_count
    if num:
        if num == 3:
            tonghuashun_of_3cards_count += 1

        elif num == 5:
            tonghuashun_of_5cards_count += 1

        elif num == 8:
            tonghuashun_of_5cards_count += 1
            tonghuashun_of_3cards_count += 1

        elif num == 10:
            tonghuashun_of_5cards_count += 2

def SanTongHuaShun(cards):
    global tonghuashun_of_3cards_count
    global tonghuashun_of_5cards_count
    tonghua = {'*':"",'#':"",'$':"",'&':""}

    for pai_i in cards:
        if '*' in pai_i:
            pai_i = pai_i.strip('*')
            tonghua['*'] += pai_i
        elif '$' in pai_i:
            pai_i = pai_i.strip('$')
            tonghua['$'] += pai_i
        elif '&' in pai_i:
            pai_i = pai_i.strip('&')
            tonghua['&'] += pai_i
        elif '#' in pai_i :
            pai_i = pai_i.strip('#')
            tonghua['#'] += pai_i

    #四种花色组成的顺子（如果存在）牌型
    meihua = tonghua['*']
    heitao = tonghua['$']
    hongtao = tonghua['$']
    fangkuai = tonghua['#']

    #梅花同花顺个数
    num = ShunZi_Judge(meihua)
    num_count(num)

    #黑桃同花顺个数
    heitaotonghuashun_num = ShunZi_Judge(heitao)
    num_count(heitaotonghuashun_num)

    #红桃同花顺个数
    hongtaotonghuashun_num = ShunZi_Judge(hongtao)
    num_count(hongtaotonghuashun_num)

    #方块同花顺
    fangkuaitonghuashun_num = ShunZi_Judge(fangkuai)
    num_count(fangkuaitonghuashun_num)

    #判断是否为3同花顺即3+5+5牌型
    if tonghuashun_of_5cards_count == 2 and tonghuashun_of_3cards_count == 1:
        return True
    return False
