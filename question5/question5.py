###first, 2 colors situation, when the number of each color is half of the grid or mid 2 numebrs when the grid is odd
###then, the grid can be filled in without panelty by arrange them one by one RDRDRD...
###5.1 fits this condition
###for 5.2, we can group R, B and Y as one color, and G and W as one color
###then (RBY) has 139+1451+457 = 2047 beads and (GW) has 977+1072 = 2049 beads
###so, arrange them in 2 colors way, panelty only comes from last 2 (GW) and another (GW) above them
###then, we can easily rearrange G and W to avoid panelty
###Hence, 5.1 and 5.2 both can reach no panelty
###Reversely, we first assign the superfluous color. When color beads remian the same,they can be easily arranged

import pandas as pd

def grid_configuration(L,dic):
    #construct grid with one more row and column to save the later interation work
    grid = pd.DataFrame(columns=[i for i in range(L+1)])
    for i in range(L+1):
        grid.loc[i] = 1

    for i in range(1,grid.shape[0]):
        for j in range(1,grid.shape[1]):
            nbr = (grid.iloc[i-1,j],grid.iloc[i,j-1])
            #choose color with most beads and avoid panelty
            n = 0
            color = sorted(dic, key=dic.get, reverse=True)[n]
            while color in nbr:
                n = n + 1
                if n >= len(dic):
                    color = sorted(dic, key=dic.get, reverse=True)[0]
                    break
                color = sorted(dic, key=dic.get, reverse=True)[n]

            dic[color] = dic[color] - 1
            if dic[color] == 0:
                del dic[color]
            grid.iloc[i,j] = color

    grid=grid.drop([0])
    grid=grid.drop([0],axis = 1)
    return grid

dic = {}
dic['R']=11
dic['B']=14
grid_configuration(5,dic).to_csv('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question5/output_question_5_1',sep='\t',header = 0, index = 0)

dic = {}
dic['R']= 139
dic['B']= 1451
dic['G']= 977
dic['W']= 1072
dic['Y']= 457
grid_configuration(64,dic).to_csv('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question5/output_question_5_2',sep='\t',header = 0, index = 0)
print('done')
