s = input('Enter the string : ')
c = 0
for i in range(0, len(s)):
    if s[i] in "aeiou":
        c += 1

print(f"Vowels in given string : {c}")