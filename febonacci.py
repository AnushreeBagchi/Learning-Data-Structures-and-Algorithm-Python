def febonacci_without_recurssion(num):
    s = [0,1]
    for index in range(num):
        l = len(s)
        prev1 = s[l-1]
        prev2 = s[l-2]
        s.append(prev1+prev2)
        print(s)
    

def febonacci_with_recussion1 (a,b,sum,num):
    if num == 0:
        return sum
    next = a+b
    sum += next
    total_sum = febonacci_with_recussion1(b,next,sum, num-1)
    return total_sum

def febonacci_with_recussion(a,b,num):
    next = a+b
    if num == 2:
        return a+b
    small = febonacci_with_recussion(b,next, num-1)+ a
    return small


print(febonacci_with_recussion(0,1,5))
