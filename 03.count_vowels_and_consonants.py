def count_vowels_consonants(s):
    vowels = "aeiou"
    vowel_count = 0
    consonants_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            consonants_count += 1

    return vowel_count, consonants_count

text = input("Enter a String: ").lower()
vowels, consonants = count_vowels_consonants(text)
print(f"Vowels : {vowels}")
print(f"consonants : {consonants}")
