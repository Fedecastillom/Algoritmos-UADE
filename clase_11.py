def count(nums):
    d = {}
    for x in nums:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for j, k in d.items():
        print(j, k)

def count2(nums):
    counted = []
    for i in range(len(nums)):
        if nums[i] not in counted:
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            print(f"{nums[i]}: {count}")
            counted.append(nums[i])

def common(list1, list2):
    ans = []
    for x in list1:
        if x in list2:
            ans.append(x)
    return ans

def prod(nums):
    res = 0
    for x in range(len(nums) - 1):
        res += nums[x] * nums[x + 1]
    return res
