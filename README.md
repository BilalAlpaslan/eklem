# eklem


bir veya birden fazla kelimeye baştan veya sondan ekleme yapan python scripti
bu script bilal alpaslan tarafından yapılmıştır



yardım metni:

argümanlar:
    
    [eklenecek yön] [eklenecek metin] [işlem yapılacak dosya] [oluşturulacak yeni dosya]
    [eklenecek yön] [eklenecek metin] [işlem yapılacak dosya]

    !eğer yazılacak dosya ismi verilmezse cevapCiktisi.txt varsayılan isimdir

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