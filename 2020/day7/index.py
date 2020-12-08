def can_hold_shiny_gold_bag(bag, rules, hold_gold):
    if rules[bag] == []:
        return False
    for child_bag in rules[bag]:
        if child_bag == 'shiny gold' or child_bag in hold_gold:
            return True
        else:
            if can_hold_shiny_gold_bag(child_bag, rules, hold_gold):
                return True

def p1():
    with open('input.txt') as data:
        bag_rules = dict()
        gold_bags = set()
        for line in data:
            rule = line.split(' bags contain ')
            parent_bag = rule[0]
            is_terminal_bag = rule[1][:2] == 'no'
            child_bags = []
            if not is_terminal_bag:
                children = rule[1].strip().split(', ')
                for child in children:
                    amt = -4
                    if '.' in child:
                        amt -= 1
                    if '1' not in child:
                        amt -= 1
                    child = child[2:amt]
                    if child == 'shiny gold':
                        gold_bags.add(parent_bag)
                    child_bags += [child]
            bag_rules[parent_bag] = child_bags
        bags_that_hold_shiny_gold = 0
        non_gold_bags = set()
        for bag in bag_rules:
            if can_hold_shiny_gold_bag(bag, bag_rules, gold_bags):
                bags_that_hold_shiny_gold += 1
                gold_bags.add(bag)
            else:
                non_gold_bags.add(bag)
        return bags_that_hold_shiny_gold

def bag_cardinality(bag, rules):
    if rules[bag] == []:
        return 0
    
    size = 0
    for (child_bag, num) in rules[bag]:
        size += num
        size += num * bag_cardinality(child_bag, rules)
    return size

def p2():
    with open('input.txt') as data:
        bag_rules = dict()
        for line in data:
            rule = line.split(' bags contain ')
            parent_bag = rule[0]
            is_terminal_bag = rule[1][:2] == 'no'
            child_bags = []
            if not is_terminal_bag:
                children = rule[1].strip().split(', ')
                for child in children:
                    offset = -4
                    if '.' in child:
                        offset -= 1
                    if '1' not in child:
                        offset -= 1
                    amount = int(child[0])
                    child = child[2:offset]
                    child_bags += [(child, amount)]
            bag_rules[parent_bag] = child_bags
        num_bags = 0
        return bag_cardinality('shiny gold', bag_rules)


print p1()
print p2()