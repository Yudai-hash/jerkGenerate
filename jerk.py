from numpy.ma.core import exp
#pyplotモジュールをインポートする
import matplotlib.pyplot as plt
#mathライブラリをインポート
import math
#Numpyライブラリのインポート
import numpy as np 

from scipy import integrate

import csv #コンマ区切り形式(CSV)ファイルの読み書きのためのモジュール

def originFunc(A,B,C,D,t,value):
  #print("len(t):",len(t))
  for i in range(0,len(t)):
    #print(i)
    if(0 <= t[i] and t[i] < B-D):
      value.append(A)
      #print(value)
    elif(B-D <= t[i] and t[i] <= 2*B):
      value.append(-A)
    elif(2*B <= t[i] and t[i] <= 3*B-D):
      value.append(A)
    elif(3*B-D <= t[i] and t[i] <= C):
      value.append(-A)
      #print(value)
    

A = 2 #縦軸の最大値と最小値の絶対値
B = 5 #BとDで加速と減速の比率を調整する
C = 5 #20(躍度一定(加速と減速の間隔が同じ))
D = 4.0 #0(躍度一定(加速と減速の間隔が同じ))
fontsize = 20 #グラフのフォント・ラベルサイズ
value = []
t = np.arange(0,C,0.01) #0.01 #0.05

#print("tの中身:",t)
#print("len(t):",len(t))
#print("")
originFunc(A,B,C,D,t,value)
#print("value",value)

#積分計算
integral_y = integrate.cumtrapz(value,t,initial = 0)
integral_integral_y = integrate.cumtrapz(integral_y,t,initial=0)
integral_integral_integral_y = integrate.cumtrapz(integral_integral_y,initial=0)

#figure()でグラフを表示する領域を作り，figというオブジェクトにする
fig = plt.figure(figsize = (22,11))
#add_subplot()でグラフを描画する領域を追加する
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.plot(t,value,label="Acceleration")
ax1.plot(t,integral_y,label="Velocity")
ax1.plot(t,integral_integral_y,label = "Angle")
ax2.plot(t,value,label="Jerk")
ax2.plot(t,integral_y,label="Acceleration")
ax2.plot(t,integral_integral_y,label = "Velocity")
ax2.plot(t,integral_integral_integral_y,label = "Angle")
#ax1.text(10,10,(B+D)/(B-D),fontsize = 15)
#ax2.text(10,10,"hoge")
ax1.set_title("When the absolute value of acceleration is constant",fontsize = 15) #グラフタイトル
ax2.set_title("When the absolute value of Jerk is constant",fontsize = 15) 
ax1.legend(loc="best",fontsize = fontsize) #凡例
ax2.legend(loc="best",fontsize = fontsize) 
#ax1.grid()
#ax2.grid()
ax1.set_xlabel("t",fontsize = fontsize) #軸ラベルの設定
ax2.set_xlabel("t",fontsize = fontsize) #軸ラベルの設定
#ax1.set_ylabel(r"$\frac{d^{2}\theta}{dt^{2}}$",fontsize = 20)
#ax2.set_ylabel(r"$\frac{d^{2}\theta}{dt^{2}}$",fontsize = 20)
ax1.set_xticks(np.arange(0,20),labelsize = fontsize)
ax2.set_xticks(np.arange(0,20))
ax1.set_xlim(0,C)
ax2.set_xlim(0,C)
ax1.tick_params(labelsize = 15)
ax2.tick_params(labelsize = 15)
ax1.set_ylim(-11,60)
ax2.set_ylim(-11,60)
plt.show()

try:
  print("加速:減速=1:",(B+D)/(B-D))
except ZeroDivisionError:
  print("You can not do this operation!")

#dはデータセット
#csvファイルを書き出すために，csv.writerオブジェクトの作成
#writerowメソッドなどを呼び出す
count = 0
ccount = 0
for i in range(0,len(np.round(integral_integral_integral_y))):
  if np.round(integral_integral_integral_y)[i] < 1000:
    #50 + 100
    count += 1
    ccount += 1
    if np.round(integral_integral_integral_y)[i] > 49.4:
      ccount += 1
  else:
    pass
print(count)
print("ccount",ccount)

with open('data20230305_acceleration.csv','w') as fo:
  #writer = csv.writer(fo)
  #for data in (np.round(integral_integral_integral_y,1))[0:count]:
     #writer.writerow(str(data))
  print(*np.round(integral_integral_integral_y,1)[0:count],sep='\n',file=fo)    
  
  
