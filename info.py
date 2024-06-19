
ROOMS = [["A1", 25],
         ["B2", 26],
         ["C3", 30],
         ["D4", 30],
         ["E5", 25],
         ["F6", 26],
         ["G7", 30],
        # ["H8", 30],
        # ["I9", 15],
        # ["J10", 30],
        # ["K11", 20],
        # ["L12", 25]
        # ["M13", 26],
        # ["N14", 20],
        # ["O15", 30]


         ]

MEETING_TIMES = [
                 "09:00 - 11:00",
                 "11:00 - 13:00",
                 "13:00 - 15:00",
                 "15:00 - 17:00",
                 "17:00 - 19:00",
                 "19:00 - 21:00"]
DAYS = ["Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"]

INSTRUCTORS = [["James Web"],
                  ["Mike Brown"],
                  ["Steve Day"],
                   ["George Miller"],
                   ["Lily Johns"],
                   ["Jannifer Dickens"],
                   ["Jane Doe"],
                   ["Andrew Lively"],
                   ["John Drake"],
                   ["Mila Kasper"],
                  ["Katherine Balvin"],
                   ["Stamatia Papa"],
                   ["Austin Day"],
                  ["Helena Kosta"],
                  ["Eirini Best"]
                                  ]

SUBJ_TEACH = {"Algorithms": ["James Web","Stamatia Papa","John Drake"],
              "Database" : ["Lily Johns","Katherine Balvin","John Drake"],
              "Cloud Computing": ["Katherine Balvin","James Web","John Drake"],
              "Web Development": ["Lily Johns","James Web","Katherine Balvin"],
              "Application Engineering": ["Lily Johns","Stamatia Papa","John Drake"],
              "Data Science": ["Stamatia Papa","Lily Johns","Katherine Balvin"],
              "Business Intelligence": ["John Drake","Stamatia Papa","Katherine Balvin"],
              "JAVA": ["John Drake","James Web","Lily Johns"],
              "Python": ["Stamatia Papa", "James Web","John Drake"],
              "C++": ["John Drake","Lily Johns","Stamatia Papa"],
              "Mathematics 2": ["Katherine Balvin","Stamatia Papa","James Web"],
              "Matlab": ["John Drake","Katherine Balvin","Stamatia Papa"],
              "SQL": ["Katherine Balvin", "John Drake","Stamatia Papa"],
              "Javascript": ["John Drake","Stamatia Papa","Lily Johns"],
              "HTML": ["James Web","John Drake","Lily Johns"],
              "Mathematics 3": ["Lily Johns", "Stamatia Papa", "James Web"],
              "Matlab 2 (Epilogis)": ["James Web", "Stamatia Papa", "Katherine Balvin"],
              "SQL 2": ["James Web","Stamatia Papa", "Katherine Balvin"],
              "Javascript 2 (Epilogis)": ["Stamatia Papa","James Web","Lily Johns"],
              "HTML 2 (Epilogis)": ["James Web","Katherine Balvin","Lily Johns"],
              "Algorithms 2": ["Eirini Best", "Lily Johns","John Drake"],
              "Database 2 (Epilogis)": ["Eirini Best", "Lily Johns", "Stamatia Papa"],
              "Cloud Computing 2 (Epilogis)": ["Katherine Balvin","Stamatia Papa", "Lily Johns"],
              "Web Development 2": ["James Web", "Eirini Best","John Drake"],
              "Application Eng. 2 (Epilogis)": ["Eirini Best", "Lily Johns", "Stamatia Papa"],
              "Algorithms 3": ["James Web", "Eirini Best","Stamatia Papa"],
              "Database 3 (Epilogis)": ["Stamatia Papa", "John Drake", "Katherine Balvin"],
              "Cloud Com. 3 (Epilogis)": ["John Drake", "James Web", "Katherine Balvin"],
              "Web Development 3": ["John Drake", "Katherine Balvin", "James Web"],
              "Application Eng. 3 (Epilogis)": ["James Web", "Stamatia Papa","Lily Johns"]}








#LABS
SUBJECTS = [{"name": "Algorithms", "number_of_students": 30, "groups": 0},
            {"name": "Database", "number_of_students": 19, "groups": 0},
            {"name": "Cloud Computing", "number_of_students": 30, "groups": 2},
            {"name": "Web Development", "number_of_students": 30, "groups": 0},
            {"name": "Application Engineering", "number_of_students": 25, "groups": 2},
            {"name": "Data Science", "number_of_students": 25, "groups": 0},
            {"name": "Business Intelligence", "number_of_students": 30, "groups": 2},
            {"name": "JAVA", "number_of_students": 22, "groups": 0},
            {"name": "Python", "number_of_students": 26, "groups": 2},
            {"name": "C++", "number_of_students": 30, "groups": 2},
            {"name": "Mathematics 2", "number_of_students": 30, "groups": 0},
            {"name": "Matlab", "number_of_students": 26, "groups": 2},
            {"name": "SQL", "number_of_students": 15, "groups": 0},
            {"name": "Javascript", "number_of_students": 20, "groups": 2},
            {"name": "HTML", "number_of_students": 30, "groups": 2},
            {"name": "Mathematics 3", "number_of_students": 30, "groups": 0},
            {"name": "Matlab 2 (Epilogis)", "number_of_students": 26, "groups": 2},
            {"name": "SQL 2", "number_of_students": 15, "groups": 2},
            {"name": "Javascript 2 (Epilogis)", "number_of_students": 30, "groups": 2},
            {"name": "HTML 2 (Epilogis)", "number_of_students": 30, "groups": 2},
            {"name": "Algorithms 2", "number_of_students": 30, "groups": 0},
            {"name": "Database 2 (Epilogis)", "number_of_students": 30, "groups": 0},
            {"name": "Cloud Computing 2 (Epilogis)", "number_of_students": 20, "groups": 0},
            {"name": "Web Development 2", "number_of_students": 30, "groups": 0},
            {"name": "Application Eng. 2 (Epilogis)", "number_of_students": 30, "groups": 0},
            {"name": "Algorithms 3", "number_of_students": 30, "groups": 0},
            {"name": "Database 3 (Epilogis)", "number_of_students": 30, "groups": 0},
            {"name": "Cloud Com. 3 (Epilogis)", "number_of_students": 20, "groups": 0},
            {"name": "Web Development 3", "number_of_students": 30, "groups": 2},
            {"name": "Application Eng. 3 (Epilogis)", "number_of_students": 30, "groups": 0}]

#1 lecture + groups=times it appears to schedule
SPECIALITIES = [
    {"name": "1st year", "subjects": ["Algorithms","Algorithms","Business Intelligence","Matlab","Application Engineering","Application Engineering"]},
    {"name": "2nd year", "subjects": ["Algorithms 2","Python","Cloud Computing","Cloud Computing","HTML","Application Eng. 2 (Epilogis)","Cloud Computing 2 (Epilogis)"]},
    {"name": "3rd year", "subjects": ["Mathematics 2","Mathematics 2","Algorithms 3","Algorithms 3","SQL","Web Development 3"]},
    {"name": "4th year","subjects": ["Database","C++","Javascript","Matlab 2 (Epilogis)","Cloud Com. 3 (Epilogis)","Data Science"]},
    {"name": "5th year","subjects": ["SQL 2","Mathematics 3","Javascript 2 (Epilogis)","HTML 2 (Epilogis)","Database 3 (Epilogis)"]}
]






                 
