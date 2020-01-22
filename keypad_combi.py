def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""

def keypad(num):
    if num <= 1:
        return ""
    elif 2 <= num <= 9:
        return get_characters(num)
    out = list()
    last_digit = num%10
    small = keypad(num//10)
    keypad_string =  get_characters(last_digit)
    for char in keypad_string:
        for item in small:
            new_item = item+char
            out.append(new_item)
    return out

print(keypad(232))