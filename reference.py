
##In this case this functon will change the variable x to 10
##This will only apply to the variable that calls the method not the original variable


def reassign_variable(x) -> int:
    return 10


my_var = 5
new_var = reassign_variable(my_var);
print(my_var)
print(new_var, "New Var");


## Pass by Value

def incrementByValue(x):
    x += 1
    return x;


y = 10;
new_num = incrementByValue(y)
print(new_num, "New num by incrementing by Passing Value");

print(y);

## Pass by Reference:
def increment(x):
    x[0] += 1

x = [10]
# increment(x)
print("Value before incrementing: ",x[0])
increment(x);
print("Value after incrementing: ", x[0])


