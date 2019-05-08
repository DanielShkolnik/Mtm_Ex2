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
        listOfLine=line.split(' ')
        if listOfLine[OPERATION] == "staff" and listOfLine[STAFF_FACULTY] == faculty:
            insertStudyProgramVote(studyProgramsList, listOfLine[STAFF_STUDY_PROGRAM], 20)
            continue
        if listOfLine[OPERATION] != "inside":
            continue
        elif listOfLine[FACULTY] != faculty:
            continue
        elif listOfLine[ID] in votersIdList:
            continue
        insertStudyProgramVote(studyProgramsList, listOfLine[STUDY_PROGRAM], 1)
        votersIdList.append(listOfLine[ID])
    file.close()
    maxStudyProgramVotes = 0
    maxStudyProgramName = ""
    for listCell in studyProgramsList:
        if listCell[1]>maxStudyProgramVotes:
            maxStudyProgramVotes = listCell[STUDY_PROGRAM_VOTES]
            maxStudyProgramName = listCell[STUDY_PROGRAM_NAME]
    if maxStudyProgramVotes == 0:
        return "Error"
    return maxStudyProgramName



Techniovision.TechniovisionWinningFaculty(techniovision)
Techniovision.TechniovisionDestroy(techniovision)
