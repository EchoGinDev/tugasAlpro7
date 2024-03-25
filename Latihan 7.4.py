# Buatlah suatu program mengetahui kata terpendek dan terpanjang dari suatu
# kalimat yang diinputkan! Misal: "red snakes and a black frog in the pool" Output: terpendek: a,
# terpanjang: snakes 

def longshortWord(kata):
    word = kata.split()
    terpendek = word[0]
    terpanjang = word[0]

    for j in word:
        if len(j) < len(terpendek):
            terpendek = j
        if len(j) > len(terpanjang):
            terpanjang = j 
    return terpendek, terpanjang

kata = input("Masukkan kalimat: ")

pendek, panjang = longshortWord(kata)

print(f"Kata terpendek: {pendek}")
print(f"Kata terpanjang: {panjang}")


    

