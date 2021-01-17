#!/usr/bin/env python 
#   
#   bir veya birden fazla kelimeye baştan veya sondan ekleme yapan python scripti
#
#   bu script bilal alpaslan tarafından yapılmıştır
#   https://github.com/BilalAlpaslan
#
import sys
args =sys.argv

yardim="""
# eklem

bir veya birden fazla kelimeye baştan veya sondan ekleme yapan python scripti
bu script bilal alpaslan tarafından yapılmıştır

yardım metni:

    argümanlar:
    
        [eklenecek yön] [eklenecek metin] [işlem yapılacak dosya] [oluşturulacak yeni dosya]
        [eklenecek yön] [eklenecek metin] [işlem yapılacak dosya]

        !eğer yazılacak dosya ismi verilmezse cevapCiktisi.txt varsayılan isimdir
        !eklenecek metinde boşluk gibi karakterleri kullanmak için metni tırnak işareti ile sarınız

    yön kullanımları:

        -f, -front  :bu kullanım ile yazılan metin her satırın sonuna eklenir
        -b, -back   :bu kullanım ile yazılan metin her satırın başına eklenir
        -h, -help   :yardım menüsünü açar

    eklenecek metin kullanımı:

        boşluk kullanmayın \n \t gibi ifadeler kullanabilirsiniz

    örnek kullanım:

        deneme.txt=[
            deneme
            deneme2
            deneme3
        ]
        python eklem.py -b * deneme.txt

        output cevapCiktisi.txt=[
            *deneme
            *deneme2
            *deneme3
        ]
    """

try:
    if(len(args)==5):
        secenek = args[1]
        eklenecekHarfler= args[2]
        dosya = args[3]
        yeniDosya = args[4]

        with open(str(dosya),"r+") as dosya:
            for satir in dosya.readlines():
                satir=satir[:-1]
                if satir!="":
                    if (secenek=="-f" or secenek=="-front"):
                        with open(str(yeniDosya),"a") as dosya:
                            dosya.write(satir+eklenecekHarfler+"\n")
                    if (secenek=="-b" or secenek=="-back"):
                        with open(str(yeniDosya),"a") as dosya:
                            dosya.write(eklenecekHarfler+satir+"\n")

    elif(len(args)==4):
        secenek = args[1]
        eklenecekHarfler= args[2]
        dosya = args[3]

        with open(str(dosya),"r+") as dosya:
            for satir in dosya.readlines():
                satir=satir[:-1]
                if satir!="":
                    if (secenek=="-f" or secenek=="-front"):
                        with open("cevapCiktisi.txt","a") as dosya:
                            dosya.write(satir+eklenecekHarfler+"\n")
                    if (secenek=="-b" or secenek=="-back"):
                        with open("cevapCiktisi.txt","a") as dosya:
                            dosya.write(eklenecekHarfler+satir+"\n")

    elif(len(args)==1):
        secenek = args[1]
        if (secenek=="-h" or secenek=="-help"):
            print(yardim)

except:
    print(yardim)
