"""[

1,2,3
4,5,6
]

add, row 0,10

"""

import sys
from file_handler import FileHandler

arguments = sys.argv[1:]
print(arguments)

#
# temp_matrix = [[1,2,3],
#                [4,5,6],
#                [7,8,9]]
# value_1 = temp_matrix[0]

file_handler = FileHandler(
    input_file_path=arguments[0],
    output_file_path=arguments[1],
    transformations=arguments[2],
)
print(file_handler.data)
file_handler.save_data()
