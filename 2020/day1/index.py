def main():
    nums = []
    with open('input.txt') as data:
        for line in data:
            nums += [int(line.strip())]
    target = 2020
    # for a in nums:
    #     if (target - a) in nums:
    #         print a * (target-a)
    #         return
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                pass
            a = nums[i]
            b = nums[j]
            c = target - a - b
            if c > 0 and c in nums:
                print a * b * (target - a - b)
                return
main()