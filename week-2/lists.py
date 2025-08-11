my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

my_list.insert(1, 15)
print(my_list)

list = [50, 60, 70]
my_list.extend(list)
print(my_list)

del my_list[-1]
print(my_list)

sorted_list = sorted(my_list)
print(sorted_list)

if 30 in my_list:
    index = my_list.index(30)  # find the index of 30
    print(f"Value at index {index} is {my_list[index]}")