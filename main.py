from csp import *
from mrv import *
from lcv import *




result = lcv_backtracking(init_assignment(my_csp), my_csp)
#assig = init_assignment(my_csp)
#result = get_domains()
print(str(get_counter_lcv()))
for i in result.keys():
    #print(str(i) + "   " + str(result[i]))
    print(str(i) + "   " + result.get(i))


#result = mrv_backtracking(init_assignment(my_csp), my_csp)




