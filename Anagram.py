
def anagram(input1, input2):
    input1 = input1.replace(" ","").lower()
    input2 = input2.replace(" ","").lower()
    if sorted(input1) == sorted(input2):
        return True
    else:
        return False


print(anagram("rat", "art"))
print(anagram("alert", "alter"))
print(anagram("Slot machines", "Cash lost in me"))
