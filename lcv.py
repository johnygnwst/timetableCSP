# from data import *
# data = Data()
# classes = data._classes
# meeting_times = data.MEETING_TIMES

# counter = 0
# lcv_domains = {}

# DOMAINS = "DOMAINS"
# VARIABLES = "VARIABLES"
# CONSTRAINTS = "CONSTRAINTS"
# FAILURE = "FAILURE"

# def is_complete(assignment):
#   return None not in (assignment.values())


# def select_unassigned_variable(variables, assignment):
#   for var in variables:
#     if assignment[var] is None:
#       return var  


# def is_consistent(assignment, constraints):
#   global counter
#   counter += 1
#   for constraint_violated in constraints:
#     if constraint_violated(assignment):
#       return False
#   return True


# #init empty assignment
# def init_assignment_lcv(csp):
#   global lcv_inf
#   assignment = {}
#   lcv_inf = {}
#   for var in csp[VARIABLES]:
#     assignment[var] = None
#     lcv_domains[var] = []
#   init_lcv(csp)
#   return assignment


# def init_lcv(csp):
#   global lcv_domains
#   for var in csp[VARIABLES]:
#     dom = []
#     val = []
#     for i in csp[DOMAINS]:
#       dom.append(i)
#       t = 0
#       for j in csp[VARIABLES]:
#         if (not var==j):
#           if (var._audience == j._audience):
#             t += 1
#           if (var._teacher == j._teacher):
#             t += 1

#       val.append(t)
  
#     print("val++++++++++++++++++")
#     print(val)
#     for g in range(len(val) - 1):
#       for j in range(len(val) -1):
#         if (val[j] > val[j+1]):
#           a = val[j]
#           val[j] = val[j+1]
#           val[j+1] = a
#           s = dom[j]
#           dom[j] = dom[j+1]
#           dom[j+1] = s


#     lcv_domains[var] = dom
#   print(lcv_domains)





# #recursive backtracking
# def lcv_backtracking(assignment, csp):
#   global lcv_domains
#   if is_complete(assignment):
#     return assignment
#   var = select_unassigned_variable(csp[VARIABLES], assignment)
#   for value in lcv_domains[var]:
#     print (lcv_domains[var])
#     assignment[var] = value
#     if is_consistent(assignment, csp[CONSTRAINTS]):
#       result = lcv_backtracking(assignment, csp)
#       if result != FAILURE:
#         return result
#     assignment[var] = None
#   return FAILURE




# def update_lcv(assignment, csp):
#   global lcv_values
#   for i in csp[VARIABLES]:
#     val = 0
#     for j in csp[VARIABLES]:
#       if (not i==j):
#         if (assignment[j] is None):
#           if (i._audience == j._audience):
#             val += 1
#           if (i._teacher == j._teacher):
#             val += 1
#     lcv_values[i] = val



# def lcv(assignment, csp):
#   global lcv_inf
#   minVar = select_unassigned_variable(csp[VARIABLES], assignment)
#   minVal = lcv_inf[minVar]
#   for i in csp[VARIABLES]:
#     if (lcv_inf[i] < minVal):
#       minVar = i
#       minVal = lcv_inf[i]
#   return minVar



# ####################### constraints #######################
# def equal(a, b): return a is not None and b is not None and a == b

# # def test(assignment):
# #   return equal(assignment[], assignment[])


# def get_var(assignment):
#   arr = []
#   for i in assignment.keys():
#     newClass = i
#     if assignment[i] is not None:
#       arr.append(newClass)
#   return arr



# def same_audiences(assignment):
#   arr = get_var(assignment)
#   if len(arr) == 1:
#     return False
#   for i in arr:
#     for j in arr:
#       if equal(i._audience, j._audience) and i!=j and assignment[i]==assignment[j]:
#         return True
#   return False


# def same_teacher(assignment):
#   arr = get_var(assignment)
#   if len(arr) == 1:
#     return False
#   for i in arr:
#     for j in arr:
#       if equal(i._teacher, j._teacher) and i!=j and assignment[i]==assignment[j]:
#         return True
#   return False


# ###########################################################


# my_csp = {VARIABLES: classes,
#           DOMAINS: meeting_times,
#           CONSTRAINTS: [same_audiences, same_teacher]
#           }


# def get_counter_lcv():
#   global counter
#   return counter