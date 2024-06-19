import random

from csp_init import *

csp = my_csp

counter = 0
var_domains = {}
degree_values = {}

#init empty assignment
def init_assignment_default(csp):
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

#recursive backtracking
def backtracking(assignment, csp, heuristic):
  global counter
  rnd_domains_back = csp[DOMAINS][:]
  while True:
    if is_complete(assignment):
      return assignment
    random.shuffle(rnd_domains_back)
    for value in rnd_domains_back:
      var = heuristic(assignment)#get an unassigned lecture or practice
      assignment[var] = value# assign a timeslot to it
      var._room = getRoom(csp,assignment, var, value) #get a room for it
      counter+=1
      if is_consistent(assignment, csp[CONSTRAINTS]):    
        break
      else: 
        assignment[var] = None
        var._room = None
  return FAILURE

def get_counter_default():
  global counter
  return counter


#simple search 
def default_heuristic(assignment):
  res = []
  for i in csp[VARIABLES]:
    if (assignment[i] is None): #choose  all classes which have not been assigned to a timeslot
      res.append(i)
  return res[random.randint(0, len(res)-1)]
