list = [1, 2, 3, 4, 5]
list_1 = []
new_list =[ s+1 for s in list]
new_list_1 = [ num *2 for num in range(1 , 5)]
print(new_list_1)
#eg for string
name = "Victor"
letter_list = [letter for letter in name]
new_list_of_name = ["ada", "obi","Nduka","ken"]
short_name = [name.upper() for name in new_list_of_name if len(name) < 5]
print(short_name)
print(letter_list)


# this is an alternative way for looping
# for s in new_list:
#     new_list = s + 1
#     print(new_list)




