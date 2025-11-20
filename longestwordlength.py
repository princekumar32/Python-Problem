words = "Hard work beats talent".split()
longest = ""

for w in words:
    if len(w) > len(longest):
        longest = w

print("Longest word:", longest)
print("Length:", len(longest))
