
print("[1] Truk   - diskon 30%")
print("[2] Mobil  - diskon 50%")
print("[3] Motor  - diskon 60%")

pilihan = input("\nPilih kendaraan [1/2/3]: ")
tarif   = float(input("Tarif dasar (Rp): "))

if pilihan == "1":
    kendaraan, diskon = "Truk", 0.30
elif pilihan == "2":
    kendaraan, diskon = "Mobil", 0.50
elif pilihan == "3":
    kendaraan, diskon = "Motor", 0.60
else:
    print("Pilihan tidak valid!")
    exit()

hemat = tarif * diskon
bayar = tarif - hemat

print(f"\nKendaraan : {kendaraan}")
print(f"Tarif awal: Rp {tarif:,.0f}")
print(f"Hemat     : Rp {hemat:,.0f}")
print(f"Bayar     : Rp {bayar:,.0f}")
