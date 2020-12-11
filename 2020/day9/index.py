def get_input():
    nums = []
    with open('input.txt') as data:
        for line in data:
            nums += [int(line.strip())]
    return nums

def has_twosum(target, nums):
    nums = set(nums)
    for num in nums:
        if (target - num) in nums:
            return True
    return False

def p1(data, preamble):
    for i in range(preamble, len(data)):
        if not has_twosum(data[i], data[i-preamble:i]):
            return data[i]

def p2(data, invalid_num):
    data_sum = [data[0]]
    for i in range(1, len(data)):
        data_sum += [data_sum[i-1] + data[i]]
    data_sum = [0] + data_sum

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            range_sum = data_sum[j+1] - data_sum[i]
            if range_sum == invalid_num:
                return max(data[i:j+1]) + min(data[i:j+1])

def main():
    data = get_input()
    preamble = 25
    invalid_num = p1(data, preamble)
    print invalid_num
    print p2(data, invalid_num)

main()