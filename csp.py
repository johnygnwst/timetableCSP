from data import *

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
  pass



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


###########################################################


my_csp = {}
