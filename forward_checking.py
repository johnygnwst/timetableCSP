from random import shuffle

from csp_init import *
csp = my_csp

counter = 0
var_domains = {}
degree_values = {}

#init empty assignment
def init_assignment_forw(csp):
  global var_domains
  global counter
  counter = 0
  assignment = {}
  for var in csp[VARIABLES]:
    assignment[var] = None
    var_domains[var] = csp[DOMAINS].copy()
  return assignment


def getRoom(csp, assignment,var, value):
  rooms = data._rooms
  rooms.sort(key=lambda c: c[1])
  
  for r in rooms:
    if (r[1] >= var._number_of_students):
      free = True
      for k in csp[VARIABLES]:
        if (assignment[k] is not None):
          if (k._room == r and assignment[k] == value):
            free = False
      if free:
       return r



def forward_checking(assignment,csp):
  global var_domains
  global counter
  rnd_domains_f = csp[DOMAINS][:]
  while True:
    if is_complete(assignment):
      return assignment
    var = select_unassigned_variable(csp[VARIABLES],assignment)
    shuffle(rnd_domains_f)
    for value in rnd_domains_f:

      if is_in_domain(var, value):
        assignment[var] = value
        add_domains(assignment, csp, var)
        var._room = getRoom(csp,assignment, var, value)
        counter+=1
        if is_consistent(assignment, csp[CONSTRAINTS]):    
          break
        else: 
          assignment[var] = None
          var._room = None
          undo(assignment,csp)
  return FAILURE



def is_in_domain(var,value):
  global var_domains
  for d in var_domains[var]:
    if (d == value):
      return True
  return False



def add_domains(assignment, csp, value):
  global var_domains
  j = value
  for i in csp[VARIABLES]:
    if (assignment[i] is None):
      if (not i==j):
        if (i._teacher == j._teacher):
          for k in range(len(var_domains[i])):
            if (var_domains[i][k] == assignment[j]):
              var_domains[i][k] = None
        if (i._speciality == j._speciality ):
          for k in range(len(var_domains[i])):
            if (var_domains[i][k] == assignment[j]):
              var_domains[i][k] = None


def undo(assignment, csp):
  global var_domains
  for var in csp[VARIABLES]:
    var_domains[var] = csp[DOMAINS].copy()
  for i in csp[VARIABLES]:
    for j in csp[VARIABLES]:
      if (assignment[j] is not None):
        if (not i==j):
          if (i._teacher == j._teacher):
            for k in range(len(var_domains[i])):
              if (var_domains[i][k] == assignment[j]):
                var_domains[i][k] = None
          if (i._speciality == j._speciality):
            for k in range(len(var_domains[i])):
              if (var_domains[i][k] == assignment[j]):
                var_domains[i][k] = None


def get_counter_forw():
  global counter
  return counter




