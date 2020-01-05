def add_one(arr):
    output = 1
    for i in range(len(arr),0,-1):
        output = output + arr[i-1] 
        borrow = output//10
        if(borrow == 0):
            arr[i-1] = output
            break
        else:
            arr[i-1] = output%10
            output = borrow
    arr = [borrow] + arr
    index = 0
    while arr[index] == 0:
        index += 1
    return arr[index: ]
    
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")      

arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)