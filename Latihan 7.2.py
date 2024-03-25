def hitung_kata(a,b):
    a_kecil = a.lower()
    hitung = a_kecil.count(b.lower())
    return hitung

a = input(str("masukkan kata: "))
k_dicari = "makan"
hitung = hitung_kata(a,k_dicari)

print("kata: ",k_dicari)
print("jumlah kata: ", hitung)

# Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan