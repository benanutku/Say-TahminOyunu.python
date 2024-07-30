import random

sayi = random.randint(1,10)
can=int(input('kaç kere tahmin hakkı istersiniz: '))
hak=can
sayac=0


while hak>0:
    hak-=1
    sayac+=1
    tahmin = int(input("1 ile 100 arasında tuttuğum sayıyı tahmin et: "))
    if (tahmin==sayi):
        print(f"Tebrikler tuttuğum sayıyı {sayac}.defada tahmin ettniz.Puananız:{100-(100/can)*(sayac-1)}")
        break
    elif sayi>tahmin :
     print('yukarı')
    else :
     print('aşağı') 
     
    if hak == 0 :
     print(f"hakkınız bitti. Tutulan sayı : {sayi}" )
     