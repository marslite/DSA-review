
def basCounting(str):
    counts_dict = {}
    for chr in str:
        if chr not in counts_dict:
            counts_dict[chr] = 0
        counts_dict[chr] +=1
    return counts_dict


def countArr(str):
    count = [0] * 256
    for chr in str:
        chr_value = ord(chr)
        count[chr_value] += 1
    return count


def stringSort(str):
    sortedStr = sorted(str.replace(" ",""))
    return "".join(sortedStr)


def stringSortCount(string):
    counts = [0] * 26
    for c in string.replace(" ",""):
        counts[ord(c) - ord('a')] += 1
    newStr = []
    for i,numLetter in enumerate(counts):
        newStr.append(chr(i+ord('a'))*numLetter)
    
    return "".join(newStr)


    



if __name__ == "__main__":
    print("Basic  Counting")
    # print(basCounting("hello"))
    # print(countArr("hello"))
    s = "the quick brown fox jumps over the lazy dog"
    print(stringSort(s))
    print(stringSortCount(s))
