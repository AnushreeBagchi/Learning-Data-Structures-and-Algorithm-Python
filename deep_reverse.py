def reverse(l):
    out = list()
    if len(l) == 0:
        return list()
    for index in range(len(l),0,-1 ):
        if isinstance(l[index-1], list):
            to_append = reverse(l[index-1])
        else:
            to_append = l[index-1]
        out.append(to_append)
    return out

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")

test_case = [[1,2,3], [3,2,1]]
test_function(test_case)

test_case = [[1, 2, [3, 4, 5], 4, 5], [5, 4, [5, 4, 3], 2, 1]]
test_function(test_case)

test_case = [[1, [2, 3, [4, [5, 6]]]], [[[[6, 5], 4], 3, 2], 1]]
test_function(test_case)

test_case = [ [1, [2,3], 4, [5,6]], [ [6,5], 4, [3, 2], 1]]
test_function(test_case)