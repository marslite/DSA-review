my_list = []; #Intializes Empty List
my_list.append(1);
print(my_list);

for i in range(0,6):
    #For each append it costs O(1)
    my_list.append(i);

print(my_list);

#Popping element from the front
last_element = my_list.pop();
print(last_element);
print(my_list);

#Constant time index accesses 
print(my_list[2]);

#Checking if an element is in a list in O(n) time.
#Notice the easy syntax
print(3 in my_list); #True
print(15 in my_list); #False

#Iterating over a list

total_sum = 0;
for i in my_list:
    total_sum += i;
print("Total sum is ", total_sum);



# It is possible to create a new list using an exisitng list with List Comprhension
string_numbers = [str(x) for x in my_list];
print(string_numbers);
#Using the same format to re-create a int (nums) list from the string_numbers list
back_to_nums = [int(x) for x in string_numbers];
print(back_to_nums);

even_nums = [x for x in my_list if (x %2) == 0]
print("Even Nums",even_nums);
odd_nums = [x for x in my_list if (x %2) == 1];
print("Odd Nums",odd_nums);

#Zip
names = ["Sam", "Bob", "Ann"];
ages = [10,8,13];
# By using ZIP it combines two parallel lists into a list of tuples
names_and_ages = zip(names,ages);
#Let's not forget to use list to list the lists of tuples
print(list(names_and_ages));



#Initializing 2D Array