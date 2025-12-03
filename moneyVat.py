
# moneyVt.py
start_money= 200  #ເງິນຕັ້ງຕົ້ນ (ໂດລາ)
interest_rate = 0.02  #2% ຕໍ່ເດືອນ
months = 3  #ຈຳນວນເດືອນ

money = start_money

for i in range(months):
    money = money + (money * interest_rate)

print("ຍອດເງິນຫຼັງຈາກ 3 ເດືອນ =", round(money, 2),"ໂດລາ")