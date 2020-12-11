def get_input():
    jolts = []
    with open('input.txt') as data:
        for line in data:
            jolts += [int(line.strip())]
    return jolts

def p1(jolts):
    jolts = [0] + sorted(jolts)
    ones = 0
    twos = 0
    threes = 1
    for i in range(len(jolts)-1):
        diff = jolts[i+1] - jolts[i]
        if diff == 1:
            ones += 1
        elif diff == 2:
            twos += 1
        elif diff == 3:
            threes += 1
    return (ones, threes, ones * threes)



def isValid(subset, lo, hi):
    for i in range(len(subset) + 1):
        if i == 0:
            if subset[i] - lo > 3:
                return False
        elif i == len(subset):
            if hi - subset[i-1] > 3:
                return False
        else:
            if subset[i] - subset[i-1] > 3:
                return False
    return True

def p2(jolts):
    jolts = sorted(jolts)
    seen = {}
    def get_subsets(jolts):
        if len(jolts) == 1:
            return 1
        if jolts[0] in seen:
            return seen[jolts[0]]
        all_subs = 0
        if len(jolts) > 1 and jolts[1] - jolts[0] <= 3:
            all_subs += get_subsets(jolts[1:]) #[[jolts[0]] + subset for subset in get_subsets(jolts[1:])]
        if len(jolts) > 2 and jolts[2] - jolts[0] <= 3:
            all_subs += get_subsets(jolts[2:]) #[[jolts[0]] + subset for subset in get_subsets(jolts[2:])]
        if len(jolts) > 3 and jolts[3] - jolts[0] <= 3:
            all_subs += get_subsets(jolts[3:]) #[[jolts[0]] + subset for subset in get_subsets(jolts[3:])]
        seen[jolts[0]] = all_subs
        return all_subs

    return get_subsets([0] + jolts)
    # return len(subsets)

# def p2(jolts):
#     jolts = sorted(jolts)
#     seen = {}
#     def get_subsets(jolts):
#         if len(jolts) == 1:
#             return [jolts]
#         if jolts[0] in seen:
#             return seen[jolts[0]]
#         all_subs = []
#         if len(jolts) > 1 and jolts[1] - jolts[0] <= 3:
#             all_subs += [[jolts[0]] + subset for subset in get_subsets(jolts[1:])]
#         if len(jolts) > 2 and jolts[2] - jolts[0] <= 3:
#             all_subs += [[jolts[0]] + subset for subset in get_subsets(jolts[2:])]
#         if len(jolts) > 3 and jolts[3] - jolts[0] <= 3:
#             all_subs += [[jolts[0]] + subset for subset in get_subsets(jolts[3:])]
#         seen[jolts[0]] = all_subs
#         return all_subs

#     subsets = get_subsets([0] + jolts)
#     return len(subsets)
    
# def p2(jolts):
#     jolts = sorted(jolts)
#     seen = {}
#     def get_subsets(base, rest):
#         if base in seen:
#             return seen[base]
#         subsets = []
#         for i in range(min(3, len(rest))):
#             if rest[i] - base <= 3:
#                 for subset in get_subsets(rest[i], rest[i:]):
#                     subsets += [[base] + subset]
#         seen[base] = subsets
#         return subsets
#     return len(get_subsets(0, jolts))

def main():
    jolts = get_input()
    print p1(jolts)
    # print get_subsets([1,2,3])
    print p2(jolts)

main()