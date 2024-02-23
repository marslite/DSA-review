
def fn_a(n: int) -> int:
    if n == 1:
        return n
    return fn_a(n -1) +1

#The function will be calling itself until n==1, in that case 1 will be returned.
#To walk us through it we can visualize the callstack for this function.
#Let n be 5
#f(5): fn_a(4) + 1 
#f(4): fn_a(3) + 1
#f(3): fn_a(2) + 1
#f(2): fn_a(1) + 1
#f(1): 1
# Now we unwind and return for each call back its value
#f(1): 1
#fn_a(2) = 1 + 1  = 2
#fn_a(3) = 2 + 1  = 3
#fn_a(4) = 3 + 1  = 4
#fn_a(5) = 4 + 1  = 5
# So in the end 5 is returned.
#The amount of call backs is totally dependend on n size. so O(n)
#Space complexity: O(1) since its contant the space for adding values at each call back.


  
# Code Block B
def fn_b(n: int) -> int:
  if n == 1:
    return n
  return fn_b(n - 1) + fn_b(n-1)
#The function will be calling for each call twice itself and then adding the two results together
#Let n be 5
#fn_b(5)= fn_b(5 -1 ) + fn_b(5-1) 
#fn_b(4)= fn_b(4 -1 ) + fn_b(4-1) 
#fn_b(3)= fn_b(3 -1 ) + fn_b(3-1) 
#fn_b(2) = fn_b(2 -1 ) + fn_b(2-1) 
#fn_b(1) = fn_b(1 -1 ) + fn_b(1-1) 

#fn_b(1)= retruns 1 (base case)
#fn_b(2)= fn_b(1) + fn_b(1) = 2
#fn_b(3)= fn_b(2) + fn_b(2) = 4
#fn_b(4)= fn_b(3) + fn_b(3) = 4 + 4 = 8
#fn_b(5)= fn_b(4) + fn_b(4) = 8 + 8 = 16
#The final result is 16. Since each call will have two more calls on the call stack untill we reach base 1.
# So if for every call we have two more then we have O(2^n-1) which reduced is O(2^n)



# Code Block C
def fn_c(n: int) -> int:
  if n == 1:
    return n
  return fn_c(n - 1) * n
#The function will be calling itself until n==1, in that case 1 will be returned.
#The function will be calculating the factorial number of n
#To walk us through it we can visualize the callstack for this function.
#Let n be 5
#f(5): fn_c(5 - 1) * 5  = 120
#f(4): fn_c(4 - 1) * 4 =  24
#f(3): fn_c(3 - 1) * 3  =   6
#f(2): fn_c(2 - 1) * 2  =  2
#f(1): 1 * 1 = 1

# Now we unwind and return for each call back its value
#fn_c(1) = returns n as base case (1)
#fn_c(2) = 1 * 2 = 2
#fn_c(3) = 2 * 3 = 6
#fn_c(4) = 6 * 4 = 20
#fn_c(5) = 24 * 5 = 120
#Runtime complexity: Since n-1 would be  multiplied to n-1 times untill we reach the base case we will tempted to say O(N-1 * N) but it won't be accurate
#The amound of times for fn_c to run will be dictated by the N times untill it reaches base case so O(n)



# Code Block D
#The function will be calling itself until n<=1, in that case 1 will be returned.
#The function will be adding the lenght of the n to count every time is recursively called
#Altough for each recursive, the function will be called two times (n^2) and the result for each will be added to count at the end
#To walk us through it we can visualize the callstack for this function.
#Let n be 5
#f(5): (count:10) + fn_d(2) + fn_d(2)
#f(2): (count:1) + 1 + 1
#f(0): 1
#Now we rewind back
#f(0) : return 1 which si the base case
#f(2): count:1 + 1 +1 = 3
#f(5): count:10 + 3 +3 = 16
#Runtime complexity: Since at each call the fn_d calls itself twice O(N^2) but then it gets sliced by half each time O(log n), however the for loop it will run for n, 
#So that's what finally matters for the sake of Runtime complexity which is O(log n) since it  gets halved, altough for the worst case scenario will be still depenedent how Big n is, so O(n) would be average/worst case scenario. However since each call will call the function twice 
#The final Runtime complexity would be O(n^2)
def fn_d(n: int) -> int:
  if n <= 1:
    return 1
  count = 0
  for x in range(n):
    count += x
  return fn_d(n//2) + fn_d(n // 2) + count





# Code Block E
#The function will be calling itself until n==0, in that case 1 will be returned.
#The function will be adding the lenght of the result of n //2 two times for each call
#To walk us through it we can visualize the callstack for this function.
#Let n be 5
# f(5): fn_e(2) + fn_e(2)
# f(2): fn_e(1) + fn_e(1)
# f(1):  fn_e(1) + fn_e(1)
# f(0):  fn_e(1) + fn_e(1)
#Now we rewind back
#f(0): 1 + 1 = 2
#f(1): 1 + 1 = 2
#f(2): 2 + 2 = 4
#f(5): 4 + 4 = 8
#Runtime complexity: Since fn_e would be calling itself twice the base will be 2^n, secondly the function at each call gets havled in half by reducing itself progressively
#untill it reaches base (0). So far the assumption is O(2^n) but since it halves in half at each call we might say O(log 2^n), but eventually in both the worst and average case scenario 
#the bulk of runtime complexity would be represented by how large n is, and since each call makes two calls we conclude that the runtime complexity for fn_e is  O(2^N)


def fn_e(n: int) ->int:
   if n == 0:
      return 1
   return fn_e(n // 2) + fn_e(n//2)



#Code Block F
#The function will be calling itself until n+1 < 0, in that case n would be returned, however this will lead to an inifite loop since the base case will never be reached
#The function will be calling itself twice at each call, for each call the result for the two functions calls will be added at each call and halved for each call
#To walk us through it we can visualize the callstack for this function.
#Let n be 5
# f(5): fn_f(2) + fn_f(2)
# f(2): fn_f(1) + fn_f(1)
# f(1): fn_f(0) + fn_f(0)
# f(0): fn_f(0) + fn_f(0)
# f(0): fn_f(0) + fn_f(0)
# ~ Ad infinitum
#Runtime complexity: The function will call itself twice at each call and it would keep on going ad infinitum, so: O(2^n)
def fn_f(n: int) -> int:
   if n + 1 < 0:
      return n
   return fn_f(n//2) + fn_f(n//2)


# Code Block G

def fn_g(n: int, m: int) -> int:
   if n <= 0 or m <= 0:
      return 1
   return fn_g(n//2, m) + fn_g(n ,m//2)



if __name__ == "__main__":

    # print(fn_a(5))
    print(fn_f(5))

