from data import *
data = Data()
classes = data._classes
meeting_times = data.MEETING_TIMES

counter = 0
mrv_domains = {}

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
  global mrv_domains
  assignment = {}
  for var in csp[VARIABLES]:
    assignment[var] = None
    mrv_domains[var] = csp[DOMAINS].copy()
  return assignment




#mrv backtracking
def mrv_backtracking(assignment, csp):
  global mrv_domains

  if is_complete(assignment):
    return assignment

  var = find_mrv(assignment,csp)
  print(var)
  for value in csp[DOMAINS]:
    if (is_in_domain(value, mrv_domains[var])):
      assignment[var] = value
      add_to_mrv_domains(assignment,csp,var)
      if is_consistent(assignment, csp[CONSTRAINTS]):
        result = mrv_backtracking(assignment, csp)
        if result != FAILURE:
          return result
      assignment[var] = None
      undo(assignment,csp)


  
  for i in assignment.keys():
    print(str(i) + "   " + assignment.get(i))
  return FAILURE



def undo(assignment, csp):
  global mrv_domains
  for var in csp[VARIABLES]:
    mrv_domains[var] = csp[DOMAINS].copy()
  for i in csp[VARIABLES]:
    for j in csp[VARIABLES]:
      if (assignment[j] is not None):
        if (not i==j):
          if (i._teacher == j._teacher):
            for k in range(len(mrv_domains[i])):
              if (mrv_domains[i][k] == assignment[j]):
                mrv_domains[i][k] = None
          if (i._audience == j._audience):
            for k in range(len(mrv_domains[i])):
              if (mrv_domains[i][k] == assignment[j]):
                mrv_domains[i][k] = None


def is_in_domain(value, domain):
  for d in domain:
    if (d == value):
      return True
  return False



def add_to_mrv_domains(assignment, csp, value):
  global mrv_domains
  global prev_assignment
  j = value
  for i in csp[VARIABLES]:
    if (not i==j):
      if (i._teacher == j._teacher):
        for k in range(len(mrv_domains[i])):
          if (mrv_domains[i][k] == assignment[j]):
            mrv_domains[i][k] = None
      if (i._audience == j._audience):
        for k in range(len(mrv_domains[i])):
          if (mrv_domains[i][k] == assignment[j]):
            mrv_domains[i][k] = None

def get_domains():
  global mrv_domains
  return mrv_domains


def domain_len(domain):
  res = 0
  for d in domain:
    if d is not None:
      res +=1
  return res


def find_mrv(assignment, csp):
  global mrv_domains
  min_val = select_unassigned_variable(csp[VARIABLES], assignment)
  min_domain = domain_len(mrv_domains[min_val])
  for i in csp[VARIABLES]:
    if (assignment[i] is None):
      if (domain_len(mrv_domains[i]) < min_domain):
        min_val = i
        min_domain = domain_len(mrv_domains[min_val])
  if (min_val==0):
    print("zero lennnn")
  return min_val

def equal(a, b): return a is not None and b is not None and a == b

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