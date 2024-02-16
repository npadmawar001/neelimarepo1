nums = []
for i in range(10):
    num = float(input("enter number {}: ".format(i+1)))
    nums.append(num)
smallest = min(nums)
largest = max(nums)
print(smallest)
print(largest)

