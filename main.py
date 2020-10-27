from csp import *
from mrv import *
from lcv import *
from data import *
from csp_init import *



# c = my_csp

# result = "FAIL"
# while (result == "FAIL"):
# 	result = recursive_backtracking(init_assignment(c), c)


# print(str(get_counter_csp()))
# for i in result.keys():
#     #print(str(i) + "   " + str(result[i]))
#     print(str(i) + "   " + result.get(i))


#result = mrv_backtracking(init_assignment(my_csp), my_csp)


# print("#############################################################")
result = recursive_backtracking(init_assignment(my_csp), my_csp)
print(str(get_counter()))
for i in result.keys():
	print(str(i) + "   " + str(result[i]))
    #print(str(i) + "   " + result.get(i))




# print("#############################################################")
# result = lcv_backtracking(init_assignment_lcv(c), c)
# print(str(get_counter_lcv()))
# for i in result.keys():
#     #print(str(i) + "   " + str(result[i]))
#     print(str(i) + "   " + result.get(i))




