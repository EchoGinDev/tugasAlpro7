def hapus_spasi_lebih(spasi):
    spasi = ' '.join(spasi.split())
    return spasi

x = hapus_spasi_lebih("saya tidak suka memancing ikan ")
print("Hasil:", x)


