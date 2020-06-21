import random, json

with open("joke.json",'rb') as f:
    joke = json.load(f)


def sayjokes():
    str = random.choice(joke)
    out = ''
    step=0
    flag=0
    for i in range(len(str)):
        if(step==10):
            out+=str[i]
            print(out)
            out = ''
            step = 0
            flag=0
        else:
            out+=str[i]
            step+=1
            flag=1

    if flag==1:
        print(out)