#Question 9 

my_list = [10, 20, 30, 9]
target = 59


triplet_list = []

n = len(my_list) 

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        required_sum = target - (my_list[i] + my_list[j])
       
        elements_set = set(my_list[j + 1:])
        if required_sum in elements_set:
            triplet_list.append((my_list[i], my_list[j], required_sum))


print(triplet_list)

