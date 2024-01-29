
# def function(a:int) -> None:
#     a=5

# a=3;

# function(a); #This will be returning None as we can see from line 2
# print(a);



def function(a: list[int]) -> None:
    a.append(5)

a = [1,2,3,4]
function(a)
print(a);