print("ຍີນດີຕ້ອນຮັບສູ່ຮ້ານຫມາກໄມ້ BorHu")
#ເກັບຂໍ້ມູນສີນຄ້າ

apple_price = 1000

banana_price =2000

print("=== ຮ້ານຫມາກໄມ້BorHu ===")
print("1. apple =",apple_price)
print("2. banana =",banana_price)
#ເລືອກສີນຄ້າ
choice = input("ເລືອກສີນຄ້າ (1 ຫຼື 2):  ")
if choice == "1":
    product = "apple"
    price = apple_price
elif choice == "2":
    product = "banana"
    price = banana_price
else :
    print("ເລືອກສີນຄ້າບໍ່ຖືກຕ້ອງ!")
    exit()
#ຈຳນວນສີນຄ້າ
while True:
     
     try:
         qty = int(input(f"ຕ້ອງການຊື້ {product} ຈຳນວນເທົ່າໃດ:"))
         if qty <= 0:
            print("ຈຳນວນຕ້ອງຫຼາຍກວ່າ 0")
                continue
           break
        except:
            print("ກະລຸນາໃສ່ຈຳນວນເປັນຕົວເລກເທົ່ານັ້ນ!")
#ຄຳນວນລາຄາລວມ
total = price * qty

prince(\n==== ສະຫຼຸບ ====)
prince(f"ສີນຄ້າ: {product}")
prince(f"ຈຳນວນ: {qty}")
prince(f"ລາຄາລວມ: {total}ກີບ")
prince("=== ຂອບໃຈທີ່ໃຊ້ບໍລິການ ===")