import  Techniovision


def inside_contest(faculty, file_name):
    file=open(file_name, 'r')


def add_vote(t,faculties,student,studentFaculty,votingProgram):

    for faculty in faculties:
        if faculty[1] == votingProgram:
            Techniovision.TechniovisionStudentVotes(t, int(student), str(studentFaculty), str(faculty[0]))




t = Techniovision.TechniovisionCreate()
faculties = []
file = open("input.txt")
for line in file:
    lineList = line.split()
    if lineList[0] == "staff":
        faculties.append([lineList[-1], ''])
file.close()

for faculty in faculties:
    faculty[1] = inside_contest(faculty[0])

ids = []
file = open("input.txt")
for line in file:
    lineList = line.split()
    if lineList[0] == "techniovision":
        if not (lineList[1] in ids):
            ids.append(lineList[1])
            add_vote(t,faculties,list[1],list[3],list[4])
file.close()

Techniovision.TechniovisionWinningFaculty(t)
Techniovision.TechniovisionDestroy(t)
