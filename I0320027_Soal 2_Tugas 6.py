banyak_data = int(input("Masukkan jumlah data: "))
a = []
jumlah = 0

for i in range(0 ,banyak_data):
    nilai = int(input("Masukkan data ke-%d: " % (i + 1)))
    a.append(nilai)
    jumlah = jumlah + nilai
    rata_rata = jumlah/banyak_data

print("Rata rata: ", format(rata_rata, '.2f'))



