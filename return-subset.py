def subset(arr):
    output = [[]]
    window = 1
    while window < len(arr):
        window_start = 0
        while window_start < len(arr):
            counter = 1
            window_end = window_start+window
            while window_end + counter <= len(arr):
                to_append = []
                to_append.extend(arr[window_start:window_end])
                to_append.append(arr[window_end+counter-1])
                output.append(to_append)
                counter +=1
            window_start += 1
        window += 1    
    return output

def subset_with_recursion(arr):
    return return_subset_with_recursion(arr, 0)

def return_subset_with_recursion(arr, index):
    if index >= len(arr):
        return [[]]
    output = list()
    small_output = return_subset_with_recursion(arr, index+1)
    for element in small_output:
        output.append(element)
    for element in small_output:
        curr = list()
        curr.append(arr[index])
        curr.extend(element)
        output.append(curr)
    
    return output


print(subset_with_recursion([9,15,12]))