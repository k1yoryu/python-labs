tarif_minutes = 60
tarif_sms = 30
tarif_price = 24.99
gb_v_mb = 1024 #1gb=1024mb

minute_price = 0.89
sms_price = 0.59
mb_price = 0.79
nalog = 0.02

used_minutes = int(input("Введите количество израсходованных за месяц минут:"))
used_sms = int(input("Введите количество отправленных за месяц SMS:"))
used_internet = int(input("Введите объем использованного интернет-трафика (в МБ): "))

dopoln_minuti = used_minutes - tarif_minutes
dopoln_smski = used_sms - tarif_sms
dopoln_trafik = used_internet - tarif_price

if dopoln_minuti < 0:
    dopoln_minuti = 0
if dopoln_smski < 0:
    dopoln_smski = 0
if dopoln_trafik < 0:
    dopoln_trafik = 0

stoimost_minuti = dopoln_minuti * minute_price
stoimost_smski = dopoln_smski * sms_price
stoimost_trafik = dopoln_trafik * mb_price

itogo_bez_naloga = tarif_minutes + stoimost_minuti + stoimost_smski + stoimost_trafik

nalog = itogo_bez_naloga * nalog

itogo = itogo_bez_naloga + nalog

print("Счет за месяц:")
print("Базовая стоимость тарифа: {:.2f} руб.".format(tarif_price))

if dopoln_minuti > 0:
    print("Дополнительные минуты: {} мин. — {:.2f} руб.".format(dopoln_minuti, stoimost_minuti))
if dopoln_smski > 0:
    print("Дополнительные SMS: {} шт. — {:.2f} руб.".format(dopoln_smski, stoimost_smski))
if dopoln_trafik > 0:
    print("Дополнительный интернет: {} МБ — {:.2f} руб.".format(dopoln_trafik, stoimost_trafik))

print("Налог (2%): {:.2f} руб.".format(nalog))
print("Итоговая сумма к оплате: {:.2f} руб.".format(itogo))