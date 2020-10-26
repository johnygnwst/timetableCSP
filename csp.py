from data import *
data = Data()
classes = data._classes
meeting_times = data.MEETING_TIMES

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
      print("select empty: " + str(var))
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
      print("no conflicts ")
      result = recursive_backtracking(assignment, csp)
      if result != FAILURE:
        return result
    assignment[var] = None
  print("Failure: ")
  for i in assignment.keys():
    if assignment.get(i) is not None:
      print(str(i) + "   " + assignment.get(i))
  print("____")
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
def equal(a, b): return a is not None and b is not None and a == b

# def test(assignment):
#   return equal(assignment[], assignment[])


def get_var(assignment):
  arr = []
  for i in assignment.keys():
    newClass = i
    if assignment[i] is not None:
      arr.append(newClass)
  return arr



def same_audiences(assignment):
  arr = get_var(assignment)
  if len(arr) == 1:
    return False
  for i in arr:
    for j in arr:
      if equal(i._audience, j._audience) and i!=j and assignment[i]==assignment[j]:
        return True
  return False


def same_teacher(assignment):
  arr = get_var(assignment)
  if len(arr) == 1:
    return False
  for i in arr:
    for j in arr:
      if equal(i._teacher, j._teacher) and i!=j and assignment[i]==assignment[j]:
        return True
  return False


###########################################################


my_csp = {VARIABLES: classes,
          DOMAINS: meeting_times,
          CONSTRAINTS: [same_audiences, same_teacher]
          }


def get_counter():
  global counter
  return counter
