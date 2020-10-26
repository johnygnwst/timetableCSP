from csp import *
from mrv import *




result = mrv_backtracking(init_assignment(my_csp), my_csp)
#assig = init_assignment(my_csp)
#result = get_domains()
print(str(get_counter()))
for i in result.keys():
    #print(str(i) + "   " + str(result[i]))
    print(str(i) + "   " + result.get(i))


#result = mrv_backtracking(init_assignment(my_csp), my_csp)




