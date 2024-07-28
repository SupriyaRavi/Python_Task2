#Question 10 : 

my_list = [4, 2, -3, 1, 6]

my_result = 0
my_dict = {0: -1}

for index, num in enumerate(my_list):
    my_result += num
    
    if my_result in my_dict:
        start_index = my_dict[my_result] + 1
        end_index = index
        sublist = my_list[start_index:end_index + 1]
        print(sublist)
        break
    
    my_dict[my_result] = index
