#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
boy=float(input("Lütfen boyunuzu metre cinsinden giriniz : "))
print(boy)
kilo=float(input("lütfen agirlik değerinizi giriniz : "))
print(kilo)
vki=(kilo/(boy*boy))
print("vücut kitle endeksiniz :",vki)



#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

güncelMaas = 0
maas = input("Maaş tutarınızı giriniz: ")
zam = input("Zam oranı giriniz: ")
güncelMaas = int(maas) + (int(maas)*int(zam)/100)
print("güncelMaas: ",güncelMaas)



#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

sayi1=float(input("Birinci sayıyı giriniz: "))
sayi2=float(input("İkinci sayıyı giriniz: "))
sayi3=float(input("Üçüncü sayıyı giriniz: "))

en_buyuk_sayi=max(sayi1, sayi2, sayi3)

print("En büyük sayı:", en_buyuk_sayi)

#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

#Alan= π*r²
#Çevre=2*π*r
pi = 3
r=int(input("Yarıçap giriniz: "))
cevre = 2*pi*r
alan = pi*r*r
print("Çevre: " ,cevre)
print("Alan: " ,alan)


#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
#github'a ekleme yapalım, linkleri paylaşalım lütfen 🙂

metin = input('Metni Girin : \n')
ters=metin[::-1]

print('Girilen metnin tersi = %s' % (ters))
if ters == metin: 
    print('Girilen metin palindrom')
else:
    print('Girilen metin palindrom değil.') 


