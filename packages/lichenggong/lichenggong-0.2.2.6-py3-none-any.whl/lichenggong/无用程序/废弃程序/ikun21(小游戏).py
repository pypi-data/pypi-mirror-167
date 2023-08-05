
boss=1
while 1:
    if boss!=1:
        if roadman==1:print('※你无权访问,你越界了！')
        if worker==1:print('你有这个资格吗,去工作吧,请')
        else :print('你没有足够的权限')
    f=int(input('1:返回,2:继续'))
    if f==1:
        print("Good bye!")
        break
    elif f==2:
        while 1:
            print('boss好')
            print('1:对战 2:图鉴 3:不干了')
            a=input('what do you want to do ?')
            if a=='1':
                list2=[['灵魂诘问','神'],
                       ['冯@娟','神'],
                       ['校霸','神'],
                       ['圣人光环','神'],
                       ['直尺量角板','工具'],
                       ['直尺量角板','工具'],
                       ['三角板们','工具'],
                       ['三角板们','工具'],
                       ['奋斗','心态'],
                       ['摆烂','心态'],
                       ['发烧','疾病'],
                       ['感冒','疾病'],
                       ['电摇小子','手牌'],
                       ['一线三等角','手牌'],
                       ['李华','手牌'],
                       ['华强的电动車','手牌'],
                       ['半角模型','手牌'],
                       ['圆周率','手牌'],
                       ['bilibili','环境'],
                       ['后排靠窗靠空调','神'],
                       ['天气好热','环境']]
                list3=[0,1]
                players=['大黄','舟舟']
                random.shuffle(list2)
                random.shuffle(list3)
                random.shuffle(players)
                player1='boss:李导'
                player2=players[0]
                mycard=[]
                computercard=[]
                print("积分数：{}".format(sincow))
                if sincow>=14:
                    print("注：正常双方 HP 4000,大师 HP 8000,赢不赢回合后结算",end="")
                    print("您好牛,特供 地狱模式 双方 99990HP ")
                    ppp=input("1:正常模式,2:大师模式,3:地狱模式")
                    sincos=1
                else:
                    print("注：正常双方 HP 4000,大师 HP 8000,赢不赢回合后结算")
                    ppp=input("1:正常模式,2:大师模式")
                    sincos=0
                while 1:
                    if ppp=='1':
                        print("OK 正常")
                        player1HP=4000
                        player2HP=4000
                        break
                    elif ppp=='2':
                        print("OK 大师")
                        player1HP=8000
                        player2HP=8000
                        break
                    elif ppp=="3":
                        if sincos==1:
                            print("OK 地狱")
                            player1HP=99990
                            player2HP=99990
                            break
                        else:
                            print("error")
                    else:
                        print("error")
                del ppp,sincos
                gc.collect()
                a=1
                while 1:
                    def Geipai_4pai_Give_Player1(qwe):
                        input("{}的时间,点Enter键继续".format(player1))
                        mycard1=list2[0]
                        mycard2=list2[1]
                        mycard3=list2[2]
                        mycard4=list2[3]
                        del list2[0],list2[1],list2[2],list2[3]
                        mycardnew=[mycard1,mycard2,mycard3,mycard4]
                        mycard.extend(mycardnew)
                        print(player1,'获得',mycardnew)
                        print(player1,'有',(" ".join(str(i) for i in mycard)))
                        print(player1,'有',len(mycard),'张牌')
                        print(player1,'的回合')
                        print(player1,'有',player1HP,"HP")
                        print(player2,'有',player2HP,"HP")
                        while 1:
                            for i in range(len(mycard) + 1):
                                if i==0:
                                    print("{},不出牌".format(i))
                                else:
                                    print("{},出{}".format(i,mycard[i - 1]))
                            The_pack=int(float(input("请选择：")))
                            if The_pack>=0:
                                if The_pack==0:
                                    print("OK,你不出牌")
                                    break
                                elif The_pack<=len(mycard):
                                    while 1:
                                        print("1:Yes,2:No")
                                        The_main=input("您确定要出这张牌：{}？".format(mycard[The_pack - 1]))
                                        if The_main=='1':
                                            print("OK,你不出{}".format(mycard[The_pack - 1]))
                                            break
                                        elif The_main=='2':
                                            print('OK,你出{}'.format(mycard[The_pack - 1]))
                                            pass#牌起效果
                                            del mycard[The_pack - 1]
                                        else:print('error')
                                else:print("error")    
                            else:print(error)
                    def Geipai_4pai_Give_Player2(qwe):
                        input("{}的时间,点Enter键继续".format(player2))
                        computercard1=list2[0]
                        computercard2=list2[1]
                        computercard3=list2[2]
                        computercard4=list2[3]
                        del list2[0],list2[1],list2[2],list2[3]
                        computercardnew=[computercard1,computercard2,computercard3,computercard4]
                        computercard.extend(computercardnew)
                        print(player2,'有',len(computercard),'张牌')
                        print(player2,'的回合')
                        print(player1,'有',player1HP,"HP")
                        print(player2,'有',player2HP,"HP")
                        while 1:
                            for The_pack in range(len(computercard) + 1):
                                if len(computercard)==0:
                                    print("{}不出牌".format(player2))
                                    break
                                else :
                                    print('OK,{}出{}'.format(player2,computercard[The_pack-1]))
                                    pass#牌起效果
                                    del computercard[The_pack-1]
                    def Geipai_1pai_Give_Player1(qwe):
                        input("{}的时间,点Enter键继续".format(player1))
                        if len(list2)==0:
                            print('{}无牌可用'.format(player1))
                        else:
                            mycard1=list2[0]
                            del list2[0]
                            mycardnew=[mycard1]
                            mycard.extend(mycardnew)
                            print(player1,'获得',mycardnew)
                            print(player1,'有',(" ".join(str(i) for i in mycard)))
                            print(player1,'有',len(mycard),'张牌')
                            print(player1,'的回合')
                            print(player1,'有',player1HP,"HP")
                            print(player2,'有',player2HP,"HP")
                            while 1:
                                for i in range(len(mycard) + 1):
                                    if i==0:
                                        print("{},不出牌".format(i))
                                    else:
                                        print("{},出{}".format(i,mycard[i - 1]))
                                The_pack=int(float(input("请选择：")))
                                if The_pack>=0:
                                    if The_pack==0:
                                        print("OK,你不出牌")
                                        break
                                    elif The_pack<=len(mycard):
                                        while 1:
                                            print("1:Yes,2:No")
                                            The_main=input("您确定要出这张牌：{}？".format(mycard[The_pack-1]))
                                            if The_main=='1':
                                                print("OK,你不出{}".format(mycard[The_pack-1]))
                                                break
                                            elif The_main=='2':
                                                print('OK,你出{}'.format(mycard[The_pack-1]))
                                                pass#牌起效果
                                                del mycard[The_pack-1]
                                            else:print('error')
                                    else:print("error")    
                                else:print(error)#player1出手
                    def Geipai_1pai_Give_Player2(qwe):
                        input("{}的时间,点Enter键继续".format(player2))
                        if len(list2)==0:
                            print('{}无牌可用'.format(player2))
                        else:
                            computercard1=list2[0]
                            del list2[0]
                            computercardnew=[computercard1]
                            computercard.extend(computercardnew)
                            print(player2,'有',len(computercard),'张牌')
                            print(player2,'的回合')
                            print(player1,'有',player1HP,"HP")
                            print(player2,'有',player2HP,"HP")
                            while 1:
                                for The_pack in range(len(computercard) + 1):
                                    if len(computercard)==0:
                                        print("{}不出牌".format(player2))
                                        break
                                    else :
                                        print('OK,{}出{}'.format(player2,computercard[The_pack-1]))
                                        pass#牌起效果
                                        del computercard[The_pack-1]#player2出手
                    if list3[0]==0:
                        if a==1:
                            a=a-1
                            Geipai_4pai_Give_Player1(1)
                            if player1HP <= 0:
                                if player2HP <= 0:
                                    print("平局")
                                else:
                                    print(player1,'输了')
                                    print(player2,'赢了')
                                    sincow-=1
                                    with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                    print("积分减1")
                                break
                            if player2HP <= 0:
                                print(player2,'输了')
                                print(player1,'赢了')
                                sincow+=1
                                with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                print("积分加1")
                                break

                            Geipai_4pai_Give_Player2(1)
                            
                            if player1HP <= 0:
                                if player2HP <= 0:
                                    print("平局")
                                else:
                                    print(player1,'输了')
                                    print(player2,'赢了')
                                    sincow-=1
                                    with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                    print("积分减1")
                                break
                            if player2HP <= 0:
                                print(player2,'输了')
                                print(player1,'赢了')
                                sincow+=1
                                with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                print("积分加1")
                                break

                        elif a==0:
                            Geipai_1pai_Give_Player1(1)
                            if player1HP <= 0:
                                if player2HP <= 0:
                                    print("平局")
                                else:
                                    print(player1,'输了')
                                    print(player2,'赢了')
                                    sincow-=1
                                    with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                    print("积分减1")
                                break
                            if player2HP <= 0:
                                print(player2,'输了')
                                print(player1,'赢了')
                                sincow+=1
                                with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                print("积分加1")
                                break

                            Geipai_1pai_Give_Player2(qwe)
                            if player1HP <= 0:
                                if player2HP <= 0:
                                    print("平局")
                                else:
                                    print(player1,'输了')
                                    print(player2,'赢了')
                                    sincow-=1
                                    with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                    print("积分减1")
                                break
                            if player2HP <= 0:
                                print(player2,'输了')
                                print(player1,'赢了')
                                sincow+=1
                                with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                print("积分加1")
                                break

                    else :
                        if a==1:
                            a=a-1
                            Geipai_4pai_Give_Player2(1)
                            if player1HP <= 0:
                                if player2HP <= 0:
                                    print("平局")
                                else:
                                    print(player1,'输了')
                                    print(player2,'赢了')
                                    sincow-=1
                                    with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                    print("积分减1")
                                break
                            if player2HP <= 0:
                                print(player2,'输了')
                                print(player1,'赢了')
                                sincow+=1
                                with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                print("积分加1")
                                break

                            Geipai_4pai_Give_Player1(qwe)
                            if player1HP <= 0:
                                if player2HP <= 0:
                                    print("平局")
                                else:
                                    print(player1,'输了')
                                    print(player2,'赢了')
                                    sincow-=1
                                    with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                    print("积分减1")
                                break
                            if player2HP <= 0:
                                print(player2,'输了')
                                print(player1,'赢了')
                                sincow+=1
                                with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                print("积分加1")
                                break

                        else:
                            Geipai_1pai_Give_Player2(1)
                            if player1HP <= 0:
                                if player2HP <= 0:
                                    print("平局")
                                else:
                                    print(player1,'输了')
                                    print(player2,'赢了')
                                    sincow-=1
                                    with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                    print("积分减1")
                                break
                            if player2HP <= 0:
                                print(player2,'输了')
                                print(player1,'赢了')
                                sincow+=1
                                with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                print("积分加1")
                                break

                            Geipai_1pai_Give_Player1(1)
                            if player1HP <= 0:
                                if player2HP <= 0:
                                    print("平局")
                                else:
                                    print(player1,'输了')
                                    print(player2,'赢了')
                                    sincow-=1
                                    with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                    print("积分减1")
                                break
                            if player2HP <= 0:
                                print(player2,'输了')
                                print(player1,'赢了')
                                sincow+=1
                                with open('.\ikun\\sincow.txt', "w", encoding="utf-8") as f111:f111.write(sincow)
                                print("积分加1")
                                break


                a114514=input('还打不打？ 1:yes 2:no')
                if a114514=='1':
                    print('ok')
                elif a114514=='2':
                    print('goodbye')
                    break
                else:
                    print("error")
            elif a=='2':
                tujian.tujian(1)
            elif a=='3':
                break
            else :print('error')
    else:print('error')
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
    elif f==2:
        pygame.init()
        screen=pygame.display.set_mode((800,700),0,32)
        missile=pygame.image.load('.\ikun\\rect1.png').convert_alpha()
        x1,y1=100,600
        velocity=800
        time=1/1000
        clock=pygame.time.Clock()
        old_angle=0
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key in offset:
                        offset[event.key]=3
                elif event.type==pygame.KEYUP:
                    if event.key in offset:
                        offset[event.key]=0
            clock.tick(24)
            x,y=pygame.mouse.get_pos()
            distance=sqrt(pow(x1-x,2)+pow(y1-y,2)) #两 点 距 离 公 式
            section=velocity * time
            sina=(y1-y)/distance
            cosa=(x-x1)/distance
            angle=atan2(y-y1,x-x1)
            x1,y1=(x1+section*cosa,y1-section*sina)
            d_angle = degrees(angle)
            A=(x1-missile.get_width(), y1-missile.get_height()/2)
            B=(a[0]+10,a[1]+5)
            screen.blit(missile, A)
            dis_angle=d_angle-old_angle
            old_angle=d_angle
            if B==(x,y):
                print('你寄了')
                pygame.quit()
                sys.exit()
    else:print('error')
while 1:
    if boss!=1:
        if roadman==1:print('※你無權訪問,你越界了！')
        if worker==1:print('你有這個資格嗎,滾去工作吧,請')
        else :print('你沒有足夠的權限')
    f=int(input('1:返回,2:繼續'))
    if f==1:
        print("Good bye!")
        break
    elif f==2:
        print('佩羅西來送死咯')
        print("遊戲後把窗口(無響應時)關掉")
        
        with open('.\ikun\\gread.txt','r') as f4:
            mi2=f4.readline()
            mi2=int(float(mi2))
        print("往期記錄：{}".format(mi2))
        # 正確10位長度的時間戳可精確到秒
        start=t.time()
        time_array_start=t.localtime(start)
        othtime_start=t.strftime("%Y-%m-%d %H:%M:%S",time_array_start)


        clock=pygame.time.Clock()
        tnndweishenmebuhe=120
        SCREEN=443
        offset={pygame.K_LEFT:0,pygame.K_RIGHT:0,pygame.K_UP:0,pygame.K_DOWN:0}
        pygame.init()
        screen = pygame.display.set_mode([SCREEN,SCREEN])
        pygame.display.set_caption('python window')
        background=pygame.image.load('.\ikun\\tnnd.jpg')
        airplane=pygame.image.load('.\ikun\\pei.png')
        peillllllll=pygame.image.load('.\ikun\\StartIcon.png')
        gameover=pygame.image.load('.\ikun\\t0.jpg')
        xiluo_pei=[0,443]
        while 1:
            a1=14
            peiluoxi=[xiluo_pei[0]+a1,xiluo_pei[1]+a1]
            clock.tick(tnndweishenmebuhe)
            screen.blit(background,(0,0))
            screen.blit(airplane,xiluo_pei)
            screen.blit(peillllllll,peiluoxi)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key in offset:
                        offset[event.key]=3
                elif event.type==pygame.KEYUP:
                    if event.key in offset:
                        offset[event.key]=0
            xingcheng_x=xiluo_pei[0]+offset[pygame.K_RIGHT]-offset[pygame.K_LEFT]
            xingcheng_y=xiluo_pei[1]+offset[pygame.K_DOWN]-offset[pygame.K_UP]
            if xingcheng_x<=0:
                xiluo_pei[0]=0
            elif xingcheng_x>=SCREEN-52:
                xiluo_pei[0]=SCREEN-52
            else:
                xiluo_pei[0]=xingcheng_x
            if xingcheng_y<0:
                xiluo_pei[1]=0
            elif xingcheng_y>=SCREEN-52:
                xiluo_pei[1]=SCREEN-52
            else:
                xiluo_pei[1]=xingcheng_y
            peiluox=[peiluoxi[0]+a1-2,peiluoxi[1]+a1-2]
            if peiluox==[345,26] or peiluox==[346,26]:
                screen.blit(gameover,(0,0))
                break
                    
        end = t.time()
        time_array_end=t.localtime(end)
        othtime_end = t.strftime("%Y-%m-%d %H:%M:%S",time_array_end)
        print(othtime_start,othtime_end)

        link_start = datetime.datetime.strptime(othtime_start, '%Y-%m-%d %H:%M:%S')
        link_end = datetime.datetime.strptime(othtime_end, '%Y-%m-%d %H:%M:%S')

        mi=round((link_end - link_start).seconds / 60, 2)
        mi=int(float(mi))
        mi=(mi)*60
        print('您用了',mi,'秒',sep='')
        print('您用了',(mi)/60,'分鐘',sep='')



        if mi <= mi2:
            print("您破紀錄了耶")
            mi=str(mi)
            with open('.\ikun\\gread.txt', "w", encoding="utf-8") as f3:f3.write(mi)
        else :
            print('您沒有破紀錄喲')

    else:print('error')
