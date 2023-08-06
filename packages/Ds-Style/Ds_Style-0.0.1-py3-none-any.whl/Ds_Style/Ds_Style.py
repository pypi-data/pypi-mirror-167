#######################################
import os
from time import sleep as timeout
import time
import sys
####################################
class Loading:

    def LD (Txt=str('Loading'),A='\033[1;37m┊',Start='\033[1;31m▊',End='\033[1;37m▒',B='\033[1;37m┊',Time=0.1,Repeat=40,TxtC='\033[1;37m'):
        for i in range(0,Repeat):
            i+=1
            cs=len (Txt)
            sv=Repeat+cs+1
            txt=End *sv
            f=i*Start
            print (txt+B,end='\r')
            print (TxtC+Txt+A+'{}'.format(f),end='\r')
            time.sleep(Time)

    def LD3(Txt='txt',Ds='=',A='[',Start=' ',End=' ',B=']',Number=10,Time=0.1,Repeat=4,TxtC='\033[1;37m'):
        for i in range (Repeat):
            for x in range (Number):
                x+=1
                cs=len (Txt)
                sv=Number+cs+3
                txt=End *sv
                f=x*Start
                ss=str(Ds)
                print (txt,B,end='\r')
                print (TxtC+Txt,A,'{}'.format(f)+ss,end='\r')
                time.sleep(Time)
############################################################
    def loading (Txt="Txt...",Time=0.1,Repeat=5):
        for x in range (Repeat):
            txt=Txt
            ss="|"
            sc="/"
            sd="-"
            sf="\\"
            time.sleep (Time)
            print (Txt+ss,end='\r')
            time.sleep (Time)
            print (Txt+sc,end='\r')
            time.sleep (Time)
            print (Txt+sd,end='\r')
            time.sleep (Time)
            print (Txt+sf,end='\r')
            time.sleep (Time)
########################################
    def counterup(Txt='Txt...',Number=10,Time=0.1,Txt2="% ",Repeat=5):
        for x in range (Repeat):
            for i in range (Number):
                i+=1
                time.sleep (Time)
                print (Txt,i,Txt2,end='\r')
                time.sleep (Time)

    def counterdown(Txt='Txt..',Number=10,Txt2='% ',Time=0.1,Repeat=1):
        txt=str(Txt)
        txt2=str(Txt2)
        for i in range (Repeat):
            for x in range (0,Number+1):
                ss=int(Number-x)
                timeout(Time)
                print (txt,ss,txt2,end='\r')
                time.sleep(Time)

###################################################
class Animation :

    def __init__(self,Txt=' Txt..'):
        self.Txt=Txt
    def SlowIndex (Animation,Time=0.001):
        txt=Animation.Txt
        for x in txt:
            time.sleep (Time)
            print (x,end='')

    def SlowText (Animation,Time=0.1):
        for chat in Animation.Txt:
            sys. stdout.write(chat)
            sys.stdout. flush ()
            time.sleep (Time)

    def Text_Line (Animation,Time=0.1,Repeat=1,CLT='\033[1;37m',CUL='\033[1;37m'):
        txt=Animation.Txt
        cs=len (txt)
        for n in range (Repeat):
            time.sleep (Time)
            print (CUL+txt[0].upper ()+CLT+txt[1::].lower(),end='\r')
            for x in range (0,cs):
                v=x+1
                time.sleep (Time)
                print (CLT+txt[0:x].lower()+CUL+txt[x].upper()+CLT+txt[v::].lower(),end='\r')
                time.sleep (Time)
                print (CLT+txt[0:x].lower()+CUL+txt[x].upper()+CLT+txt[v::].lower(),end='\r')
                time.sleep (Time)
            print (CLT+txt.lower(),end='\r')
            time.sleep (Time)
################################################
class Ds_Style:
    def __init__(self,*Txt):
       self.Txt=Txt
       for var in self.Txt:
           self.Txt=list(*Txt)

    def Style(Ds_Style,cols=2,Taps=0,Color='\033[1;31m',Space=0,Equal=False,TxtC='\033[1;37m',plus=''):

        if Equal == False:
            if cols==1:
               ss=len (Ds_Style.Txt)
               txt=Ds_Style.Txt
               taps=' '*Taps
               for x in range (0,ss):
                   ssv=len (txt[x])
                   sd1=str('─')*ssv ;sd2=str(" ")*ssv ;sd3=str('╭');sd4=str('╮');sd5=str ('╰');sd6=str('╯');sd7=str(Color+'│'+TxtC)
                   print (taps+Color+sd3+sd1+sd4);print (taps+Color+sd7+txt[x]+Color+sd7); print (taps+Color+sd5+sd1+sd6)
                   vip=str(plus)
                   if vip =='':
                       pass
                   else:
                       print (vip)
#######################################
        ## Equale == False
        ## cols == 2
        if Equal == False:
            if cols==2:
                ss=len (Ds_Style.Txt)
                bb=ss%2
                s7=ss-bb
                if bb%2==bb:
                    txt=Ds_Style.Txt
                    for x in range (0,s7,2):
                        mk=len(txt[x]);ssc=str('─')*mk;ssA=str(" ")*mk;ssB=str('╭');ssC=str('╮');ssD=str ('╰');ssE=str('╯')
                        sd=x+1;sr=len(txt[sd]);sd1=str('─')*sr;sd2=str(" ")*sr;sd3=str('╭');
                        sd4=str('╮');sd5=str ('╰');sd6=str('╯');sd7=str(Color+'│'+TxtC)
                        tap=' '*Space ; taps=' '*Taps
                        print (taps+Color+ssB+ssc+ssC+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[x]+Color+sd7+tap+sd7+txt[sd]+Color+sd7);print (taps+Color+ssD+ssc+ssE+tap+sd5+sd1+sd6)
                        vip=str(plus)
                        if vip =='':
                            pass
                        else:
                            print (vip)

                    for i in range(bb):
                        if bb==1:
                            lk=len (txt[-1]);sd1=str('─')*lk;sd2=str(" ")*lk;sd3 =str('╭');sd4=str('╮');sd5=str ('╰');sd6=str('╯');sd7=str(Color+'│'+TxtC)
                            print (taps+Color+sd3+sd1+sd4);print (taps+Color+sd7+txt[-1]+Color+sd7);print (taps+Color+sd5+sd1+sd6)
                        if bb==2:
                            lk=len (txt[-2]);sd1=str('─')*lk;sd2=str(" ")*lk;sd3 =str('╭');sd4=str('╮');sd5=str ('╰');sd6=str('╯');sd7=str(Color+'│'+TxtC)
                            tito=len (txt[-1]);ssc=str('─')*tito;ssA=str(" ")*tito;ssB=str('╭');ssC=str('╮');ssD=str ('╰');ssE=str('╯')
                            print (taps+Color+sd3+sd1+sd4+tap+ssB+ssc+ssC);print (taps+Color+sd7+txt[-2]+Color+sd7+tap+sd7+txt[-1]+Color+sd7);print (taps+Color+sd5+sd1+sd6+tap+ssD+ssc+ssE)
                            break
########################################
        ## cols =3 Equal=false
        if Equal == False:
            if cols==3:
                ss=len (Ds_Style.Txt)
                bb=ss%3
                s7=ss-bb
                if bb%3==bb:
                    txt=Ds_Style.Txt
                    for x in range (0,s7,3):
                        mk=len(txt[x]);ssc=str('─')*mk;ssA=str(" ")*mk;ssB=str('╭');ssC=str('╮');ssD=str ('╰');ssE=str('╯')
                        sd=x+1;sr=len(txt[sd]);sd1=str('─')*sr;sd2=str(" ")*sr;sd3=str('╭');
                        sd4=str('╮');sd5=str ('╰');sd6=str('╯');sd7=str(Color+'│'+TxtC)
                        sx=sd+1
                        sks=len(txt[sx]);
                        xz=str('─')*sks;xzz=str('╭');dxz=str('╮');
                        zza=str ('╰');zzx=str('╯')
                        taps=' '*Taps
                        tap=' '*Space
                        print (taps+Color+ssB+ssc+ssC+tap+sd3+sd1+sd4+tap+xzz+xz+dxz)
                        print (taps+Color+sd7+txt[x]+Color+sd7+tap+sd7+txt[sd]+Color+sd7+tap+sd7+txt[sx]+Color+sd7)
                        print (taps+Color+ssD+ssc+ssE+tap+sd5+sd1+sd6+tap+zza+xz+zzx)
                        vip=str(plus)
                        if vip =='':
                            pass
                        else:
                            print (vip)

                    for i in range(bb):
                        if bb==1:
                            lk=len (txt[-1]);sd1=str('─')*lk;sd2=str(" ")*lk;sd3 =str('╭');sd4=str('╮');sd5=str ('╰');sd6=str('╯');sd7=str(Color+'│'+TxtC)
                            print (taps+Color+sd3+sd1+sd4);print (taps+Color+sd7,txt[-1]+Color+sd7);print (taps+Color+sd5+sd1+sd6)
                        if bb==2:
                            lk=len (txt[-2]);sd1=str('─')*lk;sd2=str(" ")*lk;sd3 =str('╭');sd4=str('╮');sd5=str ('╰');sd6=str('╯');sd7=str(Color+'│'+TxtC)
                            tito=len (txt[-1]);ssc=str('─')*tito;ssA=str(" ")*tito;ssB=str('╭');ssC=str('╮');ssD=str ('╰');ssE=str('╯')
                            print (taps+Color+sd3+sd1+sd4+tap+ssB+ssc+ssC);print (taps+Color+sd7+txt[-2]+Color+sd7+tap+sd7+txt[-1]+Color+sd7);print (taps+Color+sd5+sd1+sd6+tap+ssD+ssc+ssE)
                            break
##########################################
        ## Equal == True
        ## Cols == 1
        if Equal ==True:
            if cols==1:
               max1=0 ;num=0
               txt=Ds_Style.Txt
               sv=len(txt)
               for x in range (0,sv):
                   num=len(txt[x])
                   if num > max1:
                      max1 = num
               ss=max1+2
               for n in range (0,sv):
                   vb=len(txt[n])
                   taps=' '*Taps
                   smm=ss-vb+vb
                   sd1=str('─')*ss ;sd3=str('╭');sd4=str('╮');sd5=str ('╰');sd6=str('╯');sd7=str(Color+'│'+TxtC)
                   print (taps+Color+sd3+sd1+sd4);print (taps+Color+sd7+txt[n].center(smm)+Color+sd7); print (taps+Color+sd5+sd1+sd6)
                   vip=str(plus)
                   if vip =='':
                       pass
                   else:
                       print (vip)

################################################
        ## Equale == True
        ## Cols == 2
        if Equal ==True:
            if cols ==2:
                ss=len (Ds_Style.Txt)
                bb=ss%2
                s7=ss-bb
                if bb%2==bb:
                    txt=Ds_Style.Txt
                    mm=len (Ds_Style.Txt)
                    max1=0 ;num=0
                    for n in range (0,mm):
                        num=len(txt[n])
                        if num > max1:
                            max1 = num
                    ss=max1+2
                    bg=max1
                    for x in range (0,s7,2):
                        mk=len(txt[x]);ssc=ss-mk+mk
                        sd=x+1;sr=len(txt[sd]);cv=ss-sr+sr
                        tap=' '*Space
                        taps=' '*Taps
                        sd1=str('─')*ss ;sd2=str(" ")*ss;sd3=str('╭');sd4=str('╮');sd5=str ('╰');sd6=str('╯');sd7=str(Color+'│'+TxtC)
                        print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[x].center(ssc)+Color+sd7+tap+sd7+txt[sd].center(cv)+Color+sd7);print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                        vip=str(plus)
                        if vip =='':
                            pass
                        else:
                            print (vip)

                    for i in range(bb):
                        if bb==1:
                            lk=len (txt[-1]);snc=ss-lk+lk
                            print (taps+Color+sd3+sd1+sd4);print (taps+Color+sd7+txt[-1].center(snc)+Color+sd7);
                            print (taps+Color+sd5+sd1+sd6)
                        if bb==2:
                            lk=len (txt[-2]);snc=ss-lk+lk
                            tito=len (txt[-1]);trg=ss-tito+tito
                            print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[-2].center(snc)+Colorsd7+tap+sd7,txt[-1].center(trg)+Color+sd7)
                            print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                            break

##############################################################
        ## Equale ==True
        ## Colos == 3 True
        if Equal ==True:
            if cols ==3:
                ss=len (Ds_Style.Txt)
                bb=ss%3
                s7=ss-bb
                if bb%3==bb:
                    txt=Ds_Style.Txt
                    mm=len (Ds_Style.Txt)
                    max1=0 ;num=0
                    for n in range (0,mm):
                        num=len(txt[n])
                        if num > max1:
                            max1 = num
                    ss=max1+2
                    for x in range (0,s7,3):
                        mk=len(txt[x]);ssc=ss-mk+mk
                        sd=x+1;sr=len(txt[sd]);cv=ss-sr+sr
                        ccz=x+2;vss=len (txt[ccz]);bhy=ss-vss+vss
                        tap=' '*Space
                        taps=' '*Taps
                        sd1=str('─')*ss ;sd2=str(" ")*ss ;sd3=str('╭');sd4=str('╮');sd5=str ('╰');sd6=str('╯');sd7=str(Color+'│'+TxtC)
                        print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[x].center(ssc)+Color+sd7+tap+sd7+txt[sd].center(cv)+Color+sd7+tap+sd7+txt[ccz].center(bhy)+Color+sd7);
                        print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                        vip=str(plus)
                        if vip =='':
                            pass
                        else:
                            print (vip)

                    for i in range(bb):
                        if bb==1:
                            lk=len (txt[-1]);snc=ss-lk+lk
                            print (taps+Color+sd3+sd1+sd4);print (taps+Color+sd7+txt[-1].center(snc)+Color+sd7);
                            print (taps+Color+sd5+sd1+sd6)

                        if bb==2:
                            lk=len (txt[-2]);snc=ss-lk+lk
                            tito=len (txt[-1]);trg=ss-tito+tito
                            print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[-2].center(snc)+Color+sd7+tap+sd7+txt[-1].center(trg)+Color+sd7);
                            print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                            break

############################################
    def Center (Ds_Style,cols=3,Taps=0,Color='\033[1;31m',Space=0,TxtC='\033[1;37m',plus=''):
        Equal=True
        taps=' '*Taps
        s=Ds_Style.Style
        if Equal ==True:
            if cols ==3:
                ss=len (Ds_Style.Txt)
                bb=ss%3
                s7=ss-bb
                if bb%3==bb:
                    txt=Ds_Style.Txt
                    mm=len (Ds_Style.Txt)
                    max1=0 ;num=0
                    for n in range (0,mm):
                        num=len(txt[n])
                        if num > max1:
                            max1 = num
                    ss=max1+2
                    for x in range (0,s7,3):
                        mk=len(txt[x]);ssc=ss-mk+mk
                        sd=x+1;sr=len(txt[sd]);cv=ss-sr+sr
                        ccz=x+2;vss=len (txt[ccz]);bhy=ss-vss+vss
                        tap=' '*Space
                        taps=' '*Taps
                        sd1=str('─')*ss ;sd2=str(" ")*ss ;sd3=str('╭');sd4=str('╮');sd5=str ('╰');sd6=str('╯');sd7=str(Color+'│'+TxtC)
                        print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[x].center(ssc)+Color+sd7+tap+sd7+txt[sd].center(cv)+Color+sd7+tap+sd7+txt[ccz].center(bhy)+Color+sd7);
                        print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                        vip=str(plus)
                        if vip =='':
                            pass
                        else:
                           print (vip)

                    for i in range(bb):
                        if bb==1:
                            lk=len (txt[-1]);snc=ss-lk+lk
                            k=len (txt[x]);l=len(txt[sd]);joo=len(txt[ccz])
                            pp=max1+4
                            jj=max1-pp
                            if l%3==1:
                                mm=' '*pp
                                print (taps+Color+mm+sd3+sd1+sd4);print (taps+Color+mm+sd7+txt[-1].center(snc)+Color+sd7);
                                print (taps+Color+mm+sd5+sd1+sd6)
                                vip=str(plus)

                            else:
                                mm=' '*pp
                                print (taps+Color+mm+sd3+sd1+sd4);print (taps+Color+mm+sd7,txt[-1].center(snc)+Color+sd7);
                                print (taps+Color+mm+sd5+sd1+sd6)

                        if bb==2:
                             lk=len (txt[-2]);snc=ss-lk+lk
                             tito=len (txt[-1]);trg=ss-tito+tito
                             print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[-2].center(snc)+Color+sd7+tap+sd7+txt[-1].center(trg)+Color+sd7);
                             print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                             break
########################################

             ## Equale == True
             ## Cols == 2
        if Equal ==True:
            if cols ==2:
                ss=len (Ds_Style.Txt)
                bb=ss%2
                s7=ss-bb
                if bb%2==bb:
                    txt=Ds_Style.Txt
                    mm=len (Ds_Style.Txt)
                    max1=0 ;num=0
                    for n in range (0,mm):
                        num=len(txt[n])
                        if num > max1:
                            max1 = num
                    hh=max1
                    if hh == hh:
                        ss=max1+2
                        for x in range (0,s7,2):
                            mk=len(txt[x]);ssc=ss-mk+mk
                            sd=x+1;sr=len(txt[sd]);cv=ss-sr+sr
                            tap=' '*Space
                            taps=' '*Taps
                            sd1=str('─')*ss ;sd2=str(" ")*ss ;sd3=str('╭');sd4=str('╮');sd5=str ('╰');sd6=str('╯');sd7=str(Color+'│'+TxtC)
                            print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[x].center(ssc)+Color+sd7+tap+sd7+txt[sd].center(cv)+Color+sd7);
                            print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                            vip=str(plus)
                            if vip =='':
                                pass
                            else:
                                print (vip)

                        for i in range(bb):
                            if bb==1:
                                lk=len (txt[-1]);snc=ss-lk+lk
                                k=len (txt[x]);l=len(txt[sd])
                                pp=max1//2
                                jj=max1-pp+3
                                mm=str(' ')*jj
                                print (taps+Color+mm+sd3+sd1+sd4);print (taps+Color+mm+sd7+txt[-1].center(snc)+Color+sd7);
                                print (taps+Color+mm+sd5+sd1+sd6)

                            if bb==2:
                                lk=len (txt[-2]);snc=ss-lk+lk
                                tito=len (txt[-1]);trg=ss-tito+tito
                                print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[-2].center(snc)+Color+sd7+tap+sd7+txt[-1].center (trg)+Color+sd7);
                                print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                                break
##########################################
class My_Style:

    def __init__(self,*Txt):
        self.Txt=Txt
        for x in Txt:
            self.Txt=list(*Txt)

    def Square(My_Style,cols=2,Color='\033[1;31m',TxtC='\033[1;37m',Taps=0,Space=0,Equal=True,Ds1='╭',
Ds2='─',Ds3='╮',Ds4='│',Ds5='╰',Ds6='╯',plus=''):

        if Equal == False:
            if cols==1:
                   ss=len (My_Style.Txt)
                   txt=My_Style.Txt
                   taps=' '*Taps
                   for x in range (0,ss):
                       ssv=len (txt[x])
                       sd1=str(Ds2)*ssv;sd3=str(Ds1);sd4=str(Ds3);sd5=str (Ds5);sd6=str(Ds6);sd7=str(Color+Ds4+TxtC)
                       print (taps+Color+sd3+sd1+sd4);print (taps+Color+sd7+txt[x]+Color+sd7); print (taps+Color+sd5+sd1+sd6)
                       vip=str(plus)
                       if vip =='':
                           pass
                       else:
                           print (vip)
###########################################
        ## Equale == False
        ## cols == 2
        if Equal == False:
            if cols==2:
                ss=len (My_Style.Txt)
                bb=ss%2
                s7=ss-bb
                if bb%2==bb:
                    txt=My_Style.Txt
                    for x in range (0,s7,2):
                        mk=len(txt[x]);ssc=str(Ds2)*mk;ssB=str(Ds1);ssC=str(Ds3);ssD=str (Ds5);ssE=str(Ds6)
                        sd=x+1;sr=len(txt[sd]);sd1=str(Ds2)*sr;sd3=str(Ds1);
                        sd4=str(Ds3);sd5=str (Ds5);sd6=str(Ds6);sd7=str(Color+Ds4+TxtC)
                        tap=' '*Space ; taps=' '*Taps
                        print (taps+Color+ssB+ssc+ssC+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[x]+Color+sd7+tap+sd7+txt[sd]+Color+sd7);print (taps+Color+ssD+ssc+ssE+tap+sd5+sd1+sd6)
                        vip=str(plus)
                        if vip =='':
                            pass
                        else:
                           print (vip)

                    for i in range(bb):
                        if bb==1:
                            lk=len (txt[-1]);sd1=str(Ds2)*lk;sd3 =str(Ds1);sd4=str(Ds3);sd5=str (Ds5);sd6=str(Ds6);sd7=str(Color+Ds4+TxtC)
                            print (taps+Color+sd3+sd1+sd4);print (taps+Color+sd7+txt[-1]+Color+sd7);print (taps+Color+sd5+sd1+sd6)
                        if bb==2:
                            lk=len (txt[-2]);sd1=str(Ds2)*lk;sd3 =str(Ds1);sd4=str(Ds3);sd5=str (Ds5);sd6=str(Ds6);sd7=str(Color+Ds4+TxtC)
                            tito=len (txt[-1]);ssc=str(Ds2)*tito;ssA=str(" ")*tito;ssB=str(Ds1);ssC=str(Ds3);ssD=str (Ds5);ssE=str(Ds6)
                            print (taps+Color+sd3+sd1+sd4+tap+ssB+ssc+ssC);print (taps+Color+sd7+txt[-2]+Color+sd7+tap+sd7+txt[-1]+Color+sd7);print (taps+Color+sd5+sd1+sd6+tap+ssD+ssc+ssE)
                            break
#########################################
        if Equal == False:
            if cols==3:
                ss=len (My_Style.Txt)
                bb=ss%3
                s7=ss-bb
                if bb%3==bb:
                    txt=My_Style.Txt
                    for x in range (0,s7,3):
                        mk=len(txt[x]);ssc=str(Ds2)*mk;ssA=str(" ")*mk;ssB=str(Ds1);ssC=str(Ds3);ssD=str (Ds5);ssE=str(Ds6)
                        sd=x+1;sr=len(txt[sd]);sd1=str(Ds2)*sr;sd2=str(" ")*sr;sd3=str(Ds1);
                        sd4=str(Ds3);sd5=str (Ds5);sd6=str(Ds6);sd7=str(Color+Ds4+TxtC)
                        sx=sd+1
                        sks=len(txt[sx]);
                        xz=str(Ds2)*sks;xzz=str(Ds1);dxz=str(Ds3);
                        zza=str (Ds5);zzx=str(Ds6)
                        taps=' '*Taps
                        tap=' '*Space
                        print (taps+Color+ssB+ssc+ssC+tap+sd3+sd1+sd4+tap+xzz+xz+dxz)
                        print (taps+Color+sd7+txt[x]+Color+sd7+tap+sd7+txt[sd]+Color+sd7+tap+sd7+txt[sx]+Color+sd7)
                        print (taps+Color+ssD+ssc+ssE+tap+sd5+sd1+sd6+tap+zza+xz+zzx)
                        vip=str(plus)
                        if vip =='':
                           pass
                        else:
                           print (vip)

                    for i in range(bb):
                        if bb==1:
                            lk=len (txt[-1]);sd1=str(Ds2)*lk;sd2=str(" ")*lk;sd3 =str(Ds1);sd4=str(Ds3);sd5=str (Ds5);sd6=str(Ds6);sd7=str(Color+Ds4+TxtC)
                            print (taps+Color+sd3+sd1+sd4);print (taps+Color+sd7+txt[-1]+Color+sd7);print (taps+Color+sd5+sd1+sd6)
                        if bb==2:
                            lk=len (txt[-2]);sd1=str(Ds2)*lk;sd2=str(" ")*lk;sd3 =str(Ds1);sd4=str(Ds3);sd5=str (Ds5);sd6=str(Ds6);sd7=str(Color+Ds4+TxtC)
                            tito=len (txt[-1]);ssc=str(Ds2)*tito;ssA=str(" ")*tito;ssB=str(Ds1);ssC=str(Ds3);ssD=str (Ds5);ssE=str(Ds6)
                            print (taps+Color+sd3+sd1+sd4+tap+ssB+ssc+ssC);print (taps+Color+sd7+txt[-2]+Color+sd7+tap+sd7+txt[-1]+Color+sd7);print (taps+Color+sd5+sd1+sd6+tap+ssD+ssc+ssE)
                            break
#########################################
        ## Equal == True
        ## Cols == 1
        if Equal ==True:
            if cols==1:
               max1=0 ;num=0
               txt=My_Style.Txt
               sv=len(txt)
               for x in range (0,sv):
                   num=len(txt[x])
                   if num > max1:
                      max1 = num
               ss=max1+2
               for n in range (0,sv):
                   vb=len(txt[n])
                   taps=' '*Taps
                   smm=ss-vb+vb
                   sd1=str(Ds2)*ss ;sd2=str(" ")*ss ;sd3=str(Ds1);sd4=str(Ds3);sd5=str (Ds5);sd6=str(Ds6);sd7=str(Color+Ds4+TxtC)
                   print (taps+Color+sd3+sd1+sd4);print (taps+Color+sd7+txt[n].center(smm)+Color+sd7);print (taps+Color+sd5+sd1+sd6)
                   vip=str(plus)
                   if vip =='':
                       pass
                   else:
                        pass
                        print (vip)

########################################
        ## Equale == True
        ## Cols == 2
        if Equal ==True:
            if cols ==2:
                ss=len (My_Style.Txt)
                bb=ss%2
                s7=ss-bb
                if bb%2==bb:
                    txt=My_Style.Txt
                    mm=len (My_Style.Txt)
                    max1=0 ;num=0
                    for n in range (0,mm):
                        num=len(txt[n])
                        if num > max1:
                            max1 = num
                    ss=max1+2
                    bg=max1
                    for x in range (0,s7,2):
                        mk=len(txt[x]);ssc=ss-mk+mk
                        sd=x+1;sr=len(txt[sd]);cv=ss-sr+sr
                        tap=' '*Space
                        taps=' '*Taps
                        sd1=str(Ds2)*ss ;sd2=str(" ")*ss;sd3=str(Ds1);sd4=str(Ds3);sd5=str (Ds5);sd6=str(Ds6);sd7=str(Color+Ds4+TxtC)
                        print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[x].center(ssc)+Color+sd7+tap+sd7+txt[sd].center(cv)+Color+sd7);print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                        vip=str(plus)
                        if vip =='':
                            pass
                        else:
                            print (vip)
                            pass
                    for i in range(bb):
                        if bb==1:
                            lk=len (txt[-1]);snc=ss-lk+lk
                            print (taps+Color+sd3+sd1+sd4);print (taps+Color+sd7+txt[-1].center(snc)+Color+sd7);
                            print (taps+Color+sd5+sd1+sd6)

                        if bb==2:
                            lk=len (txt[-2]);snc=ss-lk+lk
                            tito=len (txt[-1]);trg=ss-tito+tito
                            print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[-2].center(snc)+Color+sd7+tap+sd7+txt[-1].center(trg)+Color+sd7)
                            print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                            break
########################################
         ## Equale ==True
         ## Colos == 3 True
        if Equal ==True:
            if cols ==3:
                ss=len (My_Style.Txt)
                bb=ss%3
                s7=ss-bb
                if bb%3==bb:
                    txt=My_Style.Txt
                    mm=len (My_Style.Txt)
                    max1=0 ;num=0
                    for n in range (0,mm):
                        num=len(txt[n])
                        if num > max1:
                            max1 = num
                    ss=max1+2
                    for x in range (0,s7,3):
                        mk=len(txt[x]);ssc=ss-mk+mk
                        sd=x+1;sr=len(txt[sd]);cv=ss-sr+sr
                        ccz=x+2;vss=len (txt[ccz]);bhy=ss-vss+vss
                        tap=' '*Space
                        taps=' '*Taps
                        sd1=str(Ds2)*ss ;sd2=str(" ")*ss ;sd3=str(Ds1);sd4=str(Ds3);sd5=str (Ds5);sd6=str(Ds6);sd7=str(Color+Ds4+TxtC)
                        print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[x].center(ssc)+Color+sd7+tap+sd7+txt[sd].center (cv)+Color+sd7+tap+sd7+txt[ccz].center(bhy)+Color+sd7);
                        print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                        vip=str(plus)
                        if vip =='':
                            pass
                        else:
                            print (vip)
                            pass
                    for i in range(bb):
                        if bb==1:
                            lk=len (txt[-1]);snc=ss-lk+lk
                            print (taps+Color+sd3+sd1+sd4);print (taps+Color+sd7+txt[-1].center(snc)+Color+sd7);
                            print (taps+Color+sd5+sd1+sd6)

                        if bb==2:
                            lk=len (txt[-2]);snc=ss-lk+lk
                            tito=len (txt[-1]);trg=ss-tito+tito
                            print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[-2].center (snc)+Color+sd7+tap+sd7+txt[-1].center(trg)+Color+sd7);
                            print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                            break
#######################################
    # My_Style center
    def Center (My_Style,cols=3,Taps=0,Color='\033[1;31m',Space=0,TxtC='\033[1;37m',Ds1='╭',Ds2='─',Ds3='╮',Ds4='│',Ds5='╰',Ds6='╯',plus=''):
        Equal=True
        taps=' '*Taps
        s=My_Style.Txt
        if Equal ==True:
            if cols ==3:
                ss=len (My_Style.Txt)
                bb=ss%3
                s7=ss-bb
                if bb%3==bb:
                    txt=My_Style.Txt
                    mm=len (My_Style.Txt)
                    max1=0 ;num=0
                    for n in range (0,mm):
                        num=len(txt[n])
                        if num > max1:
                            max1 = num
                    ss=max1+2
                    for x in range (0,s7,3):
                        mk=len(txt[x]);ssc=ss-mk+mk
                        sd=x+1;sr=len(txt[sd]);cv=ss-sr+sr
                        ccz=x+2;vss=len (txt[ccz]);bhy=ss-vss+vss
                        tap=' '*Space
                        taps=' '*Taps
                        sd1=str(Ds2)*ss ;sd2=str(" ")*ss ;sd3=str(Ds1);sd4=str(Ds3);sd5=str(Ds5);sd6=str(Ds6);sd7=str(Color+Ds4+TxtC)
                        print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[x].center(ssc)+Color+sd7+tap+sd7+txt[sd].center (cv)+Color+sd7+tap+sd7+txt[ccz].center (bhy)+Color+sd7);
                        print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                        vip=str(plus)
                        if vip =='':
                            pass
                        else:
                           print (vip)

                    for i in range(bb):
                        if bb==1:
                            lk=len (txt[-1]);snc=ss-lk+lk
                            k=len (txt[x]);l=len(txt[sd]);joo=len(txt[ccz])
                            pp=max1+4
                            jj=max1-pp
                            if l%3==1:
                                mm=' '*pp
                                print (taps+Color+mm+sd3+sd1+sd4);print (taps+Color+mm+sd7+txt[-1].center(snc)+Color+sd7);
                                print (taps+Color+mm+sd5+sd1+sd6)

                            else:

                                mm=' '*pp
                                print (taps+Color+mm+sd3+sd1+sd4);print (taps+Color+mm+sd7+txt[-1].center(snc)+Color+sd7);
                                print (taps+Color+mm+sd5+sd1+sd6)

                        if bb==2:
                             lk=len (txt[-2]);snc=ss-lk+lk
                             tito=len (txt[-1]);trg=ss-tito+tito
                             print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[-2].center(snc)+Color+sd7+tap+sd7+txt[-1].center(trg)+Color+sd7);
                             print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                             break

             ## Equale == True
             ## Cols == 2
        if Equal ==True:
            if cols ==2:
                ss=len (My_Style.Txt)
                bb=ss%2
                s7=ss-bb
                if bb%2==bb:
                    txt=My_Style.Txt
                    mm=len (My_Style.Txt)
                    max1=0 ;num=0
                    for n in range (0,mm):
                        num=len(txt[n])
                        if num > max1:
                            max1 = num
                    hh=max1
                    if hh == hh:
                        ss=max1+2
                        for x in range (0,s7,2):
                            mk=len(txt[x]);ssc=ss-mk+mk
                            sd=x+1;sr=len(txt[sd]);cv=ss-sr+sr
                            tap=' '*Space
                            taps=' '*Taps
                            sd1=str(Ds2)*ss ;sd2=str(" ")*ss ;sd3=str(Ds1);sd4=str(Ds3);sd5=str (Ds5);sd6=str(Ds6);sd7=str(Color+Ds4+TxtC)
                            print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[x].center(ssc)+Color+sd7+tap+sd7+txt[sd].center(cv)+Color+sd7);
                            print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                            vip=str(plus)
                            if vip =='':
                                pass
                            else:
                                print (vip)

                        for i in range(bb):
                            if bb==1:
                                lk=len (txt[-1]);snc=ss-lk+lk
                                k=len (txt[x]);l=len(txt[sd])
                                pp=max1//2
                                jj=max1-pp+3
                                mm=str(' ')*jj
                                print (taps+Color+mm+sd3+sd1+sd4);print (taps+Color+mm+sd7+txt[-1].center(snc)+Color+sd7);
                                print (taps+Color+mm+sd5+sd1+sd6)
                            if bb==2:
                                lk=len (txt[-2]);snc=ss-lk+lk
                                tito=len (txt[-1]);trg=ss-tito+tito

                                print (taps+Color+sd3+sd1+sd4+tap+sd3+sd1+sd4);print (taps+Color+sd7+txt[-2].center(snc)+Color+sd7+tap+sd7+txt[-1].center (trg)+Color+sd7);
                                print (taps+Color+sd5+sd1+sd6+tap+sd5+sd1+sd6)
                                break

#########################################
# Dark_Storm #
#########################################
