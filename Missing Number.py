nums = [0, 1, 2, 4, 5]
n = len(nums)
total = n * (n+1)//2
missing = total - sum(nums)

print("Missing number is:", missing)