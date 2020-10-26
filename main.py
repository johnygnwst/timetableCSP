from csp import *

result = recursive_backtracking(init_assignment(my_csp), my_csp)
# print(str(counter) + "; \n" + str(result.keys()) + "\n" +str(result.values()))
for i in result.keys():
    print(str(i) + "   " + result.get(i))