#!/usr/bin/env
#-*- coding: UTF-8 -*-

version  =  0.2.2.4

build_version  =  0.9.1.14920
import sys,gc,datetime,webbrowser,random,os
import calendar as cal
import hh,tujian
import time as t
import turtle as t1
# import some modules

def xiugay(m1919810):
    for i in range(2):
        print('修改中!')
        t.sleep(1)
        print('修改中!!')
        t.sleep(1)
        print('修改中!!!')
        t.sleep(1)
    def tailand(haaasfsa):
        t1.color('red','yellow')
        t1.hideturtle()
        t1.speed(35)
        t1.goto(-100,-10)
        t1.begin_fill()
        for i in range(50):
            t1.forward(200)
            t1.left(170)
        t1.end_fill()
    def LMX(x,y,d):
        t1.penup()
        t1.goto(x, y)
        t1.pendown()
        t1.seth(60)
        for i in range(3):
            t1.fd(d)
            t1.left(120)
        t1.pu()
        t1.goto(x, -y)
        t1.pd()
        t1.seth(-60)
        for i in range(3):
            t1.fd(d)
            t1.right(120)
            t1.hideturtle()
    def yuan(r):
        t1.pu()
        t1.goto(-r*pow(3,0.5)/2, -r/2)
        t1.pd()
        t1.circle(r)
        t1.hideturtle()
    def sixy(x,y,r):
        def txyuan(x,y,r):
            t1.seth(0)
            y = y - r
            t1.pu()
            t1.goto(x, y)
            t1.pd()
            t1.pensize(2)
            t1.circle(r)
            t1.pu()
            t1.goto(x, y+3)
            t1.pd()
            r=r-3
            y=y-r
            t1.circle(r)
        t1.color("#5daed9") 
        txyuan(x,y,r)
        txyuan(-x,y,r)
        txyuan(-x,-y,r)
        txyuan(x,-y,r)
        txyuan(175,0,r)
        txyuan(-175,0,r)
        t1.hideturtle()
    def lbx(x,y):
        t1.penup()
        t1.goto(x, y)
        t1.pendown()
        for i in range(6):
            t1.fd(180)
            t1.left(60)
        t1.hideturtle()
    def yue(x,y,r):
        y=y-r
        t1.penup()
        t1.goto(x,y)
        t1.pendown() 
        t1.circle(r)
        t1.circle(r-10)
        t1.hideturtle()
    def xingzuo(r,c,h):
        t1.penup()
        t1.pencolor("#fdcfad")
        t1.goto(-10,-10)
        t1.seth(-45)
        t1.fd(r)
        t1.pendown()
        xz=['♒','♓','♈','♉','♌','♍','♎','♏','♊','♋','♐','♑']
        for i in range(12):
            t1.write(xz[(i+h)%12],font=("", c, ""))
            t1.penup()
            t1.right(90)
            t1.circle(-r, 30)
            t1.left(90)
            t1.pendown()
        t1.hideturtle()
    def xingdui(r):
        for i in range(1,5):
            te=3
            t1.penup()
            t1.goto(0, 0)
            t1.seth(i * 90)
            t1.pendown()
            t1.right(22.5)
            t1.fd(r)
            if i==1:
                t1.goto(0,3*r-te)
                t1.goto(0,0)
                t1.seth(i * 90 + 22.5)
                t1.fd(r)
                t1.goto(0,3*r-te)
            elif i==2:
                t1.goto(-3*r+te,0)
                t1.goto(0,0)
                t1.seth(i*90+22.5)
                t1.fd(r)
                t1.goto(-3*r+te,0)
            elif i==3:
                t1.goto(0,-3*r+te)
                t1.goto(0,0)
                t1.seth(i*90+22.5)
                t1.fd(r)
                t1.goto(0,-3*r+te)
            else:
                t1.goto(3*r+te,0)
                t1.goto(0,0)
                t1.seth(i*90+22.5)
                t1.fd(r)
                t1.goto(3*r+te,0)
            t1.hideturtle()
        x=pow(((2*r)**2)/2,0.5)-8
        for i in range(1,5):
            t1.pu()
            t1.goto(0, 0)
            t1.seth(i * 90)
            t1.pendown()
            t1.right(22.5)
            t1.fd(r)
            if i==1:
                t1.goto(x,x)
                t1.goto(0,0)
                t1.right(45)
                t1.fd(r)
                t1.goto(x,x)
            elif i==2:
                t1.goto(-x,x)
                t1.goto(0, 0)
                t1.right(45)
                t1.fd(r)
                t1.goto(-x,x)
            elif i==3:
                t1.goto(-x,-x)
                t1.goto(0,0)
                t1.right(45)
                t1.fd(r)
                t1.goto(-x,-x)
            else:
                t1.goto(x,-x)
                t1.goto(0,0)
                t1.right(45)
                t1.fd(r)
                t1.goto(x,-x)
            t1.hideturtle()
    def lx(rd,l,q,j):
        def Skip(step):
            t1.pu()
            t1.fd(step)
            t1.pd()
        CLA=['yellow','#7ecff1','black']
        for a in range(l):
            t1.pu()
            t1.goto(0,0)
            t1.pendown()
            degree=-360/l*a+q
            t1.seth(degree)
            Skip(rd)
            t1.begin_fill()
            t1.fillcolor(CLA[j])
            t1.pencolor(CLA[j])
            t1.right(30)
            t1.fd(25)        
            LZ=[60,120,60]
            for i in range(3):
                t1.left(LZ[i])
                t1.fd(25)
            t1.end_fill()
        t1.hideturtle()
    def stars(m):
        CLQ=['yellow','#7ecff1']
        for i in range(m):
            a=random.uniform(-m*2,m*2)
            b=random.uniform(-m*2,m*2)
            t1.begin_fill()
            t1.penup()
            t1.goto(a,b)
            t1.pendown()
            t1.speed(900)
            t1.fillcolor(CLQ[m%2])
            t1.pencolor(CLQ[m%2])
            t1.circle(m/200)
            t1.end_fill()
            t1.hideturtle()
    '''
    初始化
    '''
    t1.setup(1.0,1.0,0,0)
    t1.bgcolor("black")
    t1.pencolor("#7ecff1")
    t1.hideturtle()
    mt=["#0489D4","#d9f1f1"]
    mv=["#6cd1ef","#d9f1f1"]
    for i in range (2):
        t1.speed(3)
        t1.delay(0)
        t1.pensize(2-i*1.2)
        t1.color(mt[i]) 
        LMX(0,-70,122.5)
        LMX(0,-100,175)
        t1.pensize(3-i*1.6)
        t1.color(mv[i]) 
        LMX(0,-200,350)
        LMX(0,-220,385)
    nc=["#94d5f0","#acdefa"]
    for i in range(2):
        t1.speed(13)
        t1.pensize(3-i*1.5)
        t1.pencolor(nc[i])
        yuan(220+i)
        yuan(250+i)
        yuan(258+i)
        t1.pensize(1)
        t1.pencolor("#389bc8")
        t1.speed(6)
        yuan(100+i)
        yuan(110+i)
        yuan(35+i)
        yuan(30+i)
    t.sleep(0.5)
    t1.speed(5)
    sixy(86,155,40)
    BT=["#54B6D8","#f0efeb"]
    t1.speed(10)
    for i in range(2):
        t1.speed(5)
        t1.delay(0)
        t1.color(BT[i])
        t1.pensize(3-i*1.6)
        t1.seth(-12)
        lbx(-123,-135.88)
        t1.seth(0)
        lbx(-90,-155.88)
        t1.seth(12)
        lbx(-57,-175.88)
    t1.speed(10)
    t1.pencolor("#5daed9")
    t1.pensize(1.3)
    ZR=[-150,30,300,120]
    for i in range(4):
        t1.seth(ZR[i])
        yue(0,53,50)
    t1.delay(0)
    t1.pu()
    t1.goto(-400, 20)
    t1.pd()
    xingzuo(235,15,0)
    for i in range(2):
        t1.pensize(10-7.7*i)
        t1.speed(12)
        t1.pu()
        t1.goto(0, -254+i*34)
        t1.pd() 
        t1.pencolor("black")
        t1.seth(0)
        t1.circle(254-i*34)
    t.sleep(2)
    t1.speed(35)
    for i in range(15):
        t1.pu()
        t1.goto(0,-240-i*4.5)
        t1.pd()
        t1.pencolor("black")
        t1.pensize(35)
        t1.seth(0)
        t1.circle(240+i*4.5)
        xingzuo(240+i*4.5,17,i)
    t.sleep(1.5)
    t1.speed(15)
    t1.pencolor("yellow")
    t1.pensize(0.7)
    xingdui(30)
    t.sleep(2)
    t1.reset()
    CL=['#7ecff1','yellow','#7ecff1','yellow']
    j=0
    for i in range(30,91,20):
        t1.delay(0)
        t1.pensize(0.1*(i-20)/10+0.7)
        t1.pencolor(CL[j])
        t1.speed(30)
        xingdui(i)
        t.sleep(1)
        j=j+1
        t1.reset()
    j=0
    t1.pencolor("yellow")
    t1.pensize(1.4)
    t1.speed(30)
    xingdui(90)
    t1.speed(50)
    t1.delay(0)
    lx(280,8,0,0)
    t.sleep(1)
    lx(340,24,0,1)
    t.sleep(1)
    lx(400,8,0,0)
    t.sleep(1.5)
    lx(280,8,0,2)
    lx(340,24,0,2)
    lx(400,8,0,2)
    t.sleep(0.75)
    for i in range(3):
        t1.speed(150+i*100)
        t1.delay(0)
        lx(380+i*150,12,0,1)
        lx(380+i*150,6,0,0)
    t1.speed(20)
    stars(51)
    stars(100)
    stars(301)
    t1.pu()
    t1.home()
    t1.pd()
    tailand(114514)
    t1.home()
    t1.pencolor('blue')
    t1.speed(100)
    t1.hideturtle()
    for i in range(92):
        t1.forward(i)
        t1.left(91)
    t1.ht()
    t1.speed(0) 
    t1.pensize(2)
    t1.color(1,1,1)
    r = 10
    t1.pu()
    t1.goto(0,-r)
    t1.pd()
    acc_ext  = 0
    for _ in range(1000):
        t1.color(random.choice([(0,0,0),(1,1,1)]))
        ext = random.random() * 90
        t1.circle(r, ext)
        acc_ext += ext
        if acc_ext > 360:
          acc_ext  = 0
          r+= 3
          t1.pu()
          t1.goto(0,-r)
          t1.seth(0)
          t1.pd()
    t1.home()
    t1.pencolor('blue')
    t1.write('修改成功',align="center",font=("宋体",20,"normal"))
    t.sleep(3)
    t1.reset()
    print('修改已完成')
    os.startfile('.\ikun\\num2.txt')

def sqrt(m):
    x0 = m/2 #初始点，也可以是别的值
    x1 = x0/2 + m/(x0*2)
    while abs(x1-x0)>1e-5:
        x0 = x1
        x1 = x0/2 + m/(x0*2)
def CN_fanti_print(qwe):
    print('你幹甚麽')
def CN_print(qwe):
    print('宁干甚么')
def US_print(qwe):
    print('What do you want to do ?')
def CN_fanti_allthing(qwe):
    def fileeee(qwe):
        file_name=r'./'
        m1="▫"
        m2="▪"
        m3=0
        scale = 50
        start = t.perf_counter()
        
        def file_count(file_dir):
            """

            # file count
            
            """
            count = 0
            for root, dirs, files in os.walk(file_dir):
                count += len(files)
            return count
        def file_size(file_dir):
            """

            # file size

            """
            size = 0
            for root, dirs, files in os.walk(file_dir):
                for file in files:
                    size+=os.path.getsize(os.path.join(root, file))
            return size
        for i in range(scale + 1):
            m4=m3%2
            if m4==0:
                m5=m1+m2
            else :
                m5=m2+m1
            a = "█" * i
            b = "." * (scale - i)
            c = (i / scale) * 100
            dur = t.perf_counter() - start
            print("\r>> LOADING {:^3.0f}%[{}{}]{:.2f}s {}".format(c,a,b,dur,m5))
            m3+=1
        print('OK')
        a12345=file_count(file_name)
        a09876=file_size(file_name)
        print()
        print()
        import this
        print()
        for root,dirs,files in os.walk("./"):
            print(root)
            print(dirs)
            print(files,'\n')
        print('本文件夾有',a12345,'個文件')
        print('本文件夾有',a09876,'個 B 大')
        print('本文件夾有',(a09876)/1024,'個 KB 大')
        print('本文件夾有',(a09876)/1024/1024,'個 MB 大')
        print('本文件夾有',(a09876)/1024/1024/1024,'個 GB 大')
        del a12345,a09876,file_name,m1,m2,m3,m4,m5,i,scale,start,dur,a,b,c
        gc.collect()
        hh.Print()
        print('dingdong,開機成功')
    fileeee(1)
    num1='114514'
    with open('.\ikun\\num2.txt','r') as f1:
        num2=f1.readline()# give "num2
    with open('.\ikun\\sincow.txt','r') as fm:
        sincow=fm.readline()
        sincow=int(float(sincow))
    mins=[0,0,0,0,0,0]
    u=list(range(10))
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
    print('此處是驗證碼',minss,end=" ")
    ea=input('親輸入驗證碼:')
    if minss=='114514':
        print('哼哼哼哈哈哈哈哈哈哈哈~~~~~~~~~~')
        ea=minss
    if ea=='114514' or ea=='1919810':
        ea=minss
        print('好吧,勉強讓你過')
    while ea!=minss:
        print('驗證碼驗證失敗，請重試')
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
        if minss=='114514':print('哼哼哼哈哈哈哈哈哈哈哈~~~~~~~~~~')
        print('此處是驗證碼',minss,end=" ")
        ea=input('親輸入驗證碼:')
        if ea=='114514' or ea=='1919810':
            ea=minss
            print('好吧,勉強讓你過')
    del mins,minss
    del a
    gc.collect()
    print('驗證碼驗證成功')
    print('hallo,world =) ')
    
    m=input('請登錄,此處寫公共密碼:')
    while m!=num1:
        print('登陸失敗,請重試')
        m=input('請登錄,此處寫公共密碼:')
    print('登陸成功')
    print('你好,用戶')

    ea=input('請您選擇用戶:1:boss,2:user,3:worker,4:roadman:')

    while 1:
        f=input('1:返回,2:繼續')
        if f=='1':
            print("Good bye!")
            ea=input('請您選擇用戶:1:boss,2:user,3:worker,4:roadman:')
        elif f=='2':
            if ea=='1':
                x=input('請登錄,此處寫密碼:')
                while x!=num2:
                    print('登陸失敗,請重試')
                    f=input('1:返回,2:繼續')
                    if f=='1':
                        print("Good bye!")
                        ea=input('請您選擇用戶:1:boss,2:user,3:worker,4:roadman:')
                    elif f=='2':x=input('請登錄,此處寫密碼:')
                    else:print('error')
                print('boss,您好')
                boss=1
                user=0
                worker=0
                roadman=0
                break
            if ea=='2':
                print('user,您好')
                boss=0
                user=1
                worker=0
                roadman=0
                break
            elif ea=='3':
                print(' worker,你好')
                boss=0
                user=0
                worker=1
                roadman=0
                break
            elif ea=='4':
                print('roadman,快去幹活')
                boss=0
                user=0
                worker=0
                roadman=1
                break
            elif ea=='114514' or ea=='1919810':
                print('哼哼哈哈哈哈哈哈哈~~~~~~')
                print('怎麽到處都是homo(惱)',end=" ")
                print('滾')
                ea=input('請您選擇用戶:1:boss,2:user,3:worker,4:roadman:')
            else:
                print('error')
                ea=input('請您選擇用戶:1:boss,2:user,3:worker,4:roadman:')
        else:
            print('error')
    
    while 1:
        CN_fanti_print(1)
        print('0:開始菜單')
        print("1:時間,2:日期排序")
        print('3:退出賬號')
        if boss==1:
            print("4:演示,5:密碼更改")
        a=input('請輸入:')
        if a=='0':
            while 1:
                print('開始菜單')
                CN_fanti_print(1)
                print("1:計算器")
                print('2:退出')
                a=input('請輸入:')
                if a=='1':
                    while 1:
                        f=input('1:返回,2:繼續')
                        if f=='1':
                            print("Good bye!")
                            break
                        elif f=='2':
                            print('1:加,2:減,3:乘,4:除:')
                            print('5:乘方,6:平方根,7:素數:')
                            print('8:9*9乘法表,9:因式分解,10:π:')
                            print('11:解一元一次方程,12:解一元二次方程:')
                            m=input('幹什麽:')
                                
                            if m=='1':
                                n1=int(input('請輸入一個數字'))
                                n2=int(input('請輸入另一個數字'))
                                print(n1+n2)
                            elif m=='2':
                                n1=int(input('請輸入一個數字'))
                                n2=int(input('請輸入另一個數字'))
                                print(n1-n2)
                            elif m=='3':
                                n1=int(input('請輸入一個數字'))
                                n2=int(input('請輸入另一個數字'))
                                print(n1*n2)
                            elif m=='4':
                                try:
                                    counttt=input('1:除,2:除(取整),6:除(取余)')
                                    n1=int(input('請輸入一個數字'))
                                    n2=int(input('請輸入另一個數字'))
                                    if n2==0:
                                        print('…………？')
                                    if counttt=='1':
                                        print(n1/n2)
                                    if counttt=='2':
                                        print(n1//n2)
                                    if counttt=='3':
                                        print(n1%n2)
                                except ZeroDivisionError:
                                    print('哼！')
                            elif m=='5':
                                n1=int(input('請輸入一個數字'))
                                n2=int(input('請輸入另一個數字'))
                                n1=(n1)**(n2)
                                print(n1)
                            elif m=='6':
                                n1=int(input('請輸入一個數字'))
                                n1=sqrt(n1)
                                print(n1)
                            elif m=='7':
                                p1=0
                                a=int(input('請輸入範圍(2<=a<=i):'))
                                b=int(input('請輸入範圍(i<=b):'))
                                for m in range(a,b+1):
                                    if m>=2:
                                        for i in range(2,m):
                                            if m%i==0:break
                                        else:
                                            p1=p1+1
                                            print(m,"是素數")
                                    else:print('error')
                                print("Good bye!")
                                print('有{0}個素數'.format(p1))
                                p1=0
                            elif m=='8':
                                for i in range(1, 10):
                                    print( )
                                    for j in range(1, i+1):
                                        print('{0}*{1}+={2}'.format(i,j,i*j),end=" ")
                                print('')
                            elif m=='9':
                                print('請不要輸入非負數或字符!')
                                n=int(input('請輸入一個數字(因式分解):'))
                                print('{}='.format(n),end="")
                                if not isinstance(n,int) or n<=0:
                                    print('請輸入一個正確的數字!')
                                    n=int(input('請輸入一個數字(因式分解):'))
                                    print('{}='.format(n),end="")
                                elif n in [1]:print('{0}'.format(n),end="")
                                while n not in [1]:
                                    for index in range(2,n+1):
                                        if n%index==0:
                                            n//=index
                                            if n==1:print(index,end="")
                                            else:print ('{0} *'.format(index),end=" ")
                                            break
                                print()
                            elif m=='10':
                                n=10000+4
                                p=2*10**n
                                a=p//3;p+=a
                                i=2
                                while a>0:
                                    a=a*i//(i*2+1);i+=1
                                    p+=a
                                p//=10000
                                with open('.\ikun\\pi.txt', "w", encoding="utf-8") as f1m1:f1m1.write(p)
                                os.startfile('.\ikun\\pi.txt')
                                print('已計算')
                                del n,p,a,i
                                gc.collect()
                            elif m=='11':
                                while 1:
                                    print('ax+b=c')
                                    a=float(input('a=   ,(a!=0)'))
                                    if a==0:print('a不得等於0')
                                    else:break
                                b=float(input('b=    '))
                                c=float(input('c=    '))
                                a114514=(c-b)/a
                                print('x=',a114514)
                            elif m=='12':
                                while 1:
                                    while 1:
                                        print('ax^2+bx+c=d')
                                        a=float(input('a=   ,(a!=0)'))
                                        if a==0:print('a不得等於0')
                                        else:break
                                    b=float(input('b=    '))
                                    c=float(input('c=    '))
                                    d=float(input('d=    '))
                                    a1919810=((4*a*d)-(4*a*c)+((b)**2))
                                    if a1919810<0:
                                        print('error')
                                    else:
                                        a19198101=(-b+sqrt(a1919810))/(2*a)
                                        a19198102=(-b-sqrt(a1919810))/(2*a)
                                        print('x1=',a19198101)
                                        print('x2=',a19198102)
                                        break
                            else:
                                print('error')
                        else:
                            print('error')
                elif a=='2':
                    break
                else:print('error')
        elif a=='1':
            while 1:
                f=int(input('1:返回,2:繼續'))
                if f==1:
                    print("Good bye!")
                    break
                elif f==2:
                    def get_month_days(year, month):
                        if month >12 or month <= 0:
                            return -1
                        if month == 2:
                            return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
                        if month in (4, 6, 9, 11):
                            return 30
                        else:
                            return 31
                    print(t.strftime("%Y-%m-%d %H:%M:%S",t.localtime(t.time())))
                    year=int(t.strftime("%Y"))
                    month=int(t.strftime('%m'))
                    print("本月{}天".format(get_month_days(year,month)))
                    cal1=cal.month(year,month)
                    print("以下輸出{0}年{1}月份的日歷:".format(year,month))
                    print(cal1)
                    day=int(t.strftime('%d'))
                    months = (0,31,59,90,120,151,181,212,243,273,304,334)
                    sum=months[month - 1]
                    sum+=day
                    leap=0
                    if year%4==0 or year%400==0:leap=1
                    if leap==1 and month>2:sum+=1
                    print ('它是第%d天'%sum)
                    leap=0
                else:print('error')
        elif a=='2':
            while 1:
                f=int(input('1:返回，2:繼續'))
                if f==1:
                    print(" Good bye!")
                    break
                elif f==2:
                    year= int(float(input('年:')))
                    month=int(float(input('月:')))
                    day = int(float(input('日:')))
                    def get_month_days(year, month):
                        if month >12 or month <= 0:
                            return -1
                        if month == 2:
                            return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
                        if month in (4, 6, 9, 11):
                            return 30
                        else:
                            return 31
                    print("本月{}天".format(get_month_days(year,month)))
                    months= (0,31,59,90,120,151,181,212,243,273,304,334)
                    if 0<month<=12:sum=months[month - 1]
                    else:print('error')
                    if 0<day<=31:pass
                    else:print('error')
                    sum+=day
                    leap=0
                    if year%4==0 or year%400==0:leap=1
                    if leap==1 and month>2:sum+=1
                    print ('它是第%d天'%sum)
                    leap=0
                else :print('error')
        elif a=='3':
            ea=input('請您選擇用戶:1:boss,2:user,3:worker,4:roadman:')
            while 1:
                f=input('1:返回,2:繼續')
                if f=='1':
                    print("Good bye!")
                    ea=input('請您選擇用戶:1:boss,2:user,3:worker,4:roadman:')
                elif f=='2':
                    if ea=='1':
                        x=input('請登錄,此處寫密碼:')
                        while x!=num2:
                            print('登陸失敗,請重試')
                            f=input('1:返回,2:繼續')
                            if f=='1':
                                print("Good bye!")
                                ea=input('請您選擇用戶:1:boss,2:user,3:worker,4:roadman:')
                            elif f=='2':x=input('請登錄,此處寫密碼:')
                            else:print('error')
                        print('boss,您好')
                        boss=1
                        user=0
                        worker=0
                        roadman=0
                        break
                    if ea=='2':
                        print('user,您好')
                        boss=0
                        user=1
                        worker=0
                        roadman=0
                        break
                    elif ea=='3':
                        print(' worker,你好')
                        boss=0
                        user=0
                        worker=1
                        roadman=0
                        break
                    elif ea=='4':
                        print('roadman,快去幹活')
                        boss=0
                        user=0
                        worker=0
                        roadman=1
                        break
                    elif ea=='114514' or ea=='1919810':
                        print('哼哼哈哈哈哈哈哈哈~~~~~~')
                        print('怎麽到處都是homo(惱)')
                        print('滾！')
                        ea=input('請您選擇用戶:1:boss,2:user,3:worker,4:roadman:')
                    else:
                        print('error')
                        ea=input('請您選擇用戶:1:boss,2:user,3:worker,4:roadman:')
                else:print('error')
    
        elif a=='4':
            while 1:
                if boss!=1:
                    if roadman==1:print('※你無權訪問,你越界了！')
                    if worker==1:print('你有這個資格嗎,去工作吧,請')
                    if user==1:print('你沒有足夠的權限')
                f=int(input('1:返回,2:繼續'))
                if f==1:
                    print("Good bye!")
                    break
                elif f==2:
                    a=input('1:普通演示,2:權限演示')
                    if a=='1':
                        while 1:
                            f=input('1:返回,2:繼續')
                            if f=='1':
                                print("Good bye!")
                                break
                            elif f=='2':print('404 Not Found')
                            else:print('error')
                    elif a=='2':
                        while 1:
                            if boss!=1:
                                if roadman==1:
                                    print('※你無權訪問,你越界了！')
                                if worker==1:
                                    print('你有這個資格嗎,去工作吧,請')
                                if user==1:
                                    print('你沒有足夠的權限')
                            f=int(input('1:返回,2:繼續'))
                            if f==1:
                                print("Good bye!")
                                break
                            elif f==2:print('404 Not Found')
                            else:print('error')
                else:print('error')
        elif a=='5':
            while 1:
                if boss!=1:
                    if roadman==1:print('※你無權訪問,你越界了！')
                    if worker==1:print('你有這個資格嗎,去工作吧,請')
                    if user==1:print('你沒有足夠的權限')
                f=int(input('1:返回,2:繼續'))
                if f==1:
                    print("Good bye!")
                    break
                elif f==2:
                    num10=input('boss,請輸入原始密碼:')
                    if num10!=num2:
                        print('密碼錯誤')
                        num10=input('boss,請輸入原始密碼:')
                    num2=input('請輸入新密碼:')
                    xiugay(553717805371)
                    with open('.\ikun\\num2.txt','w') as f2:f2.write(num2)                    
                    print('boss您的新密碼是{0}'.format(num2))
                else:print('error')
        else :
            print('error')
def CN_allthing(qwe):
    def fileeee(qwe):
        file_name=r'./'
        m1="▫"
        m2="▪"
        m3=0
        scale = 50
        start = t.perf_counter()
        
        def file_count(file_dir):
            """

            # file count
            
            """
            count = 0
            for root, dirs, files in os.walk(file_dir):
                count += len(files)
            return count
        def file_size(file_dir):
            """

            # file size

            """
            size = 0
            for root, dirs, files in os.walk(file_dir):
                for file in files:
                    size+=os.path.getsize(os.path.join(root, file))
            return size
        for i in range(scale + 1):
            m4=m3%2
            if m4==0:
                m5=m1+m2
            else :
                m5=m2+m1
            a = "█" * i
            b = "." * (scale - i)
            c = (i / scale) * 100
            dur = t.perf_counter() - start
            print("\r>> LOADING {:^3.0f}%[{}{}]{:.2f}s {}".format(c,a,b,dur,m5))
            m3+=1
        print('OK')
        a12345=file_count(file_name)
        a09876=file_size(file_name)
        print()
        print()
        import this
        print()
        for root,dirs,files in os.walk("./"):
            print(root)
            print(dirs)
            print(files,'\n')
        print('本文件夹有',a12345,'个文件')
        print('本文件夹有',a09876,'个 B 大')
        print('本文件夹有',(a09876)/1024,'个 KB 大')
        print('本文件夹有',(a09876)/1024/1024,'个 MB 大')
        print('本文件夹有',(a09876)/1024/1024/1024,'个 GB 大')
        del a12345,a09876,file_name,m1,m2,m3,m4,m5,i,scale,start,dur,a,b,c
        gc.collect()
        hh.Print()
        print('dingdong,开机成功')
    fileeee(1)
    num1='114514'
    with open('.\ikun\\num2.txt','r') as f1:
        num2=f1.readline()# give "num2
    with open('.\ikun\\sincow.txt','r') as fm:
        sincow=fm.readline()
        sincow=int(float(sincow))
    mins=[0,0,0,0,0,0]
    u=list(range(10))
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
    print('此处是验证码',minss,end=" ")
    ea=input('亲输入验证码:')
    if minss=='114514':
        print('哼哼哼哈哈哈哈哈哈哈哈~~~~~~~~~~')
        ea=minss
    if ea=='114514' or ea=='1919810':
        ea=minss
        print('好吧,勉强让你过')
    while ea!=minss:
        print('验证码验证失败，请重试')
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
        if minss=='114514':print('哼哼哼哈哈哈哈哈哈哈哈~~~~~~~~~~')
        print('此处是验证码',minss,end=" ")
        ea=input('亲输入验证码:')
        if ea=='114514' or ea=='1919810':
            ea=minss
            print('好吧,勉强让你过')
    del mins,minss
    del a
    gc.collect()
    print('验证码验证成功')
    print('hallo,world =) ')
    
    m=input('请登录,此处写公共密码:')
    while m!=num1:
        print('登陆失败,请重试')
        m=input('请登录,此处写公共密码:')
    print('登陆成功')
    print('你好,用户')

    ea=input('请您选择用户:1:boss,2:user,3:worker,4:roadman:')

    while 1:
        f=input('1:返回,2:继续')
        if f=='1':
            print("Good bye!")
            ea=input('请您选择用户:1:boss,2:user,3:worker,4:roadman:')
        elif f=='2':
            if ea=='1':
                x=input('请登录,此处写密码:')
                while x!=num2:
                    print('登陆失败,请重试')
                    f=input('1:返回,2:继续')
                    if f=='1':
                        print("Good bye!")
                        ea=input('请您选择用户:1:boss,2:user,3:worker,4:roadman:')
                    elif f=='2':x=input('请登录,此处写密码:')
                    else:print('error')
                print('boss,您好')
                boss=1
                user=0
                worker=0
                roadman=0
                break
            if ea=='2':
                print('user,您好')
                boss=0
                user=1
                worker=0
                roadman=0
                break
            elif ea=='3':
                print(' worker,你好')
                boss=0
                user=0
                worker=1
                roadman=0
                break
            elif ea=='4':
                print('roadman,快去干活')
                boss=0
                user=0
                worker=0
                roadman=1
                break
            elif ea=='114514' or ea=='1919810':
                print('哼哼哈哈哈哈哈哈哈~~~~~~')
                print('怎么到处都是homo(恼)',end=" ")
                print('滚')
                ea=input('请您选择用户:1:boss,2:user,3:worker,4:roadman:')
            else:
                print('error')
                ea=input('请您选择用户:1:boss,2:user,3:worker,4:roadman:')
        else:
            print('error')
    
    while 1:
        CN_print(1)
        print('0:开始菜单')
        print("1:时间,2:日期排序")
        print('3:退出账号')
        if boss==1:
            print("4:演示,5:密码更改")
        a=input('请输入:')
        if a=='0':
            while 1:
                print('开始菜单')
                CN_print(1)
                print("1:计算器")
                print('2:退出')
                a=input('请输入:')
                if a=='1':
                    while 1:
                        f=input('1:返回,2:继续')
                        if f=='1':
                            print("Good bye!")
                            break
                        elif f=='2':
                            print('1:加,2:减,3:乘,4:除:')
                            print('5:乘方,6:平方根,7:素数:')
                            print('8:9*9乘法表,9:因式分解,10:π:')
                            print('11:解一元一次方程,12:解一元二次方程:')
                            m=input('干什么:')
                                
                            if m=='1':
                                n1=int(input('请输入一个数字'))
                                n2=int(input('请输入另一个数字'))
                                print(n1+n2)
                            elif m=='2':
                                n1=int(input('请输入一个数字'))
                                n2=int(input('请输入另一个数字'))
                                print(n1-n2)
                            elif m=='3':
                                n1=int(input('请输入一个数字'))
                                n2=int(input('请输入另一个数字'))
                                print(n1*n2)
                            elif m=='4':
                                try:
                                    counttt=input('1:除,2:除(取整),6:除(取余)')
                                    n1=int(input('请输入一个数字'))
                                    n2=int(input('请输入另一个数字'))
                                    if n2==0:
                                        print('…………？')
                                    if counttt=='1':
                                        print(n1/n2)
                                    if counttt=='2':
                                        print(n1//n2)
                                    if counttt=='3':
                                        print(n1%n2)
                                except ZeroDivisionError:
                                    print('哼！')
                            elif m=='5':
                                n1=int(input('请输入一个数字'))
                                n2=int(input('请输入另一个数字'))
                                n1=(n1)**(n2)
                                print(n1)
                            elif m=='6':
                                n1=int(input('请输入一个数字'))
                                n1=sqrt(n1)
                                print(n1)
                            elif m=='7':
                                p1=0
                                a=int(input('请输入范围(2<=a<=i):'))
                                b=int(input('请输入范围(i<=b):'))
                                for m in range(a,b+1):
                                    if m>=2:
                                        for i in range(2,m):
                                            if m%i==0:break
                                        else:
                                            p1=p1+1
                                            print(m,"是素数")
                                    else:print('error')
                                print("Good bye!")
                                print('有{0}个素数'.format(p1))
                                p1=0
                            elif m=='8':
                                for i in range(1, 10):
                                    print( )
                                    for j in range(1, i+1):
                                        print('{0}*{1}+={2}'.format(i,j,i*j),end=" ")
                                print('')
                            elif m=='9':
                                print('请不要输入非负数或字符!')
                                n=int(input('请输入一个数字(因式分解):'))
                                print('{}='.format(n),end="")
                                if not isinstance(n,int) or n<=0:
                                    print('请输入一个正确的数字!')
                                    n=int(input('请输入一个数字(因式分解):'))
                                    print('{}='.format(n),end="")
                                elif n in [1]:print('{0}'.format(n),end="")
                                while n not in [1]:
                                    for index in range(2,n+1):
                                        if n%index==0:
                                            n//=index
                                            if n==1:print(index,end="")
                                            else:print ('{0} *'.format(index),end=" ")
                                            break
                                print()
                            elif m=='10':
                                n=10000+4
                                p=2*10**n
                                a=p//3;p+=a
                                i=2
                                while a>0:
                                    a=a*i//(i*2+1);i+=1
                                    p+=a
                                p//=10000
                                with open('.\ikun\\pi.txt', "w", encoding="utf-8") as f1m1:f1m1.write(p)
                                os.startfile('.\ikun\\pi.txt')
                                print('已计算')
                                del n,p,a,i
                                gc.collect()
                            elif m=='11':
                                while 1:
                                    print('ax+b=c')
                                    a=float(input('a=   ,(a!=0)'))
                                    if a==0:print('a不得等于0')
                                    else:break
                                b=float(input('b=    '))
                                c=float(input('c=    '))
                                a114514=(c-b)/a
                                print('x=',a114514)
                            elif m=='12':
                                while 1:
                                    while 1:
                                        print('ax^2+bx+c=d')
                                        a=float(input('a=   ,(a!=0)'))
                                        if a==0:print('a不得等于0')
                                        else:break
                                    b=float(input('b=    '))
                                    c=float(input('c=    '))
                                    d=float(input('d=    '))
                                    a1919810=((4*a*d)-(4*a*c)+((b)**2))
                                    if a1919810<0:
                                        print('error')
                                    else:
                                        a19198101=(-b+sqrt(a1919810))/(2*a)
                                        a19198102=(-b-sqrt(a1919810))/(2*a)
                                        print('x1=',a19198101)
                                        print('x2=',a19198102)
                                        break
                            else:
                                print('error')
                        else:
                            print('error')
                elif a=='2':
                    break
                else:print('error')
        elif a=='1':
            while 1:
                f=int(input('1:返回,2:继续'))
                if f==1:
                    print("Good bye!")
                    break
                elif f==2:
                    def get_month_days(year, month):
                        if month >12 or month <= 0:
                            return -1
                        if month == 2:
                            return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
                        if month in (4, 6, 9, 11):
                            return 30
                        else:
                            return 31
                    print(t.strftime("%Y-%m-%d %H:%M:%S",t.localtime(t.time())))
                    year=int(t.strftime("%Y"))
                    month=int(t.strftime('%m'))
                    print("本月{}天".format(get_month_days(year,month)))
                    cal1=cal.month(year,month)
                    print("以下输出{0}年{1}月份的日历:".format(year,month))
                    print(cal1)
                    day=int(t.strftime('%d'))
                    months = (0,31,59,90,120,151,181,212,243,273,304,334)
                    sum=months[month - 1]
                    sum+=day
                    leap=0
                    if year%4==0 or year%400==0:leap=1
                    if leap==1 and month>2:sum+=1
                    print ('它是第%d天'%sum)
                    leap=0
                else:print('error')
        elif a=='2':
            while 1:
                f=int(input('1:返回，2:继续'))
                if f==1:
                    print(" Good bye!")
                    break
                elif f==2:
                    year= int(float(input('年:')))
                    month=int(float(input('月:')))
                    day = int(float(input('日:')))
                    def get_month_days(year, month):
                        if month >12 or month <= 0:
                            return -1
                        if month == 2:
                            return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
                        if month in (4, 6, 9, 11):
                            return 30
                        else:
                            return 31
                    print("本月{}天".format(get_month_days(year,month)))
                    months= (0,31,59,90,120,151,181,212,243,273,304,334)
                    if 0<month<=12:sum=months[month - 1]
                    else:print('error')
                    if 0<day<=31:pass
                    else:print('error')
                    sum+=day
                    leap=0
                    if year%4==0 or year%400==0:leap=1
                    if leap==1 and month>2:sum+=1
                    print ('它是第%d天'%sum)
                    leap=0
                else :print('error')
        elif a=='3':
            ea=input('请您选择用户:1:boss,2:user,3:worker,4:roadman:')
            while 1:
                f=input('1:返回,2:继续')
                if f=='1':
                    print("Good bye!")
                    ea=input('请您选择用户:1:boss,2:user,3:worker,4:roadman:')
                elif f=='2':
                    if ea=='1':
                        x=input('请登录,此处写密码:')
                        while x!=num2:
                            print('登陆失败,请重试')
                            f=input('1:返回,2:继续')
                            if f=='1':
                                print("Good bye!")
                                ea=input('请您选择用户:1:boss,2:user,3:worker,4:roadman:')
                            elif f=='2':x=input('请登录,此处写密码:')
                            else:print('error')
                        print('boss,您好')
                        boss=1
                        user=0
                        worker=0
                        roadman=0
                        break
                    if ea=='2':
                        print('user,您好')
                        boss=0
                        user=1
                        worker=0
                        roadman=0
                        break
                    elif ea=='3':
                        print(' worker,你好')
                        boss=0
                        user=0
                        worker=1
                        roadman=0
                        break
                    elif ea=='4':
                        print('roadman,快去干活')
                        boss=0
                        user=0
                        worker=0
                        roadman=1
                        break
                    elif ea=='114514' or ea=='1919810':
                        print('哼哼哈哈哈哈哈哈哈~~~~~~')
                        print('怎么到处都是homo(恼)')
                        print('滚！')
                        ea=input('请您选择用户:1:boss,2:user,3:worker,4:roadman:')
                    else:
                        print('error')
                        ea=input('请您选择用户:1:boss,2:user,3:worker,4:roadman:')
                else:print('error')
    
        elif a=='4':
            while 1:
                if boss!=1:
                    if roadman==1:print('※你无权访问,你越界了！')
                    if worker==1:print('你有这个资格吗,去工作吧,请')
                    if user==1:print('你没有足够的权限')
                f=int(input('1:返回,2:继续'))
                if f==1:
                    print("Good bye!")
                    break
                elif f==2:
                    a=input('1:普通演示,2:权限演示')
                    if a=='1':
                        while 1:
                            f=input('1:返回,2:继续')
                            if f=='1':
                                print("Good bye!")
                                break
                            elif f=='2':print('404 Not Found')
                            else:print('error')
                    elif a=='2':
                        while 1:
                            if boss!=1:
                                if roadman==1:
                                    print('※你无权访问,你越界了！')
                                if worker==1:
                                    print('你有这个资格吗,去工作吧,请')
                                if user==1:
                                    print('你没有足够的权限')
                            f=int(input('1:返回,2:继续'))
                            if f==1:
                                print("Good bye!")
                                break
                            elif f==2:print('404 Not Found')
                            else:print('error')
                else:print('error')
        elif a=='5':
            while 1:
                if boss!=1:
                    if roadman==1:print('※你无权访问,你越界了！')
                    if worker==1:print('你有这个资格吗,去工作吧,请')
                    if user==1:print('你没有足够的权限')
                f=int(input('1:返回,2:继续'))
                if f==1:
                    print("Good bye!")
                    break
                elif f==2:
                    num10=input('boss,请输入原始密码:')
                    if num10!=num2:
                        print('密码错误')
                        num10=input('boss,请输入原始密码:')
                    num2=input('请输入新密码:')
                    xiugay(553717805371)
                    with open('.\ikun\\num2.txt','w') as f2:f2.write(num2)                    
                    print('boss您的新密码是{0}'.format(num2))
                else:print('error')
        else :
            print('error')
def US_allthing(qwe):
    def fileeee(qwe):
        file_name=r'./'
        m1="▫"
        m2="▪"
        m3=0
        scale = 50
        start = t.perf_counter()
        
        def file_count(file_dir):
            """

            # file count
            
            """
            count = 0
            for root, dirs, files in os.walk(file_dir):
                count += len(files)
            return count
        def file_size(file_dir):
            """

            # file size

            """
            size = 0
            for root, dirs, files in os.walk(file_dir):
                for file in files:
                    size+=os.path.getsize(os.path.join(root, file))
            return size
        for i in range(scale + 1):
            m4=m3%2
            if m4==0:m5=m1+m2
            else :m5=m2+m1
            a = "█" * i
            b = "." * (scale - i)
            c = (i / scale) * 100
            dur = t.perf_counter() - start
            print("\r>> LOADING {:^3.0f}%[{}{}]{:.2f}s {}".format(c,a,b,dur,m5))
            
            m3+=1
            
        a12345=file_count(file_name)
        a09876=file_size(file_name)
        print()
        print()
        import this
        print()
        
        for root,dirs,files in os.walk("./"):
            print(root)
            print(dirs)
            print(files,'\n')
        print('files:',a12345)
        print('large(B):',a09876)
        print('large(KB)',(a09876)/1024)
        print('large(MB)',(a09876)/1024/1024)
        print('large(GB)',(a09876)/1024/1024/1024)
        del a12345,a09876,file_name,m1,m2,m3,m4,m5,i,scale,start,dur,a,b,c
        gc.collect()
        hh.Print()
        print('Welcome!')
    fileeee(1)
    num1='114514'
    with open('.\ikun\\num2.txt','r') as f1:
        num2=f1.readline()# give "num2
    with open('.\ikun\\sincow.txt','r') as fm:
        sincow=fm.readline()
        sincow=int(float(sincow))
    mins=[0,0,0,0,0,0]
    u=list(range(10))
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
        print('Verification Code',minss,end=" ")
        ea=input('please input:')
    del mins,minss
    gc.collect()
    print('OK!')
    print('hallo,world =) ')
    
    m=input('Public password:')
    while m!=num1:
        print('Login failed, please try again')
        m=input('Public password:')
    print('Login successfully')
    print('Hello, user')

    ea=input('Users:1:boss,2:user,3:worker,4:roadman:')

    while 1:
        f=input('1:back,2:continue')
        if f=='1':
            print("Good bye!")
            ea=input('Users:1:boss,2:user,3:worker,4:roadman:')
        elif f=='2':
            if ea=='1':
                x=input('Please log in and write your password here:')
                while x!=num2:
                    print('Login failed, please try again')
                    f=input('1:back,2:continue')
                    if f=='1':
                        print("Good bye!")
                        ea=input('Users:1:boss,2:user,3:worker,4:roadman:')
                    elif f=='2':x=input('Please log in and write your password here:')
                    else:print('error')
                print('Hello,boss')
                boss=1
                user=0
                worker=0
                roadman=0
                break
            if ea=='2':
                print('Hello,user')
                boss=0
                user=1
                worker=0
                roadman=0
                break
            elif ea=='3':
                print('Ah,worker,Hello')
                boss=0
                user=0
                worker=1
                roadman=0
                break
            elif ea=='4':
                print('roadman,get to work!')
                boss=0
                user=0
                worker=0
                roadman=1
                break
            else:
                print('error')
                print('well')
                ea=input('Users:1:boss,2:user,3:worker,4:roadman:')
        else:
            print('error')
    
    while 1:
        US_print(1)
        print('0:Start menu')
        print("1:Time,2:Sort date")
        print('3:Log out')
        if boss==1:print("4:sample,5:Password Change")
        a=input('input:')
        if a=='0':
            print("Here're 'Start menu'")
            US_print(1)
            print("1:calc")
            print('2:back')
            a=input('input:')
            while 1:
                if a=='1':
                    while 1:
                        f=input('1,back,2:continue')
                        if f=='1':
                            print("Good bye!")
                            break
                        elif f=='2':
                            print('1:add,2:minus,3:multiply,4:divide')
                            print('5:involution,6:sqrt,7:prime number')
                            print('8:9*9 tables,9:factorization,10:pi')
                            print('11:linear equation,12:quadratic equation')
                            m=input('input:')
                                
                            if m=='1':
                                n1=int(input('Please input a number'))
                                n2=int(input('Please input another number'))
                                print(n1+n2)
                            elif m=='2':
                                n1=int(input('Please input a number'))
                                n2=int(input('Please input another number'))
                                print(n1-n2)
                            elif m=='3':
                                n1=int(input('Please input a number'))
                                n2=int(input('Please input another number'))
                                print(n1*n2)
                            elif m=='4':
                                try:
                                    counttt=input('1:divide,2:divide(take an integer),6:divide(take the remainder)')
                                    count(1)
                                    if n2==0:
                                        print('NO!')
                                    if counttt=='1':
                                        print(n1/n2)
                                    if counttt=='2':
                                        print(n1//n2)
                                    if counttt=='3':
                                        print(n1%n2)
                                except ZeroDivisionError:
                                    print('Ahhh!~')
                            elif m=='5':
                                n1=int(input('Please input a number'))
                                n2=int(input('Please input another number'))
                                n1=(n1)**(n2)
                                print(n1)
                            elif m=='6':
                                n1=int(input('Please input a number'))
                                n1=sqrt(n1)
                                print(n1)
                            elif m=='7':
                                p1=0
                                a=int(input('input a range(2<=a<=i):'))
                                b=int(input('input a range(i<=b):'))
                                for m in range(a,b+1):
                                    if m>=2:
                                        for i in range(2,m):
                                            if m%i==0:break
                                        else:
                                            p1=p1+1
                                            print(m,"Is A Factorization")
                                    else:print('error')
                                print("Good bye!")
                                print('{0}Factorization'.format(p1))
                                p1=0
                            elif m=='8':
                                for i in range(1, 10):
                                    print( )
                                    for j in range(1, i+1):
                                        print('{0}*{1}+={2}'.format(i,j,i*j),end=" ")
                                print('')
                            elif m=='9':
                                print("Don't input a non-negative number or Str!")
                                n=int(input('input:'))
                                print('{}='.format(n),end="")
                                if not isinstance(n,int) or n<=0:
                                    print('………………？')
                                    n=int(input('input:'))
                                    print('{}='.format(n),end="")
                                elif n in [1]:print('{0}'.format(n),end="")
                                while n not in [1]:
                                    for index in range(2,n+1):
                                        if n%index==0:
                                            n//=index
                                            if n==1:print(index,end="")
                                            else:print ('{0} *'.format(index),end=" ")
                                            break
                                print()
                            elif m=='10':
                                n=10000+4
                                p=2*10**n
                                a=p//3;p+=a
                                i=2
                                while a>0:
                                    a=a*i//(i*2+1);i+=1
                                    p+=a
                                p//=10000
                                with open('.\ikun\\pi.txt', "w", encoding="utf-8") as f1m1:f1m1.write(p)
                                os.startfile('.\ikun\\pi.txt')
                                print('OK!!!')
                                del n,p,a,i
                                gc.collect()
                            elif m=='11':
                                while 1:
                                    print('ax+b=c')
                                    a=float(input('a=   ,(a!=0)'))
                                    if a==0:print("a can't be 0")
                                    else:break
                                b=float(input('b=    '))
                                c=float(input('c=    '))
                                a114514=(c-b)/a
                                print('x=',a114514)
                            elif m=='12':
                                while 1:
                                    while 1:
                                        print('ax^2+bx+c=d')
                                        a=float(input('a=   ,(a!=0)'))
                                        if a==0:print("a can't be 0")
                                        else:break
                                    b=float(input('b=    '))
                                    c=float(input('c=    '))
                                    d=float(input('d=    '))
                                    a1919810=((4*a*d)-(4*a*c)+((b)**2))
                                    if a1919810<0:
                                        print('error')
                                    else:
                                        a19198101=(-b+sqrt(a1919810))/(2*a)
                                        a19198102=(-b-sqrt(a1919810))/(2*a)
                                        print('x1=',a19198101)
                                        print('x2=',a19198102)
                            else:print('error')
                        else:print('error')
                elif a=='2':
                    break
                else:print('error')
        elif a=='1':
            while 1:
                f=int(input('1:back,2:continue'))
                if f==1:
                    print("Good bye!")
                    break
                elif f==2:
                    def get_month_days(year, month):
                        if month >12 or month <= 0:
                            return -1
                        if month == 2:
                            return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
                        if month in (4, 6, 9, 11):
                            return 30
                        else:
                            return 31
                    print(t.strftime("%Y-%m-%d %H:%M:%S",t.localtime(t.time())))
                    year=int(t.strftime("%Y"))
                    month=int(t.strftime('%m'))
                    print("This month {} days!".format(get_month_days(year,month)))
                    cal1=cal.month(year,month)
                    print(" {0} year {1} 月mouth's calendar:".format(year,month))
                    print(cal1)
                    day=int(t.strftime('%d'))
                    months = (0,31,59,90,120,151,181,212,243,273,304,334)
                    sum=months[month - 1]
                    sum+=day
                    leap=0
                    if year%4==0 or year%400==0:leap=1
                    if leap==1 and month>2:sum+=1
                    print ('the %d day'%sum)
                    leap=0
                else:print('error')
        elif a=='2':
            while 1:
                f=int(input('1:back，2:continue'))
                if f==1:
                    print(" Good bye!")
                    break
                elif f==2:
                    year= int(float(input('year:')))
                    month=int(float(input('mouth:')))
                    day = int(float(input('day:')))
                    def get_month_days(year, month):
                        if month >12 or month <= 0:
                            return -1
                        if month == 2:
                            return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
                        if month in (4, 6, 9, 11):
                            return 30
                        else:
                            return 31
                    print("This month {} days".format(get_month_days(year,month)))
                    months= (0,31,59,90,120,151,181,212,243,273,304,334)
                    if 0<month<=12:sum=months[month - 1]
                    else:print('error')
                    if 0<day<=31:pass
                    else:print('error')
                    sum+=day
                    leap=0
                    if year%4==0 or year%400==0:leap=1
                    if leap==1 and month>2:sum+=1
                    print ('the %d day'%sum)
                    leap=0
                else :print('error')
        elif a=='3':
            ea=input('Users:1:boss,2:user,3:worker,4:roadman:')
            while 1:
                f=input('1:back,2:continue')
                if f=='1':
                    print("Good bye!")
                    ea=input('Users:1:boss,2:user,3:worker,4:roadman:')
                elif f=='2':
                    if ea=='1':
                        x=input('Please log in and write your password here:')
                        while x!=num2:
                            print('Login failed, please try again')
                            f=input('1:back,2:continue')
                            if f=='1':
                                print("Good bye!")
                                ea=input('Users:1:boss,2:user,3:worker,4:roadman:')
                            elif f=='2':x=input('Please log in and write your password here:')
                            else:print('error')
                        print('boss,Hallo!')
                        boss=1
                        user=0
                        worker=0
                        roadman=0
                        break
                    if ea=='2':
                        print('user,Hallo')
                        boss=0
                        user=1
                        worker=0
                        roadman=0
                        break
                    elif ea=='3':
                        print('Ah,worker,Hallo')
                        boss=0
                        user=0
                        worker=1
                        roadman=0
                        break
                    elif ea=='4':
                        print('roadman,go to work!')
                        boss=0
                        user=0
                        worker=0
                        roadman=1
                        break
                    else:
                        print('error')
                        ea=input('Users:1:boss,2:user,3:worker,4:roadman:')
                else:print('error')
    
        elif a=='4':
            while 1:
                if boss!=1:
                    if roadman==1:print('※NO')
                    if worker==1:print('Get back to work')
                    if user==1:print("You Don't have enough access")
                f=int(input('1:back,2:continue'))
                if f==1:
                    print("Good bye!")
                    break
                elif f==2:
                    a=input('1:simple,2:up')
                    if a=='1':
                        while 1:
                            f=input('1:back,2:continue')
                            if f=='1':
                                print("Good bye!")
                                break
                            elif f=='2':print('404 Not Found')
                            else:print('error')
                    elif a=='2':
                        while 1:
                            if boss!=1:
                                if roadman==1:print('※NO')
                                if worker==1:print('Get back to work')
                                if user==1:print("You Don't have enough access")
                            f=int(input('1:back,2:continue'))
                            if f==1:
                                print("Good bye!")
                                break
                            elif f==2:print('404 Not Found')
                            else:print('error')
                else:print('error')
        elif a=='5':
            while 1:
                if boss!=1:
                    if roadman==1:print('※NO')
                    if worker==1:print('Get back to work')
                    if user==1:print("You Don't have enough access")
                f=int(input('1:back,2:continue'))
                if f==1:
                    print("Good bye!")
                    break
                elif f==2:
                    num10=input('boss,Please enter your original password:')
                    if num10!=num2:
                        print('Password error')
                        num10=input('boss,Please enter your original password:')
                    num2=input('Please enter a new password:')
                    xiugay(553717805371)
                    with open('.\ikun\\num2.txt','w') as f2:f2.write(num2)                    
                    print('boss~your new password is :{0}'.format(num2))
                else:print('error')
        else :
            print('error')
'''
以下是正文
'''
if __name__=='__main__':
    print("开始运行,wish haven't ERROR")
    with open('.\ikun\\upgread.txt','r') as fp:
        upgread=fp.readline()
    if upgread=='0':
        print()
        print('您是初次使用我们巨硬的产品 noodows (R才怪) {0}(内部版本 {1}) 无图像版'.format(version,build_version))
        print("You're use noodows (no R) {0}( {1} build) no Image by Bignesshard".format(version,build_version))
        print()
        print('设置语言')
        print('Setup language')
        while 1:
            lauguage=input('1:English,2:简体中文,3:繁體中文')
            if lauguage=='1':
                print('OK!')
                break
            elif lauguage=='2':
                print('OK!')
                break
            elif lauguage=='3':
                print('OK!')
            else:
                print('error')
        
        print('马上就好')
        print("It'll only take a second")
        with open('.\ikun\\lauguage.txt', "w", encoding="utf-8") as fp1:
            fp1.write(lauguage)
        upgread='1'
        with open('.\ikun\\upgread.txt', "w", encoding="utf-8") as fp1:
            fp1.write(upgread)
        print('欢迎使用')
        print('Thank you for your support!')
        with open('.\ikun\\lauguage.txt', "r", encoding="utf-8") as fpp1:
            lauguage=fpp1.readline()
        if lauguage=='1':
            US_allthing(1)
        elif lauguage=='2':
            CN_allthing(1)
        elif lauguage=='3':
            print('error')
        else :
            print('error')
    elif upgread=='1':
        with open('.\ikun\\lauguage.txt', "r", encoding="utf-8") as fpp1:
            lauguage=fpp1.readline()
        if lauguage=='1':
            print('Hallo!')
            US_allthing(1)
        elif lauguage=='2':
            print('你好')
            CN_allthing(1)
        elif lauguage=='3':
            print('你好')
            CN_fanti_allthing(1)
        else :
            print('error')
    else :
        print('error')
