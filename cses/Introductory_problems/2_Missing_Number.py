n = int(input())
nums = list(map(int, input().split(' ')))
nums.sort()
for i in range(n):
    if n != nums[-1]:
        print(n)
        break
    if i+1 != nums[i]:
        print(i+1)
        break
