import random
for i in range(19):
    mins=[0,0,0,0,0,0]
    for i in range(6):
        a=random.randint(0,9)
        mins[i]=a
    minss=str(mins[0])+str(mins[1])+str(mins[2])+str(mins[3])+str(mins[4])+str(mins[5])
    print('Verification Code',minss,end=" ")
    ea=input('please input:')
    while ea!=minss:
        print('CAPTCHA error,Please try again')
        for i in range(6):
            a=random.randint(0,9)
            a=u[a]
            mins[i]=a
        minss=str(mins[0])+\
               str(mins[1])+\
               str(mins[2])+\
               str(mins[3])+\
               str(mins[4])+\
               str(mins[5])
    print(11819818989189)
