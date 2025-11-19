s = "leetcode"
freq = {}

# Step 1: counting frequency
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print("Current frequency:", freq)

# Step 2: find first non-repeating
result = -1
for ch in s:
    if freq[ch] == 1:
        result = ch
        break

print("First non-repeating character:", result)
