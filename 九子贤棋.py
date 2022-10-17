# copyright THU @xwz_code
# upload: 2022-9-21 by @yuandj
# -*- coding: UTF-8 -*-

import pygame,sys
import math
from pygame.locals import *
qzx={}
qzy={}
dot={}
cango=[]
jumpover={}
ept=[]
tmf=1
qz={1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1}
for i in range(250000):
    dot[i]=0
window = pygame.display.set_mode((430, 430))
pygame.display.set_caption("贤者九子棋")
pygame.draw.rect(window,(210,160,0),(0,0,430,430),0)
s=1
pygame.font.init()
font  =  pygame.font.SysFont('华文宋体',190)
def draw_dot_circle(y1,x1,rd,bh):
    global dot
    for i in range(1,430,1):
        for j in range(1,430,1):
            if math.sqrt((x1-j)*(x1-j)+(y1-i)*(y1-i))<rd+0.5:
                pygame.draw.ellipse(window,(210,160,0),(i,j,1,1),0)
                dot[i+j*500]=bh
def find_can_go(bh):
    global cango
    global jumpover
    cango=[]
    jumpover={}
    if bh==1 and qz[6]==1 and qz[7]==0:
        cango.append(7)
        jumpover[7]=6
    if bh==1 and qz[10]==1 and qz[9]==0:
        cango.append(9)
        jumpover[9]=10
    if bh==2 and qz[6]==1 and qz[10]==0:
        cango.append(10)
        jumpover[10]=6
    if bh==2 and qz[7]==1 and qz[8]==0:
        cango.append(8)
        jumpover[8]=7
    if bh==3 and qz[7]==1 and qz[6]==0:
        cango.append(6)
        jumpover[6]=7
    if bh==3 and qz[8]==1 and qz[9]==0:
        cango.append(9)
        jumpover[9]=8
    if bh==4 and qz[8]==1 and qz[7]==0:
        cango.append(7)
        jumpover[7]=8
    if bh==4 and qz[9]==1 and qz[10]==0:
        cango.append(10)
        jumpover[10]=9
    if bh==5 and qz[10]==1 and qz[6]==0:
        cango.append(6)
        jumpover[6]=10
    if bh==5 and qz[9]==1 and qz[8]==0:
        cango.append(8)
        jumpover[8]=9
    if bh==6 and qz[7]==1 and qz[3]==0:
        cango.append(3)
        jumpover[3]=7
    if bh==6 and qz[10]==1 and qz[5]==0:
        cango.append(5)
        jumpover[5]=10
    if bh==7 and qz[6]==1 and qz[1]==0:
        cango.append(1)
        jumpover[1]=6
    if bh==7 and qz[8]==1 and qz[4]==0:
        cango.append(4)
        jumpover[4]=8
    if bh==8 and qz[7]==1 and qz[2]==0:
        cango.append(2)
        jumpover[2]=7
    if bh==8 and qz[9]==1 and qz[5]==0:
        cango.append(5)
        jumpover[5]=9
    if bh==9 and qz[8]==1 and qz[3]==0:
        cango.append(3)
        jumpover[3]=8
    if bh==9 and qz[10]==1 and qz[1]==0:
        cango.append(1)
        jumpover[1]=10
    if bh==10 and qz[6]==1 and qz[2]==0:
        cango.append(2)
        jumpover[2]=6
    if bh==10 and qz[9]==1 and qz[4]==0:
        cango.append(4)
        jumpover[4]=9
def drc(x,y):
    global s
    draw_dot_circle(x-1,y-1,30,s)
    pygame.draw.ellipse(window,(0,0,0),(x-32,y-32,64,64),4)
    pygame.draw.ellipse(window,(240,240,160),(x-20,y,40,20),0)
    pygame.draw.ellipse(window,(255,255,175),(x-20,y,40,20),1)
    pygame.draw.rect(window,(240,240,160),(x-20,y-10,40,20),0)
    pygame.draw.ellipse(window,(240,240,160),(x-20,y-20,40,20),0)
    pygame.draw.ellipse(window,(255,255,175),(x-20,y-20,40,20),1)
    qzx[s]=x
    qzy[s]=y
    s=s+1
def gbqz(bh,c1,c2,c3):
    x=qzx[bh]
    y=qzy[bh]
    pygame.draw.ellipse(window,(c1,c2,c3),(x-20,y,40,20),0)
    pygame.draw.ellipse(window,(c1+15,c2+15,c3+15),(x-20,y,40,20),1)
    pygame.draw.rect(window,(c1,c2,c3),(x-20,y-10,40,20),0)
    pygame.draw.ellipse(window,(c1,c2,c3),(x-20,y-20,40,20),0)
    pygame.draw.ellipse(window,(c1+15,c2+15,c3+15),(x-20,y-20,40,20),1)
def dlet(bh):
    x=qzx[bh]
    y=qzy[bh]
    pygame.draw.ellipse(window,(0,0,0),(x-32,y-32,64,64),4)
    pygame.draw.ellipse(window,(210,160,0),(x-28,y-28,56,56),0)
    qz[bh]=0
def ds(x,y):
    xx={}
    yy={}
    pi2=2*3.1415926
    for i in range(1,6):
        x1=math.cos(i/5*pi2)*210+x
        y1=math.sin(i/5*pi2)*210+y
        xx[i]=430-x
        yy[i]=430-y
        x=x1
        y=y1
    pygame.draw.line(window,(0,0,0),(xx[1],yy[1]),(xx[3],yy[3]),4)
    pygame.draw.line(window,(0,0,0),(xx[5],yy[5]),(xx[3],yy[3]),4)
    pygame.draw.line(window,(0,0,0),(xx[5],yy[5]),(xx[2],yy[2]),4)
    pygame.draw.line(window,(0,0,0),(xx[2],yy[2]),(xx[4],yy[4]),4)
    pygame.draw.line(window,(0,0,0),(xx[4],yy[4]),(xx[1],yy[1]),4)
    for i in range(1,6):
        drc(xx[i],yy[i])
    v=math.tan(math.radians(18))
    t=(1+v*v)/(3-v*v)*180
    drc(215-t*math.cos(math.radians(18)),290-(57-t*math.sin(math.radians(18))))
    drc(215-t*math.cos(math.radians(54)),290-(57+t*math.sin(math.radians(54))))
    drc(215+t*math.cos(math.radians(54)),290-(57+t*math.sin(math.radians(54))))
    drc(215+t*math.cos(math.radians(18)),290-(57-t*math.sin(math.radians(18))))
    drc(215,290-57+t)
ds(320,57)
pygame.display.update()
pygame.display.flip()
xz=0
while True:
    (x1,y1)=pygame.mouse.get_pos()
    if tmf==1:
        for i in range(1,s):
            if qz[i]==1:
                if dot[y1*500+x1]==i:
                    gbqz(i,160,0,0)
                else:
                    gbqz(i,240,240,160)
    if tmf==2:
        for i in range(i,s):
            if qz[i]==0:
                pygame.draw.ellipse(window,(210,160,0),(qzx[i]-28,qzy[i]-28,56,56),0)
        for i in range(1,s):
            if qz[i]==1:
                if dot[y1*500+x1]==i:
                    gbqz(i,0,0,160)
                else:
                    gbqz(i,240,240,160)
        m=1
        for i in range(1,s):
            if qz[i]!=0:
                find_can_go(i)
                if cango!=ept:
                    m=0
        if m==1:
            for i in range(1,s):
                if qz[i]!=0:
                    gbqz(i,240,240,160)
            tmf=4
    if tmf==3:
        find_can_go(xz)
        for i in range(1,s):
            if qz[i]==0 and dot[y1*500+x1] in cango:
                if dot[y1*500+x1]==i:
                    pygame.draw.ellipse(window,(0,160,0),(qzx[i]-28,qzy[i]-28,56,56),0)
                else:
                    pygame.draw.ellipse(window,(210,160,0),(qzx[i]-28,qzy[i]-28,56,56),0)
            elif qz[i]==0:
                pygame.draw.ellipse(window,(210,160,0),(qzx[i]-28,qzy[i]-28,56,56),0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if tmf==1:
                if dot[y1*500+x1]!=0:
                    dlet(dot[y1*500+x1])
                    tmf=2
            elif tmf==2:
                if dot[y1*500+x1]!=0:
                    if qz[dot[y1*500+x1]]==1:
                        qz[dot[y1*500+x1]]=2
                        gbqz(dot[y1*500+x1],0,0,160)
                        xz=dot[y1*500+x1]
                        tmf=3
            elif tmf==3:
                find_can_go(xz)
                if dot[y1*500+x1] in cango:
                    dlet(xz)
                    dlet(jumpover[dot[y1*500+x1]])
                    pygame.draw.ellipse(window,(210,160,0),(qzx[dot[y1*500+x1]]-28,qzy[dot[y1*500+x1]]-28,56,56),0)
                    qz[dot[y1*500+x1]]=1
                    gbqz(dot[y1*500+x1],240,240,160)
                    xz=0
                    tmf=2
                else:
                    for i in range(1,s):
                        if qz[i]!=0:
                            pygame.draw.ellipse(window,(210,160,0),(qzx[i]-28,qzy[i]-28,56,56),0)
                    qz[xz]=1
                    xz=0
                    tmf=2
    if tmf==4:
        sl=0
        for i in range(1,s):
            if qz[i]!=0:
                sl=sl+1
        if sl==1:
            text='成功'
            text_sf  =  font.render(text,True,pygame.Color(255,0,0),None)
            window.blit(text_sf,(15,100))
        if sl!=1:
            text2='失败'
            text_sf  =  font.render(text2,True,pygame.Color(255,0,0),None)
            window.blit(text_sf,(15,100))
    pygame.display.update()
