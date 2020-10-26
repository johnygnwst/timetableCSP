from data import *
data = Data()

counter = 0

DOMAINS = "DOMAINS"
VARIABLES = "VARIABLES"
CONSTRAINTS = "CONSTRAINTS"
FAILURE = "FAILURE"

def is_complete(assignment):
  return None not in (assignment.values())


def select_unassigned_variable(variables, assignment):
  for var in variables:
    if assignment[var] is None:
      return var  


def is_consistent(assignment, constraints):
  global counter
  counter += 1
  for constraint_violated in constraints:
    if constraint_violated(assignment):
      return False
  return True


#init empty assignment
def init_assignment(csp):
  assignment = {}
  for var in csp[VARIABLES]:
    assignment[var] = None
  return assignment


#recursive backtracking
def recursive_backtracking(assignment, csp):
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


#minimum remaining values
def mrv(assignment, csp):
  pass


#degree heuristic
def degree_heuristics(assignment, csp):
  pass


#heuristic with the least restrictive value
def lrv(assignment, csp):
  pass


#forward checking heuristic
def forward_checking(assignment, csp):
  pass


#constraint propagation heuristic
def constraint_propagation(assignment, csp):
  pass


####################### constraints #######################
def eq(a, b): return a is not None and b is not None and a == b


###########################################################


my_csp = {VARIABLES: data._classes,
          DOMAINS: data.MEETING_TIMES,
          CONSTRAINTS: []}
