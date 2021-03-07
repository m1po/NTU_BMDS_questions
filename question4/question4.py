import pandas as pd

matrix = pd.read_csv('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question4/input_question_4', sep='\t',header=None)
#add one top row and one left column as background to save the work in iteration later
matrix.insert(0,-1,0)
matrix.loc[-1] = 0
matrix = matrix.sort_index()

#set intial label and equivalent numbers
label = 1
eq = [(0,0)]
for i in range(1,matrix.shape[0]):
    for j in range(1,matrix.shape[1]):
        if matrix.iloc[i,j] == 0:
            continue
        #using 4-connectivity
        nbr = (matrix.iloc[i-1,j],matrix.iloc[i,j-1])
        if nbr == (0,0):
            matrix.iloc[i,j] = label
            label = label + 1
        elif nbr[0] == 0 and nbr[1] != 0:
            matrix.iloc[i,j] = nbr[1]
        elif nbr[0] != 0 and nbr[1] == 0:
            matrix.iloc[i,j] = nbr[0]
        elif nbr[0] == nbr[1] and nbr[0] != 0:
            matrix.iloc[i,j] = nbr[0]
        else:
            matrix.iloc[i,j] = nbr[0]
            #collect equivalent numbers
            if nbr[0] in eq[-1]:
                eq[-1] = eq[-1] +(nbr[1],)
            elif nbr[1] in eq[-1]:
                eq[-1] = eq[-1] +(nbr[0],)
            else:
                eq.append(nbr)

matrix=matrix.drop([-1])
matrix=matrix.drop([-1],axis = 1)

#set equivalent points into their representative number
for k in eq:
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix.iloc[i,j] in k:
                matrix.iloc[i,j] = k[0]

matrix.to_csv('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question4/output_question_4',sep='\t',header = 0, index = 0)
print('done')
