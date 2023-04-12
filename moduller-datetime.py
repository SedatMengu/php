# import datetime

# tanım : tarih ve saat ile ilgili bilgileri aynı anda içinde barındıran bir modüldür.

# bu modülü 2 parça halince inceleyeceğiz.

# ilk parça date kısmı

from datetime import date

bugun = date.today()
print(bugun)                            # / 2023-04-12
print(type(bugun))                      # / <class 'datetime.date'>
print(bugun.day)                        # / 12
print(bugun.month)                      # / 4
print(bugun.year)                       # / 2023
print(bugun.strftime("%d:%m:%Y"))

gecmis_tarih=date(2020,10,22)
print(gecmis_tarih)                     # / 2020-10-22 bu tarihi başka şekillerde de yaabilirdik ancak bu yöntem ile date ile ilgili foksiyonları da çağırmış olduk.

gecen_zaman=bugun-gecmis_tarih
print(gecen_zaman)                      # / 902 days, 0:00:00
print(type(gecen_zaman))                # / <class 'datetime.timedelta'>

# time kısmına ait fonksiyonlar

# 1  - bugun.ctime() fonksiyonu           : 
# 2  - bugun.fromisocalendar() fonksiyonu :
# 3  - bugun.fromordinal() fonksiyonu     :
# 4  - bugun.fromisoformat() fonksiyonu   :
# 5  - bugun.fromtimestamp() fonksiyonu   :
# 6  - bugun.isocalendar() fonksiyonu     :
# 7  - bugun.isoweekday() fonksiyonu      :     # bugun haftanın kaçıncı günü olduğunu döner.( pazartesi 1 , salı 2 )
# 8  - bugun.replace() fonksiyonu         :
# 9  - bugun.strftime() fonksiyonu        :
# 10 - bugun.toordinal() fonksiyonu       :
# 11 - bugun.timetuple() fonksiyonu       :
# 12 - bugun.today() fonksiyonu           :
# 13 - bugun.toordinal() fonksiyonu       :
# 14 - bugun.weekday() fonksiyonu         :     # / bugun haftanın kaçıncı günü olduğunu döner. (pazartesi 0 , salı 1 )


# ikinci bölüm datetime

from datetime import datetime

suan = datetime.now()
print(suan.year)                        # / 2023 - şuanki yıl
print(suan.month)                       # / 4   - şuanki ay
print(suan.day)                         # / 12  -   şuanki gün
print(suan.fold)
print(suan.hour)                        # / 15  -   şuanki saat
print(suan.minute)                      # / 15  -   şuanki dakika
print(suan.second)                      # / 14  -   şuanki saniye
print(suan.tzinfo)                      # / None



# 1  - datetime.astimezone() fonksiyonu       : 
# 2  - datetime.combine() fonksiyonu          :
# 3  - datetime.ctime() fonksiyonu            :     # / parantez içinde bir ifade varsa 1 ocak 1970 tarihinin üstüne o kadar saniye ekler. Fri Jan  2 06:46:40 1970 , str döner
# 4  - datetime.date() fonksiyonu             :     # / datetime in sadece date kısmını almamız yarar.
# 5  - datetime.dst() fonksiyonu              :
# 6  - datetime.fromisoformat() fonksiyonu    :
# 7  - datetime.fromisocalendar() fonksiyonu  :
# 8  - datetime.fromordinal() fonksiyonu      :
# 9  - datetime.fromtimestamp() fonksiyonu    :
# 10 - datetime.isocalendar() fonksiyonu      :
# 11 - datetime.isoformat() fonksiyonu        :
# 12 - datetime.isoweekday() fonksiyonu       :
# 13 - datetime.mro() fonksiyonu              :  
# 14 - datetime.now() fonksiyonu              :     # / işlem yapıldığı andaki datetime ı verir. <class 'datetime.datetime'>
# 15 - datetime.replace() fonksiyonu          :
# 16 - datetime.strftime() fonksiyonu         :     # / datetime ı istediğimiz formatta çıktı almamıza yarar. 
# 17 - datetime.strptime() fonksiyonu         :
# 18 - datetime.time() fonksiyonu             :     # / datetime in sadece time kısmını almamıza yarar.
# 19 - datetime.timestamp() fonksiyonu        :
# 20 - datetime.timetuple() fonksiyonu        :
# 21 - datetime.timetz() fonksiyonu           :
# 22 - datetime.today() fonksiyonu            :
# 23 - datetime.toordinal() fonksiyonu        :
# 24 - datetime.tzname() fonksiyonu           :
# 25 - datetime.utcfromtimestamp() fonksiyonu :
# 26 - datetime.utcnow() fonksiyonu           :
# 27 - datetime.utcoffset() fonksiyonu        :
# 28 - datetime.utctimetuple() fonksiyonu     :
# 29 - datetime.weekday() fonksiyonu          :


from datetime import timedelta

# tanımı: zamandaki değişim

# Örnek : 7 gün sonra tarih ne olacak..

suan2 = datetime.now()
tdelta = timedelta(days=7,hours=12,weeks=2,minutes=15)

print(suan + tdelta)                                                                # / 2023-05-04 04:44:47.877267 (2 hafta 7 gün 12 saat 15 dakika sonraki datetime)

# timedelta fonksiyonları :

# 1- timedelta.mro() fonksiyonu            :
# 2 - timedelta.total_seconds() fonksiyonu : 
