#include 'provided_files/Technovision.py'

CELL_ZERO = 0
CELL_ONE = 1
CELL_TWO = 2
CELL_THREE = 3
CELL_FOUR = 4

def isIn (list,studyProgram):
    for listCell in list:
        if listCell[CELL_ZERO]==studyProgram:
            return True
    return False

def insertStudyProgramVote (studyProgramsList, studyProgram):
    for listCell in studyProgramsList:
        if listCell[CELL_ZERO]==studyProgram:
            listCell[CELL_ONE]+=1


def inside_contest(faculty, file_name):
    file=open(file_name,'r')
    votersIdList=[]
    studyProgramsList=[]
    for line in file:
        listOfLine=line.split(' ')
        if listOfLine[CELL_ZERO]!="inside":
            continue
        elif listOfLine[CELL_ONE]!="contest":
            continue
        elif listOfLine[CELL_FOUR]!=faculty:
            continue
        elif listOfLine[CELL_TWO] in votersIdList:
            continue
        if isIn(studyProgramsList,listOfLine[CELL_THREE]):
            insertStudyProgramVote(studyProgramsList, listOfLine[CELL_THREE])
        else:
            studyProgramsList.append([listOfLine[CELL_THREE], 1])
        votersIdList.append(listOfLine[CELL_TWO])
    maxStudyProgramVotes=0
    maxStudyProgramName="NULL"
    for listCell in studyProgramsList:
        if listCell[1]>maxStudyProgramVotes:
            maxStudyProgramVotes=listCell[CELL_ONE]
            maxStudyProgramName=listCell[CELL_ZERO]
    if maxStudyProgramVotes==0:
        file.close()
        return "Error"
    file.close()
    return maxStudyProgramName







