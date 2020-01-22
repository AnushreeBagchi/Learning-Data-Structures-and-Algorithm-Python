def test_case(testcase):
    arr = testcase[0]
    solution = testcase[1]
    output = find_duplicate(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

def find_duplicate(arr):
    curr_sum = 0
    expected_sum = 0
    for num in arr:
        curr_sum += num
    for i in range(len(arr)-1):
        expected_sum += i
    return curr_sum - expected_sum

input_arr = [0,1,2,1,3,4,5]
out = 1
testcase = [input_arr, out]
test_case(testcase)

input_arr = [0,1,2,3,3,4,5]
out = 3
testcase = [input_arr, out]
test_case(testcase)