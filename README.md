# Tower of Hanoi Menggunakan Algoritma Rekursif

**Nama:** A’isyah Putri Nur Afifah  
**NIM:** 20240801143  
**Program Studi:** Teknik Informatika  
**Mata Kuliah:** Game Development

## 1. Deskripsi Program

Program ini merupakan implementasi permainan Tower of Hanoi menggunakan bahasa pemrograman Python dengan algoritma rekursif. Program bertujuan untuk memindahkan tiga cakram dari tiang asal ke tiang tujuan dengan bantuan satu tiang lainnya.

## 2. Tujuan

- Memahami konsep algoritma rekursif.
- Mengetahui cara kerja pemindahan cakram pada Tower of Hanoi.
- Menghitung jumlah langkah minimum untuk menyelesaikan permainan.

## 3. Algoritma yang Digunakan

Algoritma yang digunakan adalah **algoritma rekursif (Recursive Algorithm)**, yaitu teknik pemrograman ketika sebuah fungsi memanggil dirinya sendiri untuk menyelesaikan masalah yang lebih kecil.

Pada program ini, fungsi `hanoi()` melakukan tiga tahapan:

1. Memindahkan `n-1` cakram dari tiang asal ke tiang bantuan.
2. Memindahkan cakram terbesar dari tiang asal ke tiang tujuan.
3. Memindahkan `n-1` cakram dari tiang bantuan ke tiang tujuan.

Ketika jumlah cakram adalah 1, program langsung mencetak pemindahan cakram. Kondisi ini disebut *base case* atau kondisi berhenti.

## 4. Kode Program

```python
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
```

## 5. Cara Menjalankan Program

1. Pastikan Python sudah terpasang di komputer.
2. Simpan kode program dengan nama `hanoi.py`.
3. Buka terminal pada folder tempat file disimpan.
4. Jalankan perintah berikut:

```bash
python hanoi.py
```

## 6. Hasil Output

```text
Langkah-langkah Tower of Hanoi:
A -> C
A -> B
C -> B
A -> C
B -> A
B -> C
A -> C
Total langkah: 7
```

Berdasarkan hasil output, program menampilkan urutan pemindahan cakram dari tiang A ke tiang C dengan bantuan tiang B. Jumlah pemindahan yang diperlukan adalah **7 langkah**.

## 7. Perhitungan Jumlah Langkah

Jumlah langkah minimum Tower of Hanoi dapat dihitung menggunakan rumus:

**T(n) = 2ⁿ − 1**

Keterangan:
- `T(n)` adalah jumlah langkah minimum.
- `n` adalah jumlah cakram.

Karena program menggunakan 3 cakram, perhitungannya adalah:

T(3) = 2³ − 1

T(3) = 8 − 1

**T(3) = 7 langkah**

Dengan demikian, diperlukan 7 langkah untuk memindahkan ketiga cakram ke tiang tujuan.

## 8. Kesimpulan

Program Tower of Hanoi ini menerapkan algoritma rekursif untuk menyelesaikan pemindahan cakram secara bertahap. Dengan menggunakan 3 cakram, program berhasil menampilkan urutan pemindahan dan menghitung total 7 langkah. Program ini membantu memahami konsep rekursi, kondisi berhenti, serta pemecahan masalah menjadi bagian-bagian yang lebih kecil.