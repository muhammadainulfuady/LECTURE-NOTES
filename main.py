index = 1
temp = []
genap = 0
ganjil = 0
total = 0
user = int(input("Berapa angka yang ingin dimasukkan? "))
while index < user+1:
    user2 = int(input(f"Masukkan angka ke-{index} : "))
    temp.append(user2)
    index += 1

iterasi = 0
print("\nAngka-angka yang kamu masukkan:")
for i in temp:
    if i % 2 == 0:
        genap += 1
    else:
        ganjil += 1
    angka = i
    iterasi += 1
    total += i
    print(f"{iterasi}. {angka}")
rata_rata = total / user
print(f"\nTotal semua angka: {total}")
print(f"Rata-rata angka: {rata_rata}")
print(f"Jumlah angka genap: {genap}")
print(f"Jumlah angka ganjil: {ganjil}")