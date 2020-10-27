from csp_init import *
csp = my_csp




#init empty assignment
def init_assignment(csp):
  assignment = {}
  for var in csp[VARIABLES]:
    assignment[var] = None
  return assignment

#recursive backtracking
def recursive_backtracking(assignment, csp):
  global counter
  if counter == 100:
    return FAIL
  if is_complete(assignment):
    return assignment
  var = select_unassigned_variable(csp[VARIABLES], assignment)
  for value in csp[DOMAINS]:
    assignment[var] = value
    if is_consistent(assignment, csp[CONSTRAINTS]):
      result = recursive_backtracking(assignment, csp)
      if result != FAILURE:
        return result
    assignment[var] = None
  return FAILURE
