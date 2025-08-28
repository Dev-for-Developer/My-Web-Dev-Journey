my_list = [1,2,3,4,5]
# print(my_list)
my_tup = (1,2,3,4,5,6,6,6,6)
# print(my_tup)

my_set1 = {1,2,3,3,4,5,5,6,6,6}
# print(my_set)
my_set2 = {11,23,53,64,44}

my_dict = {"name":"Dev", "age":21,"Gender":"Male"}
# print(my_dict)
# for key,values in my_dict.items():
    # print(key,values)

diff = my_set2.difference(my_set1)
# print(diff)

name = "Dev"
age = 21
my_string = f"My name is {name} and age is {age}"
# print(my_string)

func = lambda x,y : x * y
res = func(4,9)
print(res)