# def main():
#     with open('input.txt') as data:
#         valid = 0
#         present_fields = set()
#         required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
#         all_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
#         for line in data:
#             if line == '\n':
#                 if present_fields == required_fields or present_fields == all_fields:
#                     print present_fields
#                     valid += 1
#                 present_fields = set()
#             else:
#                 fields = line.strip().split(' ')
#                 for entry in fields:
#                     f = entry.split(':')
#                     present_fields.add(f[0])
#     return valid

def isValid(field, value):
    if field == 'byr':
        return 1920 <= int(value) and int(value) <= 2002
    elif field == 'iyr':
        return 2010 <= int(value) and int(value) <= 2020
    elif field == 'eyr':
        return 2020 <= int(value) and int(value) <= 2030
    elif field == 'hgt':
        val = value[:-2]
        metric = value[-2:]
        if metric == 'cm':
            return 150 <= int(val) and int(val) <= 193
        elif metric == 'in':
            return 59 <= int(val) and int(val) <= 76
        else:
            return False
    elif field == 'hcl':
        if value[0] != '#':
            return False
        values = set(value[1:])
        return values.issubset(set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']))
    elif field == 'ecl':
        return value in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    elif field == 'pid':
        if len(value) != 9:
            return False
        try:
            val = int(value)
        except:
            return False
        return True
    elif field == 'cid':
        return True
    return False

def main():
    with open('input.txt') as data:
        valid = 0
        present_fields = set()
        required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
        all_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
        for line in data:
            if line == '\n':
                if present_fields == required_fields or present_fields == all_fields:
                    print present_fields
                    valid += 1
                present_fields = set()
            else:
                # import pdb; pdb.set_trace()
                fields = line.strip().split(' ')
                for entry in fields:
                    f = entry.split(':')
                    if isValid(f[0], f[1]):
                        present_fields.add(f[0])
    return valid


print main()