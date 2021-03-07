#contruct the derived formula
def find_index(L1,L2,L3,L4,L5,L6,x1,x2,x3,x4,x5,x6):
    if x1 in range(L1) and x2 in range(L2) and x3 in range(L3) and x4 in range(L4) and x5 in range(L5) and x6 in range(L6):
        index = x1 + x2*L1 + x3*L1*L2 + x4*L1*L2*L3 + x5*L1*L2*L3*L4 +x6*L1*L2*L3*L4*L5
        return str(index)
    else:
        return 'out of range'

def find_cordinates(L1,L2,L3,L4,L5,L6,index):
    if index in range(L1*L2*L3*L4*L5*L6):
        left_toadd = index
        X=[]
        L=[L1,L2,L3,L4,L5,L6]

        for x in reversed(range(6)):
            div = 1
            for i in range(x):
                div = div * L[i]

            x = int(left_toadd / div)
            X.append(x)
            rem = left_toadd % div
            left_toadd = rem
        return str(X[5])+'\t'+str(X[4])+'\t'+str(X[3])+'\t'+str(X[2])+'\t'+str(X[1])+'\t'+str(X[0])
    else:
        return 'out of range'

#load in coordinates and write out index
f = open ('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question7/question7.2/input_coordinates_7_2.txt','r')
fw = open ('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question7/question7.2/output_index_7_2.txt','w')

lines = f.readlines()

for line in lines:
    line = line.strip()
    X = line.split('\t')
    try:
        fw.write(find_index(4,8,5,9,6,7,int(X[0]),int(X[1]),int(X[2]),int(X[3]),int(X[4]),int(X[5]))+'\n')
    except:
        fw.write('index\n')

f.close()
fw.close()

#load in index and write out coordinates
f = open ('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question7/question7.2/input_index_7_2.txt','r')
fw = open ('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question7/question7.2/output_coordinates_7_2.txt','w')

lines = f.readlines()

for line in lines:
    line = line.strip()
    try:
        fw.write(find_cordinates(4,8,5,9,6,7,int(line))+'\n')
    except:
        fw.write('x1\tx2\tx3\tx4\tx5\tx6\n')

f.close()
fw.close()

print('done')
