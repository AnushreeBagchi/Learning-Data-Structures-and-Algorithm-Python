def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.

    temp = in_list[0];
    
    for i, value in enumerate (in_list):
        if value > 0:
            temp = value;
            break;
    
            
    for i, value in enumerate (in_list):
        if(value < temp and value > 0):
            temp = value
    
    if temp > 0:
        return temp;
    else:
        return None

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-33.04, 48.83, 75.33, 39.82, 76.38, 98.41, 71.27, 67.84, -16.58]))

print(smallest_positive([-1,-2,-3]))