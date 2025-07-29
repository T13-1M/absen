import os

os.system("cls")

def tambah():
    jumlah = int(input("Berapa jumlah siswa: "))

    for no in range(jumlah):
        nama = input(f"Masukkan nama siswa ke-{no+1}: ")
        print("\n")

        with open("30 day python challenge/day 20.txt", "a", encoding="utf-8") as f:
            f.write(f"{no+1}. {nama}\n")

        continue

def lihat():
    try:
        with open("30 day python challenge/day 20.txt", "r", encoding="utf-8") as f:
            data = f.read()
            if data:
                print("\nDaftar Murid:")
                print(data)
            else:
                print("\nBelum ada murid yang terdaftar.")
    except FileNotFoundError:
        print("\nFile daftar murid belum ada.")

def absen():
    try:
        with open("30 day python challenge/day 20.txt", "r", encoding="utf-8") as f:
            murid = f.readlines()
        if not murid:
            print("\nBelum ada murid yang terdaftar.")
            return
        print("\nDaftar Murid:")
        for line in murid:
            print(line.strip())
        nomor = int(input("Masukkan nomor murid yang absen: "))
        if 1 <= nomor <= len(murid):
            print(f"Murid {murid[nomor-1].strip()} sudah absen hari ini.")
        else:
            print("Nomor murid tidak ditemukan.")
    except FileNotFoundError:
        print("\nFile daftar murid belum ada.")


while True:
    pilih = input("""
1. Tambah murid
2. Lihat daftar murid
3. Absen murid
4. Keluar

Masukkan pilihan: """)

    if pilih == "1":
        tambah()
    elif pilih == "2":
        lihat()
    elif pilih == "3":
        absen()
    elif pilih == "4":
        print("Keluar . . .")
        break

    input("tekan enter untuk lanjut . . . . .")
    os.system("cls")