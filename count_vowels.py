a = "hello world"
count = 0 
for ch in a:
    if ch.lower() in "aeiou":
        count += 1

print("Number of Vowel:", count)

