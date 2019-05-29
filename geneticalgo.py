import random
import string

user_string = input("Enter in the string you want to be guessed :")
def random_string(u,a,b,c):

    for letters in u:
        a = a + random.choice(string.ascii_letters)
        b = b + random.choice(string.ascii_letters)
        c = c + random.choice(string.ascii_letters)

    String_array = [a,b,c]
    return String_array

def check_fitness(input_string,string1,string2,string3):
  first_fitness = 0
  second_fitness = 0
  third_fitness = 0
  first_tuple =  tuple(zip(input_string,string1))
  second_tuple = tuple(zip(input_string, string2))
  third_tuple =  tuple(zip(input_string, string3))
  print(first_tuple)
  count = 0
  for i in first_tuple:
      x , y = first_tuple[count]
      count = count +1
      print(x + " - " + y )
      if x == y:
          first_fitness += 1
          print("they're Equal")
      else:
          print("not equal")
  print(second_tuple)
  count = 0
  for i in second_tuple:
      x, y = second_tuple[count]
      count = count + 1
      print(x + " - " + y)
      if x == y:
          print("they're Equal")
          second_fitness += 1
      else:
          print("not equal")
  print(third_tuple)
  count = 0
  for i in third_tuple:
      x, y = third_tuple[count]
      count = count + 1
      print(x + " - " + y)
      if x == y:
          third_fitness += 1
          print("they're Equal")
      else:
          print("not equal")
  fitness_score = first_fitness + second_fitness + third_fitness
  if fitness_score < 1:
      main(user_string)
      print("------------------new attempt --------------------")



def main(user_string):

    random_string_one = ""
    random_string_two = ""
    random_string_three = ""

    string_array = random_string(user_string,random_string_one,random_string_two,random_string_three)
    random_string_one = string_array[0]
    random_string_two = string_array[1]
    random_string_three = string_array[2]
    check_fitness(user_string, random_string_one, random_string_two, random_string_three)

asdf
main(user_string)









