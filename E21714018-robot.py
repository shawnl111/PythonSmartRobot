import random
from joke import sayjokes
from translate import translate
from playmusic import playmusic
from weather import inquire
from websearch import search
from game import game
welcome = ['您现在想做什么呢？','有何吩咐?','我能为您帮忙吗?']
ask = ['您还想做什么呢？','我还有很多智慧的功能哦，来和我一起玩吧','我还能为您做点什么？']
notunderstand = ['这个问题我还不会，我还在努力学习中','太难了，说点简单的吧~','不好意思，我暂时还听不懂你的问题']

def robot (s):
    while s.upper() != 'BYE':
        if s == "计算":
            calcstr = str(input('请输入计算表达式：\n\t\t\t\t\t\t'))
            print('计算结果为：{}'.format(eval(calcstr)))
        elif s == '玩游戏': 
            n = int(input("我会玩：\n\n１．猜数\n２．掷骰子\n\n你想要玩哪个呢？\n\t\t\t\t\t\t"))
            game(n)
        elif s == "听歌":
            playmusic()
        elif s == "翻译":
            translate()
        elif s == "讲笑话":
            sayjokes()
        elif s == "查询天气":
            inquire()
        elif s == "搜索关键词":
            search()
        elif s == "厉害" or s == "真棒":
            print("谢谢夸奖～")
        else:
            print(random.choice(notunderstand))
        s = str(input("\n{},{}\n\t\t\t\t\t\t".format(user,random.choice(ask))))
    print("{},下次再会~\n".format(user))

user=str(input("嗨！您好，我是小安~\n请问您如何称呼？\n\t\t\t\t\t\t"))
s=str(input("{},{}\n\t\t\t\t\t\t".format(user,random.choice(welcome))))

if s.upper()!="BYE":
    robot(s)
