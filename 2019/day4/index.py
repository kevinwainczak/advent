input = '265275-781584'
lo = 265275
hi = 781584

def valid_password(n):
    adjacency_seen = False
    last_seen = n % 10
    n /= 10
    while n > 0:
        curr = n % 10
        if curr == last_seen:
            adjacency_seen = True
        if curr > last_seen:
            return False
        last_seen = curr
        n /= 10
    return adjacency_seen

def challenge1():
    matches = 0
    for n in range(lo, hi):
        if valid_password(n):
            matches += 1
    return matches

print challenge1()

def valid_password2(n):
    num_array = [-1] * 6
    index = 5
    while n > 0:
        num_array[index] = n % 10
        index -= 1
        n /= 10

    last_seen = 10
    digits = dict()
    for i in reversed (num_array):
        if i > last_seen:
            return False
        if i in digits:
            digits[i] += 1
        else:
            digits[i] = 1
        last_seen = i
    
    two_groups = 0
    larger_groups = 0
    for num in digits:
        if digits[num] == 2:
            two_groups += 1
        if digits[num] > 2:
            larger_groups += 1
    return two_groups >= 1


    
    n /= 10
    while n > 0:
        curr = n % 10
        if curr == last_seen:
            adjacency_seen = True
        if curr > last_seen:
            return False
        last_seen = curr
        n /= 10
    return adjacency_seen

def challenge2():
    matches = 0
    for n in range(lo, hi):
        if valid_password2(n):
            matches += 1
    return matches

print challenge2()

