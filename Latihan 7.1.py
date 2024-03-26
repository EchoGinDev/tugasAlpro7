def anagram_kata(kata1, kata2):
    kata1_anagram = list(kata1.replace(" ", "").lower())
    kata2_anagram = list(kata2.replace(" ", "").lower())
    
    kata1_anagram.sort()
    kata2_anagram.sort()
    
    if kata1_anagram == kata2_anagram:
        return True
    else:
        return False

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

print(f"{kata1} {'anagram' if anagram_kata(kata1, kata2) else 'tidak anagram'} dengan kata {kata2}.")



