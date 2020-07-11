import sys
import ast
array1 = ast.literal_eval(sys.argv[1])
array2 = ast.literal_eval(sys.argv[2])
print(sorted(array1 + array2))
