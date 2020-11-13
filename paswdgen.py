import random


def keygen():
    password_lengths = [8,16]
    size = password_lengths[random.randrange(0,len(password_lengths))]
    password = ""
    alpha_upper =  []
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in alpha :
        alpha_upper.append(i.upper())
    digit = ['0','1','2','3','4','5','6','7','8','9']
    spclChar = ['~','`','!','@','#','$','%','^','&','*','(',')','-','+','=','#','{','}',':',';',"'",'"','<','>',',','.','/','?','|']
    dataset = [alpha,alpha_upper,digit,spclChar]
    for i in range(size):
        data =random.randrange(0,len(dataset))
        if data == 0 :
            char = random.randrange(0,len(alpha))
        elif data == 1 :
            char = random.randrange(0,len(alpha_upper))
        elif data == 2:
            char = random.randrange(0,len(digit))
        elif data == 3 :
            char = random.randrange(0,len(spclChar))
        password = password + dataset[data][char]
    return password



