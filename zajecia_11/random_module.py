import random

for number in range(6):
    print(random.randint(1, 10))

# print(random.choices(range['wojtek','adam'], k=1))

names_list = ["adam", "michal", "pies"]
for x in range(len(names_list)):
    selected_name = random.choices(names_list, k=1)
    print(selected_name[0])
    names_list.remove(selected_name[0])
