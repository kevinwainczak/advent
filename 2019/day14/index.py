def process_reactions():
    reactions = dict()
    output_amounts = dict()
    file = open('input.txt', 'r')
    for line in file.readlines():
        line = line.split('=>')
        inputs = line[0]
        output = line[1].strip()
        output = output.split(' ')
        output_amounts[output[1].strip()] = int(output[0].strip())
        reaction_input = []
        inputs = inputs.split(',')
        for inp in inputs:
            inp = inp.strip().split(' ')
            reaction_input.append((int(inp[0].strip()), inp[1].strip()))
        reactions[output[1].strip()] = reaction_input
    return reactions, output_amounts

# inputs; list of form (quantity, item)
def all_ore(inputs):
    for entry in inputs:
        if inputs[entry] != 'ORE':
            return False
    return True

def reduce_inputs(inputs):
    input_dict = {}
    for entry in inputs:
        if entry[1] in input_dict:
            input_dict[entry[1]] += entry[0]
        else:
            input_dict[entry[1]] = entry[0]
    result = []
    for entry in input_dict:
        result.append((input_dict[entry], entry))
    return result

def challenge1():
    reactions, output_amounts = process_reactions()
    inputs = {'FUEL': 1}
    waste = {}
    while not all_ore(inputs):

        for entry in inputs:
            if entry == 'ORE':
                continue
        
            amount_needed = inputs[entry]
            needed_inputs = reactions[entry]
            amount_produced_from_reaction = output_amounts[entry]                
            
            multiplier = 1
            if amount_produced_from_reaction < amount_needed:
                multiplier = amount_needed / amount_produced_from_reaction

            for element in needed_inputs:
                if element[1] in inputs:
                    inputs[element[1]] += element[0] * multiplier
                else:
                    inputs[element[1]] = element[0] * multiplier
            amount_actually_produced = multiplier * amount_produced_from_reaction
            if amount_actually_produced > inputs[entry]


        print inputs
        new_inputs = []
        for entry in inputs:
            if entry[1] == 'ORE':
                new_inputs.append(entry)
                continue

            amount_needed = entry[0]
            needed_inputs = reactions[entry[1]]
            amount_produced_from_reaction = output_amounts[entry[1]]

            multiplier = 1
            if amount_produced_from_reaction < amount_needed:
                multiplier = amount_needed / amount_produced_from_reaction
            
            for element in needed_inputs:
                new_inputs.append((element[0] * multiplier, element[1]))
            new_inputs = reduce_inputs(new_inputs)
        inputs = list(new_inputs)
    print inputs
challenge1()