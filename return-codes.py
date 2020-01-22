def get_alphabet(number):
    return chr(number+96)
def all_codes(number):
    if number == 0:
        return [""]
    
    #calculation of 2 right most digits
    reminder = number%100
    output_100 = list()
    if reminder <= 26 and number> 9:
        output_100 = all_codes(number//100)
        alphabet = get_alphabet(reminder)
        for index, elem in enumerate(output_100):
            output_100[index] = elem + alphabet
    
    #calculation of right most digit
    reminder = number%10
    output_10 = all_codes(number//10)
    alphabet = get_alphabet(reminder)
    for index,elem in enumerate(output_10):
        output_10[index] =  elem + alphabet

    output = list()
    output.extend(output_10)
    output.extend(output_100)

    return output

print(all_codes(1145))