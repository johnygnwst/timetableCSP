from random import shuffle

from csp_init import *

csp = my_csp

counter = 0
var_domains = {}
degree_values = {}


# init empty assignment
def init_assignment_con(csp):
    global var_domains
    global counter
    counter = 0
    assignment = {}
    for var in csp[VARIABLES]:
        assignment[var] = None
        var_domains[var] = csp[DOMAINS].copy()
    return assignment


def getRoom(csp, assignment, var, value):
    rooms = data._rooms
    rooms.sort(key=lambda c: c[1])

    for r in rooms:
        if (r[1] >= var._number_of_students):
            free = True
            for k in csp[VARIABLES]:
                if (assignment[k] is not None and k._room is not None):
                    if (k._room[0] == r[0] and assignment[k] == value):
                        free = False
                        break
            if free:
                return r


def constraint_propagation(assignment, csp):
    global var_domains
    global counter
    rnd_domains_p = csp[DOMAINS][:]
    while True:
        if is_complete(assignment):
            return assignment
        var = select_unassigned_variable(csp[VARIABLES], assignment) #select random class assignment
        shuffle(rnd_domains_p)
        for value in rnd_domains_p: #for each timeslot

            if is_in_domain(var, value):# we check if the timeslot is  possible for this class
                assignment[var] = value #we assign it
                add_domains(assignment, csp, var)
                if check_for_zero(csp):
                    var._room = getRoom(csp, assignment, var, value)
                    counter += 1
                    if is_consistent(assignment, csp[CONSTRAINTS]):
                        break
                    else:
                        assignment[var] = None
                        var._room = None
                        undo(assignment, csp)
                else:
                    assignment[var] = None

    return FAILURE


def check_for_zero(csp):
    global var_domains

    for i in csp[VARIABLES]:
        r = False
        for j in var_domains[i]:
            if (j is not None):
                r = True
        if r == False:
            return False
    return True


def is_in_domain(var, value):
    global var_domains
    for d in var_domains[var]:# for every available timeslot  this class has
        if (d == value):#  we check if the value is
            return True
    return False


def add_domains(assignment, csp, var):
    global var_domains
    j = var
    for i in csp[VARIABLES]:# for each class
        if (assignment[i] is None): # if this class is not assigned yet
            if (not i == j):
                if (i._teacher == j._teacher): #if this class has the same teacher as the other
                    for k in range(len(var_domains[i])): # we check all available timeslots of the other class
                        if (var_domains[i][k] == assignment[j]):#and we make unavailable those thats have been assigned by this
                            var_domains[i][k] = None
                if (i._speciality == j._speciality):
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
                if (not i == j):
                    if (i._teacher == j._teacher):
                        for k in range(len(var_domains[i])):
                            if (var_domains[i][k] == assignment[j]):
                                var_domains[i][k] = None
                    if (i._speciality == j._speciality):
                        for k in range(len(var_domains[i])):
                            if (var_domains[i][k] == assignment[j]):
                                var_domains[i][k] = None



def get_counter_con():
    global counter
    return counter




  
       
