from csp import *

result = recursive_backtracking(init_assignment(my_csp), my_csp)
print(str(get_counter()))
for i in result.keys():
    print(str(i) + "   " + result.get(i))