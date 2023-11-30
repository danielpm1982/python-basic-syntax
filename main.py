#This is a simple script that includes many of the basic syntax and functionalities of Python, structured into separate blocks of commented pieces of code (one block for each example). You can uncomment them, one at a time, for running the exemplified use case at a valid Python IDE - as PyCharm.#

# The content and examples of this script include:
# - input and output (print method)
# - strings and manipulating methods (including formatter)
# - data types and conversions
# - data structures (lists, dictionaries, sets, tuples) and methods
# - conditional statements (if, elif, else, continue, break, pass)
# - logical operators
# - recursiveness (for, while, range, enumerate)
# - custom functions and arg types (positionals, varargs, kwargs, defaults)
# - scope (global, local, nonlocal, in-built)
# - functional programming (map, filter, zip, reduce)
# - comprehensions (list comprehensions, set comprehensions, dict comprehension)

# inputs and outputs
# name = input("Please, type your name:")
# print("Hello World ! Welcome, "+name+" !")

# basic arithmetic operators
# var1 = 100
# var2 = 3
# print(var1+var2)
# print(var1-var2)
# print(var1*var2)
# print(var1/var2)

# exponentiation, floor division, modulo, type
# print(var1**var2)
# print(var1//var2)
# print(var1%var2)
# print(type(var1))
# print(type(var1/var2))

# other numerical operators... for more, import math module
# print(round(3.1))
# print(abs(-3.1))

# binaries, hexadecimals, decimals and complex numbers
# print(bin(5))
# print(int("0b101",2))
# print(hex(63))
# print(int("0x3f",16))
# print(complex(5+5j))

# booleans
# var_bool1=True
# var_bool2=False
# var_bool3="True"
# var_result=var_bool1 and var_bool2 and var_bool3
# print(var_result)

# constants
# CONST_VAR_1=100
# CONST_VAR_1=50
# print(CONST_VAR_1)
# strings are immutable, other-value "constants" are not

# multi-assignments
# a,b,c = 1,2,3
# print("a = "+str(a)+", b = "+str(b)+", c = "+str(c))
# print("a ("+str(a)+") + b ("+str(b)+") + c ("+str(c)+") = "+str(a+b+c))

# increment / decrement operators
# aso = 5
# # aso = aso + 5
# aso += 5
# aso -= 2
# aso *= 3
# print(aso)

# strings
# string_var_1 = "danielpm"
# int_var = 1982
# string_var_2 = ".com"
# string_var_full = string_var_1+str(int_var)+string_var_2
# text_var = '''Hello World ! This is a big text string
# (between triple single quotes) !!!!!!!!!!'''
# print(text_var)
# print(string_var_full)

# automatic casting in strings
# first_name="Daniel"
# second_name="danielpm"
# third_name=1982
# print(f'Hello {first_name} from {second_name}{third_name} !') #format string operator
# print('Hello {first} from {second}{third} !'.format(first=first_name, second=second_name, third=third_name))
# print('Hello {} from {}{} !'.format(first_name, second_name, third_name))
# print('Hello {2} from {1}{0} !'.format(first_name, second_name, third_name)) # scrambled order

# string indexes (start, stop, stepover, reverse)
# my_name = "DaNiEl"
# print(my_name[0]+"\n"+my_name[1]+"\n"+my_name[2]+"\n"+my_name[3]+"\n"+my_name[4]+"\n"+my_name[5])
# print(my_name[0:3])
# print(my_name[0:6])
# print(my_name[0:6:2])
# print(my_name[3:])
# print(my_name[:3])
# print(my_name[::2])
# print(my_name[::])
# print(my_name[-1:])
# print(my_name[-2:])
# print(my_name[-3:])
# print(my_name[-6:])
# print(my_name[::-1])

# scape sequence
# print("Weather is \"great\" today !")
# print("\tWeather \nis \"great\" today !")

# len function
# stringVar = "Daniel"
# print(len(stringVar))
# print(stringVar[0:len(stringVar)])

# example of methods (instead of intrinsic functions)
# stringLogo = "danielpm1982.com"
# print(stringLogo.upper())
# print(stringLogo.split(".")[0]+" - "+stringLogo.split(".")[1])
# print(stringLogo.replace("."," & "))
# print("\'l\' is present at index: ["+str(stringLogo.find("l"))+"]")

# # conversions
# birth_year = input("What year were you born in ?\n")
# birth_year_number = int(birth_year)
# actual_year_number = 2023
# age_number = actual_year_number-birth_year_number
# print(f"You are around {age_number} years old (+-1) !")

# import getpass
# username = input("Username: ")
# password = getpass.getpass()
# password_length = len(password)
# print(f"Hello {username} ! Your password {'*' *password_length} is {password_length} chars long.")

# lists and list slicing
# list slice copies the list to another instance in memory (independent from the original)
# list attribution to another variable, keeps both variables pointing to the same instance in memory
# li = [1,2,3,4,5]
# print(li)
# print(li[0:3:1])
# li2 = li[0:3:1] # if you wanna an independent copy, use slice, for instance: li2 = li[:]
# li2[0]=100
# li2[1]=200
# li2[2]=300
# print(li2)
# print(li)
# li = li2 # if you wanna point out to the same structure in memory, do a simple attribution
# print(li)

#matrices
# matrix = [
#   [5,0,2],[0,1,0],[1,0,1]
# ]
# print(matrix[0][0], matrix[0][1], matrix[0][2])
# print(matrix[1][0], matrix[1][1], matrix[1][2])
# print(matrix[2][0], matrix[2][1], matrix[2][2])

#functions and methods on lists
# my_list=["dog", "bird", "cat"]
# print(my_list)
# print(f"This list has {len(my_list)} elements !")
# my_list.append("fish")
# print(my_list)
# print(f"This list has {len(my_list)} elements !")
# my_list.insert(0,"crab")
# print(my_list)
# print(f"This list has {len(my_list)} elements !")
# my_list.extend(["eagle", "monkey", "lion"])
# print(my_list)
# print(f"This list has {len(my_list)} elements !")
# print(my_list.pop(), my_list.pop(), my_list.pop())
# print(my_list)
# print(f"This list has {len(my_list)} elements !")
# print(my_list.pop(0)) # pop argument is an index or none, and return is an element
# print(my_list)
# print(f"This list has {len(my_list)} elements !")
# my_list.remove("fish") # remove argument is an element (not index), with no return
# print(my_list)
# print(f"This list has {len(my_list)} elements !")
# print(f'\'dog\' value is at index: [{my_list.index("dog")}]')
# print(f"value \"dog\" is at list ? {'dog' in my_list}")
# print(f"value \"dog\" appears at list {my_list.count('dog')} time(s)")
# print(f"value \"leopard\" is at list ? {'leopard' in my_list}")
# print(f"value \"leopard\" appears at list {my_list.count('leopard')} time(s)")
# print(f"unsorted list: {my_list}")
# my_list.sort() # sorts the list itself, doesn't produce or return any copy of the list
# print(f"sorted list: {my_list}")
# my_list.reverse()
# print(f"reversed list: {my_list}")
# print(f"sorted copy of the list: {sorted(my_list)}") # creates a copy of the list that is sorted and returned without modifying the list passed as argument
# print(f"original list: {my_list}")
# just_a_copy = my_list.copy()
# print(just_a_copy.clear()) # the copy is emptied, not the original one
# print(my_list)
# print(list(range(1,21)))
# print(" ".join(["Hi","my", "name", "is", "Daniel", "!"]))

#list unpacking
# a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a,b,c, *other, d)

# None type (like null)
# someVar = None
# print(someVar)

#dictionaries (like a map - unordered key-value pairs... keys must be an immutable value data type and unique inside that data structure)
# dictionary = {
#   "a": 100,
#   "b": 200,
#   "c": True,
#   "d": "some_text_value",
#   "e": [1,2,3]
# }
# print(dictionary)
# print(dictionary["b"])
# print(dictionary["e"][2])

# listOfDictionaries = [
#   {"x": 123},
#   {"y": 456,
#   "z": 789
#   }
# ]
# print(listOfDictionaries)
# print(listOfDictionaries[1]["z"])

# methods on dictionaries
# user = {
#   "id": 100,
#   "first_name": None,
#   "last_name": None
# }
# user["first_name"] = "first_name" # key values are updatable, similar to lists, not immutable
# print(user)
# # get method avoids errors when the key does not exist, returning None... and can also set a default return value instead of None, in this case.
# print(user.get("id"))
# print(user.get("aaa"))
# print(user.get("third_name", "default_third_name"))
# # dict() built-in function (less common than using the literal form for creating dictionaries, as above)
# user2 = dict(v1="value1", v2="value2", v3="value3")
# print(user2)
# print("v1" in user2)
# print("v1" in user2.keys()) # keys() method returns an iterable list of keys
# print("value1" in user2)
# print("value1" in user2.values()) # values() method returns an iterable list of values
# print(user2.items()) # items() method returns an iterable list of tuples (key / value pairs)
# user2.clear() # clears the dictionary items
# print(user2)
# user2 = user.copy() # creates and return a copy of a dictionary
# print(user2)
# print(user2.pop("id")) # pops out and return the pair whose key is the one passed
# print(user2)
# print(user2.popitem()) # pops out and return a randomly chosen pair, not necessarily the last one
# print(user2)
# user2.update({"first_name": "another_name"}) # adds or updates a key-value pair at a dictionary using another dictionary passed as argument
# print(user2)
# user2.update({"n_name": "n_name"})
# print(user2)

#tuples (immutable lists... as such, can be used as keys at dictionaries, differently from lists)
# my_tuple = (1,2,3,4,5,3,4,3)
# print(my_tuple)
# print(my_tuple[0])
# print(my_tuple[1:3:1])
# print(my_tuple.count(3))
# print(my_tuple.index(5))
# print(len(my_tuple))
# temp_dict = {    # example mixing dictionaries, tuples, lists and literals
#   (1,2): "abc",
#   ("x","y"): ["def", "ghi", "jkl"]
# }
# print(temp_dict)

# sets (mutable unordered collection of unique values... repeated values are ignored)
# my_set = {1,"a",5,"b","c",5,1,"c"}
# print(my_set)
# my_set.add(6)
# my_set.add(5)
# my_set.add("c")
# print(my_set)
# another_set = my_set.copy()
# my_set.clear()
# print(my_set)
# print(another_set)
# another_list = list(another_set)
# print(another_list)
# another_list.extend([1,5,6])
# print(another_list)
# print(my_set)
# my_set = set(another_list) # when receiving repeated values through a previously existing data structure or by literals direct attribution, sets will always turn those values unique, excluding redundancies
# print(my_set)
# my_set.update({1, 5, 6, 7}) # adds unexistent but does not substitute existent - keeps all values: new and old ones
# print(my_set)
# print(my_set.pop()) # pops out and returns a radomly chosen value
# print(my_set.pop())
# print(my_set.pop())
# print(my_set)
# my_set.remove(7) # removes but does not return a specified value
# print(my_set)

# setA = {1,2,3,5,6,7}
# setB = {2,5,7,9,10}
# print(setA)
# print(setB)
# print(setA.difference(setB)) # returns A - B (Set theory), but does not change sets
# setB.discard(10)
# print(setB)
# setA.difference_update(setB) # changes set A to (A - B), but does not return anything
# print(setA)
# setA = {1,2,3,5,6,7}
# print(setA.intersection(setB)) # returns intersection, but does not change sets
# setA.intersection_update(setB) # changes setA to the intersection of A intersect B, and does not return anything
# print(setA)
# setA = {1,2,3,5,6,7}
# setB = {2,5,7,9,10}
# print(setA.isdisjoint(setB)) # checks if are two disjoint sets, returning boolean
# print(setA.union(setB)) # returns a new set that is A U B, without duplicates
# print(setA | setB) # shortcut for A U B
# print(setA & setB) # shortcut for A intersection B
# setA = {1,2,3}
# setB = {1,2,3,5,7,9,10}
# print(setA.issubset(setB)) # checks if A is a subset of B (all elements of A belong to B, A is contained by B and B contains A)
# print(setB.issuperset(setA)) # checks if B is a superset of A (contains A)

#conditional logic
# arg1 = True
# arg2 = True
# if arg1 and arg2:
#   print("All args are true !")
# elif arg1:
#   print("Only arg1 is true !")
# elif arg2:
#   print("Only arg2 is true !")
# else:
#   print("No args is true ! All false !")
# print("This current statement is outside the logical flux above !")

#ternary operator (conditional expression)
# is_adult = False
# msg = "You can set parental configs !" if is_adult else "Parental configs only for adults !"
# print(msg)

#short circuit
# var_bool_a=True
# var_bool_b=False
# if var_bool_a | var_bool_b:
#   print("result: short-circuit on var_bool_a, var_bool_b never evaluated !")
# if (not var_bool_b & var_bool_a):
#   print("result: short-circuit on var_bool_b, var_bool_a never evaluated !")

#Truthy and Falsy statements
# print(bool(True))
# print(bool(False))
# print(bool([]))
# print(bool(()))
# print(bool({}))
# print(bool(set()))
# print(bool(""))
# print(bool(range(0)))
# print(bool(0))
# print(bool(0.0))
# print(bool(0j))
# print(bool(None))
# print(bool([1,2,3]))
# print(bool("a"))
# print(bool(33))
# print(bool(range(1,10)))

#logical operators
# print(5 == 5)
# print(1 < 10)
# print(10 <= 10)
# print(10 > 1)
# print(10 >= 10)
# print("a" < "z")
# print("a" > "A")
# print(1 < 2 < 3 < 0 < 4 < 5) # short-circuit at '< 0'
# print("a" != "A")
# print(5 != 50)
# print(True and True and (not False) or False)
# print(True & True & (not False) | False)

# "=="" versus "is"
# "==" checks values, trying to transform them to bool (doesn't always work for different types) - use preferably for same types... while "is" compares memory positions. Simple constant literals have the same memory position in memory, while data structures don't.
# print(5==5.0)
# print("a"=="A")
# print([] == [])
# print([1] == [1])
# print([] == [1])
# print(1 == "1")
# print(0 == "")
# print(False == ())
# print(True == 1)
# print()
# print(5 is 5.0)
# print("a" is "A")
# print([] is [])
# print([1] is [1])
# print([] is [1])
# print(1 is "1")
# print(0 is "")
# print(False is ())
# print(True is 1)
# print(5 is 5)
# print("a" is 'a')
# print(True is True)

# looping with 'for' (lists, dictionaries, tuples, sets and other iterable objects)
# char_list = []
# for i in "danielpm1982.com":
#   char_list.append(i)
# print(char_list)

# #iterating dictionaries in 4 different ways
# dict_client = {
#   "client_0": "Peter",
#   "client_1": "Peter",
#   "client_2": "Mary",
#   "client_3": "Junior",
#   "client_4": "Junior",
#   "client_5": "Junior"
# }
# print(dict_client) #iterating the whole dictionary

# for key,value in dict_client.items(): #iterating tuples (key, value) from the items() list
#   print(key+": "+value)

# for key in dict_client.keys(): #iterating keys from the list of keys and getting each respective value
#   print(f"{key} -> {dict_client.get(key)}")

# # custom function that removes duplicities of items in a list
# def eliminate_duplicities_from_list(original_list):
#   unique_elements_temp = []
#   for i in original_list:
#     if(i not in unique_elements_temp):
#       unique_elements_temp.append(i)
#   return unique_elements_temp
# # iterating non unique list of values and getting matching key(s) - including multiple keys for one same value. Must eliminate duplicities in values list before looking for matching key(s). For that, a custom function is defined above.
# for value in eliminate_duplicities_from_list(list(dict_client.values())):
#   for key in dict_client.keys():
#     print(f'{value} <- {key}\n' if (key,value) in dict_client.items() else "", end="")

# nested loops
# receipt_list = []
# index_i, index_j, index_k, total = 0, 0, 0, 0
# for i in ("milk", "chocolate", "coffee"):
#   index_i+=1
#   for j in ("banana", "apple", "grape", "pineapple", "pear"):
#     index_j+=1
#     for k in ("sugar", "sweetener", "no sugar or sweetener"):
#       index_k+=1
#       receipt_list.append(f"{index_i}.{index_j}.{index_k} - {i} with {j} and {k}")
#       total+=1
#     index_k=0
#   index_j=0
# index_i=0
# for r in receipt_list:
#   print(r)
# for l in range(1,31):
#   print("↑",sep="",end=" ")
# print("", end="\n")
# for l in range(1,31):
#   print("-",sep="",end=" ")
# print("", sep="", end="\n", flush=False)
# for l in range(1,31):
#   print("↓",sep="",end=" ")
# print("", sep="", end="\n", flush=False)
# print(f"Total: {total} receipts generated !")

#range object
# for i in range(1,11,1):
#   print(i)
# print("")
# for i in range(10,0,-1):
#   print(i)

# #enumerate object
# for i,char in enumerate("danielpm1982.com"): #enumeration with index starting at 0
#   print(f"{i}: {char}")

# for i,item in enumerate(list(range(1,101,1)),1): #enumeration with index starting at 1
#   print(f"{i}: {item}")

# looping with 'while' (lists, dictionaries, tuples, sets and other iterable objects)
# i = 1
# while(i < 21):
#   print(i)
#   if(i==10): #optionally using breaking points (if breaks, else won't run)
#     break
#   i += 1
# else:
#   print("While loop ended !!")

# j=0
# while_list = ["cat", "dog", "fish"]
# while j < len(while_list):
#   print(while_list[j])
#   j+=1

# while True:
#   response = input('say something:')
#   if(response.strip() == "exit"):
#     break

# number_var = 0
# result = []
# while(number_var<1000):
#   number_var+=1
#   if(number_var%2!=0):
#     continue
#   result.append(number_var)
#   pass
# else:
#   print("All Done !!")
# for n in result:
#   print(n,sep=" ", end=" ")

#custom functions, parameters, arguments
#no return (None) function with simple positional parameters (no default parameter values)
# def say_hello(name, year_of_birth, had_birthday_already_current_year, current_year):
#   print(f"Hello {name} !")
#   age = 0
#   if(had_birthday_already_current_year):
#     age = current_year-year_of_birth
#   else:
#     age = current_year-year_of_birth-1
#   print(f"Your current age is: {age} years old !")
# #function call / invoke with simple positional arguments (no keyword arguments)
# say_hello("Daniel", 1980, True, 2023)
# say_hello("John", 1992, False, 2023)
# say_hello("Mary", 1998, True, 2023)

#return functions
# def calc_fibonnaci(number=0): #default parameter values
#   if(number<=1):
#     return number
#   return calc_fibonnaci(number-1)+calc_fibonnaci(number-2)
# n = 25
# #keyword argument (more useful for more than one positional params, to guarantee the right assignment of each arg to each respective param, although being bad practice and causing confusion for not following the right order of the parameters at the defined function)
# print(f"Fibonnaci of {n} is equal to {calc_fibonnaci(number=n)} !")
# #no-arg, defaulting to 0 as defined at the function
# print(f"Fibonnaci of no-arg (default = 0) is equal to {calc_fibonnaci()} !")

#nested functions
# def get_sum_string(number1, number2):
#   def do_sum(): #no need for args in this case, although it could have its own params
#     return number1+number2
#   return f"{number1} + {number2} = {do_sum()}"
# print(get_sum_string(10,8))

#docstrings and ways of using it (in some browsers popup documentation won't work when using replit)
# def some_function(some_param):
#   '''
#   This is an echo function that echoes the value of the arg assigned to the local param some_param !
#   '''
#   print(some_param)
# some_function("Hello World !")
# help(some_function)
# print(some_function.__doc__)

# *args and **kwargs
# def sum_many_positional_args_func(*args):
#   return sum(args)
# print(sum_many_positional_args_func(1,2,3,4,5))

# def sum_many_keyword_args_func(**kwargs):
#   return sum(kwargs.values())
# print(sum_many_keyword_args_func(a=1,b=2,c=3,d=4,e=5))

# def print_all_types_of_args(param1, param2, *args, default_param=0, **kwargs):
#   '''
#   This function exemplifies how to receive and print different types of param args.
#   The right order must be followed at the function declaration:
#   1st: declared positional param args
#   2nd: undeclared and variable-number positional param args using the * operator, e.g. *args
#   3rd: default param args
#   4th: undeclared and variable-number keyword param args using the ** operator, e.g. **kwargs
#   \nThe function then simply prints all values.
#   '''
#   print(f"=> declared positional args: param1={param1}, param2={param2}")
#   print("=> variable-number positional args:")
#   arg_index=-1
#   for arg in args:
#     arg_index+=1
#     print(f"{arg_index}: {arg}")
#   print(f"=> default param: {default_param}")
#   print("=> variable-number positional keyword args:")
#   for key,value in kwargs.items():
#     print(f"{key}: {value}")
# print_all_types_of_args("param1_value", "param2_value", 1, 2, 3, 4, 5, a="abc", b="def", c="ghi")

# def highest_even(arg_list=None):
#   '''
#   This function receives a non-empty list of numbers and returns, if exists, the highest even number.
#   '''
#   if arg_list and len(arg_list)>0:
#     even_list = []
#     for n in arg_list:
#       if n%2==0:
#         even_list.append(n)
#     if(len(even_list)>0):
#       return max(even_list)
#     else:
#       return "No even numbers at the arg list !"
#   else:
#     return "You gotta pass a non-empty list as an arg !"
# print(highest_even([1,2,3,8,12,87,6102,9,99]))
# print(highest_even([102,2,16,17,23,33,68]))
# print(highest_even([1,2,3,8,12,87,6102,9,2222222222]))
# print(highest_even([1,3,5,7,9]))
# print(highest_even([]))
# print(highest_even())

# #scope in python - priorization in detecting which variable or function is being called (for instance, when there are more than one with the same name)
# #1st priority - local scope inside a function
# #2nd priority - local scope inside a parent function (nested functions)
# #3rd priority - global scope - outside any functions, inside the .py file
# #4th priority - built-in python functions
# repeated_var = 1
# def parent_function():
#   repeated_var = 2
#   print(repeated_var)
#   def nested_function():
#     repeated_var = 3
#     return repeated_var
#   return nested_function()

# print(repeated_var) # this will access the global-scope repeated_var variable (1)
# print(parent_function()) # this will have returned the nested_function local-scope repeated_var (3), but, before that, the parent_function local-scope repeated_var (2) will be printed. If repeated_var wasn't also declared inside the nested_function own scope (3), the program would have taken the repeated_var from the parent_function local scope (2). If this one also wasn't defined, the nested_function repeated_var returned would have been the one at the global scope (acessed from the nested_function scope). When local-scope variables have their values changed, this does not affect the global-scope or outer-scope same-name variables' values
# print(max("a","b","c")) #if a variable or function is called and there's no other scope where it is defined, the interpreter will look up to the built-in functions scope to see if that name matches any, but only after checking the other scopes (global and local ones). "max" function is not defined anywhere at this main.py file, so it will invoke the python built-in scope max() function. If a max() is defined anywhere else, the above precedence will be considered regarding which max() function to call

#global and nonlocal keywords
#global keyword links to a global variable from inside the local scope. It avoids having to declare a previously declared global variable as local, for instance, when reassigning its value, and, at the same time, persists any change at the global variable accessed from inside the function... as there's actually only the global-scope variable. If local variables were declared inside the function(), any change to it wouldn't have any effect on the global one, differently from when global keyword is used, as below:
# some_var=1
# def some_function():
#   global some_var # this is not a declaration of a local variable, but a link to the global one
#   some_var+=1
#   print(some_var)
# some_function()
# print(some_var)
#nonlocal keyword links to a parent-scope declared variable from an inner-scope, in order that the variable can have its value manipulated and persisted from the inner scope. If a local inner-scope variable would have been created, any change on it wouldn't persist at the outer one, as there would be two different and independent variables (although with the same name)... and only the inner one would have had its value changed.
# def outer_function():
#   some_var=1
#   def inner_function():
#     nonlocal some_var # this is not a declaration of a local variable, but a link to the outer one
#     some_var+=1
#   inner_function()
#   print(some_var)
# outer_function()

#functional programming in Python
#pure functions - functions that have no side-effects (do not affect any external element), and that given the same input always return the same output
# input_list = [1,2,3]
#in the use case below, a pure function should not alter the external input_list - should work with and return another list, declared inside it - in this case, the output_list - leaving the input_list (and external scope state) as it is
# def multiply_by_2_taking_list(input_list):
#   output_list = []
#   for item in input_list:
#     output_list.append(item*2)
#   return output_list
# print(multiply_by_2_taking_list(input_list))
# print(input_list)
# map, filter, zip, reduce
#in the same use case, but using map() function instead, this streaming function will iterate over each item from the iterable arg passed and run the pure function - passed as the first arg - on each element, returning a new iterable and not altering the external iterable received as arg (not altering the external scope). The pure function now should work on individual items (instead of on a list of items), as the map() function will be in charge of iterating the list implicitly
# def multiply_by_2_taking_item(input_item):
#     return input_item*2
# print(list(map(multiply_by_2_taking_item, input_list))) #only the function name should be passed as arg, the map will invoke it implicitly
# print(input_list)
#in the same yet use case above, but now using lambda in place of the pure functions, we would have the same result using the map() streaming function as well. The lambda will substitute the pure function as the first arg for the streaming map() function, while the iterable would continue being the second arg
# print(list(map(lambda x: x*2, input_list)))

# name_list=["Daniel", "john", "pEtEr", "mATHEw"]
# print("Change the list items all to UPPERCASE:")
# print(name_list)
# print(list(map(lambda x: x.upper(), name_list)))

# number_list=[1,2,4,6,7,7,8,0,0,9,6,4,40,33,20,33]
# # def is_odd(number):
# #   return number%2!=0
# # print("Odd numbers in the list:")
# # odd_number_list = list(filter(is_odd, number_list))
# odd_number_list = list(filter(lambda x:x%2!=0, number_list))
# print(odd_number_list)
# print("Without duplicates:")
# print(sorted(set(odd_number_list)))

# name_list = ["Daniel", "John", "Peter", "Mathew"]
# phone_tuple = ["555-5555", "855-2222", "355-1111", "888-4432"]
# birth_year_set = [1980, 1995, 1950, 2000]
# zip_list = list(zip(name_list, phone_tuple, birth_year_set, strict=True))
# print(zip_list)
# print("")
# print(f"NAME\t\tPHONE\t\tBIRTH_YEAR")
# print(f"----\t\t-----\t\t----------")
# for name, phone, birth_year in zip_list:
#   print(f"{name}\t\t{phone}\t\t{birth_year}")

# from functools import reduce
# # def add(x,y):
# #   return x+y
# # print(reduce(add, [1,2,3,4,5], 0))
# print(reduce(lambda x,y:x+y, [1,2,3,4,5], 0))

# comprehensions for creating lists, sets and dictionaries
# my_list = [f"*{char}*" for char in "danielpm1982.com"]
# print(my_list)

# my_odd_list = [number**3 for number in range(1,11) if number%2!=0]
# print(my_odd_list)

# my_set = {f"*{char}*" for char in "danielpm1982.com"}
# print(my_set)

# base_dictionary = {
#   "a": 1,
#   "b": 2,
#   "c": 3
# }
# my_dictionary_from_base_dictionary = {k: v**3 for k, v in base_dictionary.items() if v%2==0}
# print(my_dictionary_from_base_dictionary)

# base_list = [1,2,3,4,5]
# my_dictionary_from_base_list = {str(item)+"^2": item**2 for item in base_list if item**2<10}
# print(my_dictionary_from_base_list)
