import random

def random_list(start, end, num_items):
    # random_list = []
    # for _ in range(num_items):
    #     random_list.append(random.randint(start, end))
    # random_list = [random.randint(start, end) for i in range(num_items)]
    random_list = random.sample(range(start, end+1), num_items)
    return random_list

inp = input("Enter the starting number the ending number and the number of items to generate: \n")
inps = inp.split()
start_num, end_num, num_items = int(inps[0]) ,int(inps[1]), int(inps[2])

rand_list = random_list(start_num, end_num, num_items)

print("Random list:", rand_list)
print("Number of items:", len(rand_list))


