

def f(n:int) -> bool:
    if n<0:
        return True
    if n<3:
        return n == 0
    return f(n-3) and f(n-6)


def question4(tuples: list[tuple[int,int]]) -> list[tuple[int,int]]:
    list = list.sort(key= lambda x:x[0]+ x*3[1])



def question5(tuples: list[tuple[int,int]]) -> list[tuple[int,int]]:
    list = list.sort(key= lambda x:(x[0],x[1]))



# def question6(input_list: list[int])-> list[int]:

    # solution = []
    # solution.append(list[0])

    # for i in range(len(input_list) -1):
    #     solution.append(input_list[i] * input_list[i+1])

    # if len(input_list) <= 1:

    

    # while(len(input_list) >= 1):
    #     for i in input_list:
    #         output *= i

    #     input_list.pop()
    #     solution.append(output)
    #     output = 1


        

    

    
    # solution = []
    # solution.append(input_list[0])

    # # input_list.pop(0)
    
    # for i in range(len(input_list)-1):
    #     result = input_list[i] + input_list[i+1]
    #     final = result + input_list[i+1]
    #     solution.append(final)

    
    # return question6(input_list[:len(input_list)-1]) + question6(input_list[])


def question13(input_strings: list[str]) -> dict[str,int]:
    freq = {}

    for i in input_strings:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return freq


# def f(n:int) ->int:
#     if n<=4:
#         return n
    
#     return f(n//2) + f(n//4) 



def g(n):
    if n == 0:
        return 0
    return g(n//2) + g(n//2) + n


# def f(m: int, n:int) -> int:
#     if min(m,n) <=1:
#         return 0
#     return f(m//2, n-1) * f(m-1,n//2) + m *n


def sort(arr):
    N = len(arr)
    for i in range(N):
        print("i=",i,"N",N,"i"  )

        for j in range(N-1,i,-1):
            # print("j=",j,"N-1",N-1,"i", i, "-1"  )
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
    return arr


def fs(n: int) -> int:
    if n <= 4:
        return n
    print("fs(",n, "/2",")","==", n//2, "fs(",n, "/4/",")=",n//4,"--> ==" ,n//2 + n//4   )
    return fs( n//2) + fs(n//4)

#f(): f(4) + (f2) = 6
#6 will be returned since our n is now lower than 4.


def fr(n:int) -> bool:
    if n<0:
        return True
    if n<3:
        return n == 0
    return fr(n-3) and fr(n-6)


def fd(m:int, n:int) -> int:
    if min(m,n) <= 1:
        return 0
    return fd(m//2, n-1) * fd(m-1, n//2) + m * n


# class A:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y



class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def f(self,x):
        return x*2
    
class B(A):
    def g(self,y):
        return self.f(y) + 4
    

##Coding Challenge
    
def question1(n: int) -> int:
    if n == 0:
        return 1
    return n *  question1(n-1)


def question2(n: int) -> int:
    if n <= 1:
        return 1
    
    return question2(n//2) + question2(n//2)

def question3(n: int) -> int:
    if n<=1:
        return 1
    
    return question3(n //2) + question3(n -1)


def question4(tuples: list[tuple[int,int]]) -> list[tuple[int,int]]:
    tuples = sort(key=lambda x:(x[0] + x[1]*3), reverse= True )
    return tuples

def question5(tuples: list[tuple[int,int]]) -> list[tuple[int,int]]:
    tuples = sort(key=lambda x:(-x[0], x[1]))
    return tuples


def question6(input_list: list[int]) -> list[int]:
    sums = 0
    res = []
    for i in input_list:
        sums += i
        res.append(sums)
    
    return res


def question7(input_list: list[int]) ->  list[int]:
    res = []
    sums = 1


    for num in input_list:
        temp = [i for i in input_list if i!= num]
        for c in temp:
            sums *= c
        res.append(sums)
        sums = 1
    
    return res




    
def question8(input_list: list[int], k:int) -> list[int]:
    result = []
    # sums = 0
    counter, index = k, 0

    # cutoff = len(input_list) - k

    for  i in range(0, len(input_list) -(k-1)):
        s = input_list[i:k + i]
        sums = sum(s)
        result.append(sums)
        # counter -= 1
        # sums = 0
        # index += 1


    return result


def question9(n:int) -> int:
    if n <= 2:
        return n
    else:
        return question9(n-2) +  question9(n-1)



# class Something:
#     def __init__(self, x:int, y:int) -> None:
#         self.x = x
#         self.y = y

#     def __lt__(self, other: Something):
#         return self.x > other.x
    
#     def getX(self):
#         return self.x
    
#     def getY(self):
#         return self.y
    
#     def setter(self,x,y):
#         self.x = x
#         self.y = y




    



if __name__ == "__main__":

    # print(f(33))
    # list = [1,2,3,4]
    # lstw = ['hello','hello','goodbye']
    # print(question13(lstw))
    # print(question6(list))
    # print(g(5))
    # my_string = 'good morning, world'
    # res = []
    # res.append(my_string.split())
    # res.append(my_string.split(','))
    # print(res)
    # arr = [100,28,31,120,31,35,93,15,23,59,55,47]
    # print(sort(arr))
    # l = [Something(1,2), Something(3,4), Something(5,6)]
    # l.sort()
    # some_list = ['a','b','c']
    # print(',,'.join(some_list))
    # print(fs(64))
    # print(fd(5,7))
    # a = A(1,2,3)
    # print(a)
    # b = B(2,3)
    # print(b.g(5))
    # first_input = [1,2,3,4,5,6]
    # print(question8(first_input,3))
    # print(question8(first_input,2))

    example1 = [1, 2, 3, 4, 5]

    # example2 = [-1,1,0,-3,3]
    # example3 = [-1,1,-1,1,-1]
    # example4 = [3,5]

    print(question8(example1,3));