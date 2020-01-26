input_list = [5, 10, 9, 8, 12, 1, 16, 6]
target = 16

def pair_sum_array(input_list, target): #complexity O(n2)
    for first in range(len(input_list)):
        for second in range(first+1, len(input_list)):
            sum = input_list[first] + input_list[second]
            if sum == target:
                return (first , second)

def pair_sum_array_faster(input_list, target):
    input_dict = dict()
    for index, element in enumerate(input_list):
        input_dict[element] = index
        if target-element in input_dict:
            if input_dict[target-element] != index:
                return [input_dict[target-element], index]
print(pair_sum_array_faster(input_list, target))