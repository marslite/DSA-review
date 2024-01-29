from __future__ import annotations

'''
Write a function that appends the numbers or a string from 1 to n, inclusive, using the following rules:
1. If the number is a multiple of 3 and 5, append "Fizz Buzz"
2. If the number is just a multiple of 5, append "Buzz"
3. If the number is just a multiple of 3, append "Fizz"
4. If the number is neither a multiple of 3 nor 5, append then number as a string
'''
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

    


'''
Write a function that, given a list of integers, return the largest value in the list.
'''
def max_integer(input_list: list[int]) -> int:
  max = 0
  for i in input_list:
    if i > max:
      max = i
  return max
  

'''
Write a function that, given a list of integers, return the index of the largest integer in the list. 
If there are duplicates, return the earliest index.
'''
def max_integer_index(input_list: list[int]) -> int:
  max = 0
  
  for i in input_list:
    if i > max:
      max = i

  return input_list.index(max);
  

'''
Write a function that, given a list of tuples in the form (Student Name, Score), returns 
a dictionary where the key is the Student Name and the value is the Score for that student.

If a Student Name appears multiple times, take the score from the tuple at the largest index.
'''
def tuples_to_dictionary(input_list: list[tuple[str, int]]) -> dict[str, int]:
  dicto = {}
  for name,score in input_list:
    if name in dicto:
      if score > dicto[name]:
        dicto[name] = score
    else:
      dicto[name] = score
  return dicto

'''
Write a function that, given a dictionary of the form Student Name: Score, returns a list of 
names of the students who got the highest score.
In the output, student names should be sorted alphabetically ascending. 
'''
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



'''
Write a function that, given a dictionary of the form Student Name: Score, returns a dictionary
of the form Score: Count. 
Suppose the input is { 'A': 100, 'B': 90, 'C': 90 }, then the output would be
{ 100: 1, 90: 2}
'''
def count_score_frequencies(input_dict: dict[str, int]) -> dict[int, int]:
  final_dict = {}
  for name, score in input_dict.items():
    if score in final_dict.keys():
      final_dict[score] += 1
    else:
      final_dict[score] = 1
  return final_dict

'''
Write a function that, given a dictionary of the form Student Name: Score, returns the average score.
'''
def average_score(input_dict: dict[str, int]) -> float:
  avg = 0
  for name, score in input_dict.items():
    avg += score
  final_score = avg / len(input_dict.keys())
  return float(final_score)

'''
Write a function that, given a dictionary of the form Score: Count, returns the average score.
'''
def average_score_frequency_weighted(input_dict: dict[int, int]) -> float:
  avg = 0
  frq = 0
  for score, frequency in input_dict.items():
    avg += score * frequency
    frq += frequency
  final_score = avg / frq
  return float(final_score)


'''
Write a function that, given a dictionary of the form Student Name: Score, returns a dictionary
of letter grades. Here, A is 90 to 100 inclusive, B is 80 to 89 inclusive, C is 70 to 79 inclusive, and anything else is an F.
'''
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