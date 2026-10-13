
def hanoi(n, asal, bantu, tujuan):
    if n == 1:
        print(asal, "->", tujuan)
    else:
        hanoi(n-1, asal, tujuan, bantu)
        print(asal, "->", tujuan)
        hanoi(n-1, bantu, asal, tujuan)

jumlah_cakram = 3

print("Langkah-langkah Tower of Hanoi:")
hanoi(jumlah_cakram, "A", "B", "C")

print("Total langkah:", 2**jumlah_cakram - 1)