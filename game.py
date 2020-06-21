import random

def game(n):
    if n == 1:
        print("\n好的，猜数．．．\n\n请在心里想一个1~100的整数\n．．．\n")
        a=1
        b=100
        c=int((a+b)/2)
        while 1:
            s = str(input("请问这个数比{}大吗？\n\t\t\t\t\t\t".format(c)))
            if s =="不" or s =="不是" or s =="否":
                if c-a==1 or c -b ==1:
                    t = str(input("请问这个数是{}吗？\n\t\t\t\t\t\t".format(c)))
                    if t == "是" or t == "是的":
                        print("我猜到了吧，厉不厉害～\n\t\t\t\t\t\t");
                        break;
                else:
                    b=c
                    c=int((a+b)/2)
            else:
                a=c
                c=int((a+b)/2)

        
    elif n == 2:
        print("\n好的，掷骰子．．．\n\n")
        usernum = random.randint(1,6)
        robotnum = random.randint(1,6)
        if usernum>robotnum:
            output = "你赢啦，真厉害！"
        elif usernum == robotnum:
            output = "我们是平局哦～"
        else:
            output = "嘿嘿，我赢啦～"
        print("你的骰子数是：{}\n我的骰子数是：{}\n{}".format(usernum,robotnum,output))
    else:
        s = int(input("输错啦，重新选择正确的序号吧～\n\t\t\t\t\t\t"))
        game(s)