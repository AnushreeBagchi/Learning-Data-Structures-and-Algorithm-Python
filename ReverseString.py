# Reverse the words in sentence
def word_flipper(our_string):
    inputList = our_string.split(" ")
    reverseList = []
    for word in inputList:
        reverse = ""
        for i in range(0, len(word)):
            reverse += word[len(word)-1-i]
        reverseList.append(reverse)
    reverseString =  " ".join(reverseList) 
    return reverseString
# print(word_flipper("This is one small step for ..."))
print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")
