nums = [0, 1, 0, 3, 12]
new_list = []
zero_count = 0

for n in nums:
    if n == 0:
        zero_count += 1
    else:
        new_list.append(n)

for i in range(zero_count):
    new_list.append(0)

print(new_list)
