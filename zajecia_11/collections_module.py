from collections import defaultdict, Counter

very_long_string = "thisdsadnasjdnsa jdjnsajdjn sajdnjsnajdknas jddsadjnsajndjs"

counter_dict = {}
default_counter_dict = defaultdict(int)

counter = Counter(very_long_string)
print(counter)


# for letter in very_long_string:
#     default_counter_dict(letter) +=1


# for letter in very_long_string:
#     if letter in counter_dict.keys():
#         counter_dict[letter] += 1
#     else:
#         counter_dict[letter] = 1
