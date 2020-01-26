def staircase(num):
    if num<=0:
        return 
    if num ==1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    return staircase(num-1)+staircase(num-2)+staircase(num-3)

# caching the output to get faster implementation of the function
def staircase_with_hashmap(num):
    num_dict = dict({})
    return staircase_faster(num,num_dict)

def staircase_faster(num,num_dict ):
    if num<=0:
        return 
    if num ==1:
        output = 1
    elif num == 2:
        output = 2
    elif num == 3:
        output = 4
    else:
        if (num-1) in num_dict:
            n1 = num_dict[num-1]
        else:
            n1 = staircase(num-1)
        if (num-2) in num_dict:
            n2 = num_dict[num-2]
        else:
            n2 = staircase(num-2)
        if (num-3) in num_dict:
            n3 = num_dict[num-3]
        else:
            n3 = staircase(num-3)
        output = n1+n2+n3
    num_dict[num] = output
    return output
    


print(staircase_with_hashmap(3))
