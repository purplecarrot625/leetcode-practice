import itertools

def scaleBalancing(strArray):
    number2s = list(int(s) for s in strArray[0][1:-1].split(','))
    weights = list(int(s) for s in strArray[1][1:-1].split(','))

    # Add one weight
    for weight in weights:
        if number2s[0] + weight == number2s[1] or number2s[1] + weight == number2s[0]:
            return str(weight)
    
    # Add two weights
    for pair in itertools.combinations(weights, 2):
        if number2s[0] + pair[0] == number2s[1] + pair[1] or number2s[0] + pair[1] == number2s[1] + pair[0] or number2s[0] + pair[0] + pair[1] == number2s[1] or number2s[0] == number2s[1] + pair[0] + pair[1]:
            return "".join(str(min(pair))) +","+ str(max(pair))
    
    return "not possible"

print(scaleBalancing(["[13, 4]", "[1, 2, 3, 6, 14]"]))

