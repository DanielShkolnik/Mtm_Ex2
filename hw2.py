import Techniovision

STAFF_STUDY_PROGRAM = 2
STAFF_FACULTY = -1
STUDY_PROGRAM_NAME = 0
STUDY_PROGRAM_VOTES = 1
OPERATION = 0
ID = 2
STUDY_PROGRAM = 3
FACULTY = 4

def isIn (list, studyProgram):
    for listCell in list:
        if listCell[STUDY_PROGRAM_NAME] == studyProgram:
            return True
    return False

def insertStudyProgramVote (studyProgramsList, studyProgram, votes):
    if not isIn(studyProgramsList, studyProgram):
        studyProgramsList.append([studyProgram, votes])
        return None
    for listCell in studyProgramsList:
        if listCell[STUDY_PROGRAM_NAME] == studyProgram:
            listCell[STUDY_PROGRAM_VOTES] += votes


def inside_contest(faculty, file_name):
    file = open(file_name, 'r')
    votersIdList = []
    studyProgramsList = []
    for line in file:
        listOfLine=line.split()
        if listOfLine[OPERATION] == "staff" and listOfLine[STAFF_FACULTY] == faculty:
            insertStudyProgramVote(studyProgramsList, listOfLine[STAFF_STUDY_PROGRAM], 20)
            continue
        if listOfLine[OPERATION] == "inside" and listOfLine[FACULTY] == faculty\
                and not (listOfLine[ID] in votersIdList):
            insertStudyProgramVote(studyProgramsList, listOfLine[STUDY_PROGRAM], 1)
            votersIdList.append(listOfLine[ID])
    file.close()
    maxStudyProgramVotes = 0
    maxStudyProgramName = ""
    for listCell in studyProgramsList:
        if listCell[1] > maxStudyProgramVotes:
            maxStudyProgramVotes = listCell[STUDY_PROGRAM_VOTES]
            maxStudyProgramName = listCell[STUDY_PROGRAM_NAME]
    if maxStudyProgramVotes == 0:
        return "Error"
    return maxStudyProgramName


TECHNIOVISION_STUDENT = 1
TECHNIOVISION_VOTING_PROGRAM = 2
TECHNIOVISION_STUDENT_FACULTY = 3


def add_vote(t,faculties,student,studentFaculty,votingProgram):
    for faculty in faculties:
        if faculty[1] == votingProgram:
            Techniovision.TechniovisionStudentVotes(t, int(student), str(studentFaculty), str(faculty[0]))


techniovision = Techniovision.TechniovisionCreate()
faculties = []
file = open("input.txt")
for line in file:
    lineList = line.split()
    if lineList[0] == "staff":
        faculties.append([lineList[STAFF_FACULTY], ''])
file.close()


for faculty in faculties:
    faculty[1] = inside_contest(faculty[0], "input.txt")

ids = []
file = open("input.txt")
for line in file:
    lineList = line.split()
    if lineList[0] == "techniovision":
        if not (lineList[1] in ids):
            ids.append(lineList[TECHNIOVISION_STUDENT])
            add_vote(techniovision, faculties, lineList[TECHNIOVISION_STUDENT], lineList[TECHNIOVISION_STUDENT_FACULTY],
                     lineList[TECHNIOVISION_VOTING_PROGRAM])
file.close()

Techniovision.TechniovisionWinningFaculty(techniovision)
Techniovision.TechniovisionDestroy(techniovision)
