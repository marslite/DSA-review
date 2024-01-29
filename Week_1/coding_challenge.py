
def fizz_buzz(n: int) -> list[str]:
  listO = []
  for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
      listO.append("Fizz Buzz")
    elif i % 5 == 0:
      listO.append("Buzz")
    elif i % 3 == 0:
      listO.append("Fizz")
    else:
      listO.append(str(i));
  return listO


fizzSol = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "Fizz Buzz"]
fizzBob = 15
print(fizz_buzz(15));


#Test

# fizzb = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "Fizz Buzz"]
fizz1 = 1;
fizz2 = 9;






    
def max_integer(input_list: list[int]) -> int:
  max = 0
  for i in input_list:
    if i > max:
      max = i
  return max
  

  
testMax = max_integer([5, 6, 8, 2, 7]);

print(testMax);







def max_integer_index(input_list: list[int]) -> int:
  max_i = 0
  max = 0

  for i in input_list:
    if i > max:
      max = i

  return input_list.index(max);
  




textIdx = [4, 6, 8, 2, 7];
test2 = max_integer_index(textIdx);
print(test2)

#Write a function that, given a list of tuples in the form (Student Name, Score), returns 
#a dictionary where the key is the Student Name and the value is the Score for that student.

#If a Student Name appears multiple times, take the score from the tuple at the largest index.

def tuples_to_dictionary(input_list: list[tuple[str, int]]) -> dict[str, int]:
  dicto = {}
  for name,score in input_list:
    if name in dicto:
      if score > dicto[name]:
        dicto[name] = score
    else:
      dicto[name] = score
  return dicto
  

made_so = tuples_to_dictionary([("Alice", 57), ("Bob", 62), ("Carl", 73)]);
made_so_again = tuples_to_dictionary([("Alice", 57), ("Bob", 62), ("Alice", 73)])
print(made_so);
print(made_so_again);





def highest_scoring_students(input_dict: dict[str, int]) -> list[int]:
  values = dict(sorted(input_dict.items(), key= lambda item:item[1], reverse=True))
  final_list = []
  max = 0
  for name, value in values.items():
    if value > max:
      max = value;
  
  for name, value in values.items():
    if value == max:
      final_list.append(name)

  return final_list;


text1 = {"Bob": 90,"Alice": 100, "Iger":1000, "Boson":10};
text2 = {"Alice": 100, "Bob": 100};


text3 = {"Alice": 100, "Bob": 90}
text4 = {"Alice": 100, "Bob": 100}

# print(highest_scoring_students(text1))
# print(highest_scoring_students(text2))
# print(highest_scoring_students(text3))
# print(highest_scoring_students(text4))





#   assert highest_scoring_students({"Alice": 100, "Bob": 90}) == ["Alice"]
    

#   assert highest_scoring_students({"Alice": 100, "Bob": 100}) == ["Alice", "Bob"]

  

def count_score_frequencies(input_dict: dict[str, int]) -> dict[int, int]:
  final_dict = {}
  for name, score in input_dict.items():
    if score in final_dict.keys():
      final_dict[score] += 1
    else:
      final_dict[score] = 1
  return final_dict

test_frequency = {"Alice": 100, "Bob": 90, "Carl": 90, "Jesse": 90};
print(count_score_frequencies(test_frequency));


def average_score(input_dict: dict[str, int]) -> float:
  avg = 0
  for name, score in input_dict.items():
    avg += score
  final_score = avg / len(input_dict.keys())
  return float(final_score)


      
test_avg = {"Alice": 100, "Bob": 90, "Carl": 90, "Dave": 90}

print(average_score(test_avg));



def average_score_frequency_weighted(input_dict: dict[int, int]) -> float:
  avg = 0
  frq = 0

  for score, frequency in input_dict.items():
    avg += score * frequency
    frq += frequency
  final_score = avg / frq
  return float(final_score)


test_weighted = {100: 1, 90: 3}
print(average_score_frequency_weighted(test_weighted));


def convert_to_gradebook(input_dict: dict[str, int]) -> dict[str, int]:
  finals = {"A":0, "B":0, "C":0, "F":0}
  for student, score in input_dict.items():
    if 90 <= score <= 100:
      finals["A"] += 1
    elif 80 <= score <= 89:
      finals["B"] += 1
    elif 70 <= score <= 79:
      finals["C"] +=1
    else:
      finals["F"] += 1
  return finals


test_convert = {"Alice": 100, "Bob": 89, "Carl": 79, "Dave": 60, "Eve": 50}

print(convert_to_gradebook(test_convert));
