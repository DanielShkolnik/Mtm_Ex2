import  Techniovision



STUDY_PROGRAM_NAME = 0
STUDY_PROGRAM_VOTES = 1
OPERATION1 = 0
OPERATION2 = 1
ID = 2
STUDY_PROGRAM = 3
FACULTY = 4

def isIn (list,studyProgram):
    for listCell in list:
        if listCell[STUDY_PROGRAM_NAME]==studyProgram:
            return True
    return False

def insertStudyProgramVote (studyProgramsList, studyProgram):
    for listCell in studyProgramsList:
        if listCell[STUDY_PROGRAM_NAME]==studyProgram:
            listCell[STUDY_PROGRAM_VOTES]+=1


def inside_contest(faculty, file_name):
    file = open(file_name,'r')
    votersIdList = []
    studyProgramsList = []
    for line in file:
        listOfLine=line.split(' ')
        if listOfLine[OPERATION1]!="inside":
            continue
        elif listOfLine[OPERATION2]!="contest":
            continue
        elif listOfLine[FACULTY]!=faculty:
            continue
        elif listOfLine[ID] in votersIdList:
            continue
        if isIn(studyProgramsList,listOfLine[STUDY_PROGRAM]):
            insertStudyProgramVote(studyProgramsList, listOfLine[STUDY_PROGRAM])
        else:
            studyProgramsList.append([listOfLine[STUDY_PROGRAM], 1])
        votersIdList.append(listOfLine[ID])
    maxStudyProgramVotes=0
    maxStudyProgramName="NULL"
    for listCell in studyProgramsList:
        if listCell[1]>maxStudyProgramVotes:
            maxStudyProgramVotes=listCell[STUDY_PROGRAM_VOTES]
            maxStudyProgramName=listCell[STUDY_PROGRAM_NAME]
    if maxStudyProgramVotes==0:
        file.close()
        return "Error"
    file.close()
    return maxStudyProgramName





Techniovision.TechniovisionWinningFaculty(techniovision)
Techniovision.TechniovisionDestroy(techniovision)
