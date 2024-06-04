def isPalidrome(str) -> bool:
    print(str+  "==" + str[::-1])
    return str == str[::-1]

def palindromeCheck(str):
    new_s = ''
    for i in str:
        if i.isalnum():
            new_s += i
    
    return new_s.lower() == new_s[::-1].lower()











if __name__ == "__main__":
    print("Palindromes")
    print(palindromeCheck("madam"))
    print(palindromeCheck("anagram"))
    # isPalidrome("anagram")