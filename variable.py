# ism = "Sharifboy "
# familiya = "Olloyorov"
# ism_sharif = f"{ism}{familiya}"
# print(ism_sharif.capitalize())
#
# meva = "    olma    "
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Hello world")
# print('Hello \tworld')
# print('Hello \nworld')
#
# 1
# text = "Hello world"
# print(text)
#
# 2
# xabar = "Assalom alaykum"
# print(xabar)
#
# 3
# klass = "Hello world"
# print(klass)
#
# 4
# ism = input("Ismingiz nima?")
# print(ism.capitalize())
#
# car_0 = {'model': 'feraari', 'rangi': 'qizil'}
# print(car_0['model'])
# print(car_0['rangi'])
#
# talaba_0 = {'ism': 'murod olimov', 'yosh': 20, 't_yil': 2000}
# print(f"{talaba_0['ism'].title()}, {talaba_0['t_yil']}-yilda tug'ilgan, {talaba_0['yosh']} yoshda")
#
# talaba_0 = {'ism': 'murod olimov', 'yosh': 20, 't_yil': 2000}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-yilda tu'gilgan,\
#  {talaba_0['yosh']} yoshda")
#
# talaba_0['kurs'] = 4  # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
# talaba_0['fakultet'] = 'informatika'  # 'fakultet' ga esa 'informatika’
# print(talaba_0)
#
# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
#
# telefonlar = {
#     'ali': 'iphone x',
#     'vali': 'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310'
# }
# print(telefonlar)
#
# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")
#
# phone = telefonlar['hasan']
# print(f"Hasanning telefoni {phone}")
#
# phone = telefonlar.get('hasan', 'Bunday ism mavjud emas')
# print(phone)
#
# phone = telefonlar.get('hasan')
# print(phone)
#
# talaba_0 = {
#     'ism': 'jonibek',
#     'familiya': 'uralov',
#     'yosh': 22,
#     'fakultet': 'kompyuter injenering',
#     'kurs': 2
# }
#
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")
#
# print(talaba_0.items())
#
# telefonlar = {
#     'ali': 'iphone x',
#     'vali': 'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310'
# }
#
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni: {q}")
#
# mahsulotlar = {
#     'olma': 10000,
#     'anor': 20000,
#     'uzum': 30000,
#     'shaftoli': 23000,
# }
# print(mahsulotlar.keys())
#
# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
#
# bozorlik = ['olma', 'anor', 'uzum', 'baliq']
# for mahsulot in masulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {masulotlar[mahsulot]} so'm")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos do'koningizda {buyum} ham olib keling")
#
# telefonlar = {
#     'ali': 'iphone x',
#     'umar': 'iphone x',
#     'vali': 'galaxy s9',
#     'olim': 'mi 10 pro',
#     'zafar': 'mi 10 pro',
#     'orif': 'nokia 3310'
# }
#
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
# for tel in telefonlar.values():
#     print(tel)
#
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
# for tel in set(telefonlar.values()):
#     print(tel)
#
# print("""G'anisher dukondan "Python asoslari"
#  degan kitob oldi!
# Bu kitobda Python o'rganish
# mumkin.""")
#
# abc = 'Hello World'
# print(abc)
#
# xabar = "salom dunyo"
# print(xabar)
# xabar = "Hello world"
# print(xabar)
#
# klass = 212.32 * 21212.32
# print(klass)
#
# ism = input("Ismingizni kiriting: ").title()
# print(ism)
#
# son = int(input("Istalgan son kiriting: "))
# print(f"{son} ning kvadrati {son ** 2} ga teng\n{son} ning kubi {son ** 3} ga teng")
#
# yosh = int(input("Yoshingiz nechida?"))
# print(f"Siz {2023 - yosh} yilda tugilgan ekansiz")
#
# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# print(f"{son1 + son2}\n{son1 - son2}\n{son1 * son2}\n{son1 / son2}")
# a = son1 + son2
# b = son1 - son2
# c = son1 * son2
# d = son1 / son2
#
# print(f"{son1} + {son2} = {a} \n{son1} - {son2} = {b}\n{son1} * {son2} = {c}\n{son1} / {son2} = {d}")
