#1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

x = 1
y = 1

fibonacci = [x,y]
for i in range(20):
    x,y=y,x+y
    fibonacci.append(y)
print(fibonacci)


#2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

sayi = int(input("Bir sayı girişi yapiniz: "))
    
toplam = 0
for i in range(1,sayi):
        if(sayi%i ==0 ):
            toplam += i
if(sayi==toplam):
       print("Mükemmel sayi")
else:
       print("Mükemmel sayi değildir.") 


          



#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
       
birinciSayi = int(input("Birinci Sayiyi Giriniz : "))
ikinciSayi = int(input("İkinci Sayiyi Giriniz : "))
 
if (birinciSayi > ikinciSayi):
    kucuksayi = ikinciSayi
else:
    kucuksayi = birinciSayi
for i in range(1,kucuksayi+1):
    if (birinciSayi % i==0) and (ikinciSayi%i ==0):
        ebob = i
        ekok = (birinciSayi*ikinciSayi)//ebob

print ("EBOB:", ebob)
print ("EKOK:", ekok)



#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

sayi=int(input("Sayiyi Girin : "))
if sayi > 1:
   
   for i in range(2,sayi):
       if (sayi % i) == 0:
           print(sayi," Asal Sayi Değildir.")
           break
   else:
       print(sayi," Asal Sayidir.")
 
else:
   print(sayi," Asal Sayi Değildir.")
     


#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
   

sayi = int(input("Bir sayı girin: "))
bolen = 2
print(sayi, "sayısının asal çarpanları:")
while bolen <= sayi:   #veya for i in range(1,sayi):    
    if sayi % bolen == 0:
        print(bolen)
        sayi //= bolen
    else:
        bolen += 1
  