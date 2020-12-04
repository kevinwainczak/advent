# def isValid(least, most, letter, password):
#     appearances = 0
#     for i in range(len(password)):
#         if letter == password[i]:
#             appearances += 1
#     return appearances >= least and appearances <= most

def isValid(pos1, pos2, letter, password):
    return password[pos1-1] == letter and password[pos2-1] != letter or password[pos1-1] != letter and password[pos2-1] == letter

def main():
    with open('input.txt') as data:
        valid = 0
        for line in data.readlines():
            elems = line.strip().split(' ')
            nums = elems[0]
            letter = elems[1][0]
            password = elems[2]
            least = int(nums.split('-')[0])
            most = int(nums.split('-')[1])
            
            if isValid(least, most, letter, password):
                valid += 1
    return valid

print main()