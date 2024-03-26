
def stringSort(s):
    #Runtime O(n log n)
    #Space O(n)
    sortedStr = sorted(s.replace(" ", ""))
    return "".join(sortedStr)

def stringSortCountsArr(s):
    #Alphabet: r
    #Runtime O(N + r)
    #Space O(N)

    alphabetSize = 26
    counts = [0] * alphabetSize
    for c in s.replace(" ",""):
        counts[ord(c) - ord('a')] += 1
    newStr = []
    for i,numLetters in enumerate(counts):
        newStr.append(chr(i + ord('a')) * numLetters)
    
    return "".join(newStr)

def stringStrongMultiPass(s):
    #alphabet size: r
    #Runtime: O(n*r)
    #Space: O(N)
    #As an array O(1)

    alphabetSize = 26
    s = list(s.replace(" ",""))
    swap_idx = 0
    for i in range(alphabetSize):
        curLetter = chr(i + ord('a'))
        for j,c in enumerate(s):
            if c == curLetter:
                s[swap_idx], s[j] = s[j], s[swap_idx]
                swap_idx += 1
    
    return "".join(s)






if __name__ == '__main__':
    #Alphabet of size 26 - aka constant, all low-caps


    s = 'the quick borwn fox jumps over the lazy dog'
    a = stringSort(s)
    b = stringSortCountsArr(s)
    c = stringStrongMultiPass(s)
    c += 'b'

    if a == b and b == c:
        print("True")
    else:
        print("False")

    # print(stringSort(s))
    # print(stringSortCountsArr(s))
    # print(stringStrongMultiPass(s))
