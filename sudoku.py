correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
# Define a function check_sudoku() here:
def check_sudoku(arr):
    for row in arr:
        check_list = list(range(1,len(arr)+1))
        for i in row:           
            if i in check_list:
                check_list.remove(i)
            elif i not in check_list:
                return False
    for  n in range(len(arr[0])):
        check_list = list(1,len(arr[0])+1)
        for row in arr       
print(check_sudoku(incorrect))
#>>> False

# print(check_sudoku(correct))
#>>> True

#print(check_sudoku(incorrect2))
#>>> False

#print(check_sudoku(incorrect3))
#>>> False

#print(check_sudoku(incorrect4))
#>>> False

#print(check_sudoku(incorrect5))
#>>> False

