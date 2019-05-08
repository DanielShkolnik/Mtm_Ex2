import  Techniovision


CELL_ZERO = 0
CELL_ONE = 1
CELL_TWO = 2
CELL_THREE = 3
CELL_FOUR = 4

def isIn (list,studyProgram):
    for listCell in list:
        if listCell[CELL_ZERO] == studyProgram:
            return True
    return False

def insertStudyProgramVote (studyProgramsList, studyProgram):
    for listCell in studyProgramsList:
        if listCell[CELL_ZERO] == studyProgram:
            listCell[CELL_ONE] += 1


def inside_contest(faculty, file_name):
    file = open(file_name,'r')
    votersIdList = []
    studyProgramsList = []
    for line in file:
        listOfLine = line.split(' ')
        if listOfLine[CELL_ZERO] != "inside":
            continue
        elif listOfLine[CELL_ONE] != "contest":
            continue
        elif listOfLine[CELL_FOUR] != faculty:
            continue
        elif listOfLine[CELL_TWO] in votersIdList:
            continue
        if isIn(studyProgramsList,listOfLine[CELL_THREE]):
            insertStudyProgramVote(studyProgramsList, listOfLine[CELL_THREE])
        else:
            studyProgramsList.append([listOfLine[CELL_THREE], 1])
        votersIdList.append(listOfLine[CELL_TWO])

    maxStudyProgramVotes = 0
    maxStudyProgramName = ""
    for listCell in studyProgramsList:
        if listCell[1] > maxStudyProgramVotes:
            maxStudyProgramVotes=listCell[CELL_ONE]
            maxStudyProgramName=listCell[CELL_ZERO]

    file.close()
    if maxStudyProgramVotes == 0:
        return "Error"
    return maxStudyProgramName









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
            add_vote(t, faculties, list[1], list[3], list[4])
file.close()

Techniovision.TechniovisionWinningFaculty(t)
Techniovision.TechniovisionDestroy(t)
