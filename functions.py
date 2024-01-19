
def square(x):
    return x*x




def foo(a):
    a = 3


a = 4
foo(a)
print(a);


def bar(a):
    a.append(2);
a = [1];
bar(a)
print(a);


listA = [0];
listB = listA;
listB.append(1);


print(listA);

print("#####")

print(max(min(4,5),max(6,7)));