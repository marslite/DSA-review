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

#Enumerate
names_in_order = ["Sam", "Bob", "Ann"];
for i,name in enumerate(names_in_order):
    print(i,name);




#Initializing 2D Array
N=10;
#The 0 is the number that will be used to intialize the 2d array
matrix = [ [0 for i in range(0,N)] for j in range(0,N) ]
print(matrix);

#Basic String Operations

s = 'abcdef'
print(s[4]);

# Substring extraction
print(s[1:4])

str_ = 'abcdefghij';
print(str_[1:8:2]);
#Here we are saying start from the first elemetn and stop at the last one, the step will be -2 each time.
print(str_[::-2]); #jhfdb

str1 = 'Good';
str2 = 'Morning';
str3 = 'Vietnam';
print(str1 + " " + str2 + " " + str3 + "!");

# Function to split the string by "_" and then printing the splitted_aray at index 2
def get_enzyme(ln):
    splitted = ln.split("_")
    enzyme_product = splitted[2]
    print(enzyme_product)


line = "lacZ_1013aa_betagalactosidase_escherichiacoli";
get_enzyme(line);

#Strings are Immutable

original_string = "hello";
modified_string = original_string.upper();

print(original_string);
print(modified_string);

#When using strings, we can join and split them to convert to and from lists
sentence_with_dashes = "The-fox-jumped-over-the-moon";
words = sentence_with_dashes.split('-');
print(words);

#The space_character will be the joining element between element of th elist into a string.
space_character = " "
sentence_with_spaces = space_character.join(words);
print(sentence_with_spaces);

#Sorting
random_list = [5,1,3,4,2]

# 'sorted' returns a new list
sorted_list = sorted(random_list);
print(sorted_list);
reverse_list = sorted(random_list, reverse= True);
print(reverse_list);

random_list.sort();
print(random_list);

#One can also sort lists with a custom key using lambda
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __repr__(self):
        return repr((self.name, self.age))

bob = Person("Bob", 14)
sam = Person("Sam", 12)
ann = Person("Ann", 16)

people = [bob,sam,ann];
people.sort(key=lambda x: x.name)
print(people, "Sorting by name")
people.sort(key=lambda x:x.age)
print(people, "Sorting by age");
