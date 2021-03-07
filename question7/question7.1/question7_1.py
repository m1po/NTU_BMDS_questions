#contruct the derived formula
def find_index(L1,L2,x1,x2):
    if x2 in range(L2) and x1 in range(L1):
        index = x1 + x2 * L1
        return str(index)
    else:
        return 'out of range'

def find_cordinates(L1,L2,index):
    if index in range(L1*L2):
        x1 = index % L1
        x2 = int(index / L1)
        return str(x1)+'\t'+str(x2)
    else:
        return 'out of range'

#load in coordinates and write out index
f = open ('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question7/question7.1/input_coordinates_7_1.txt','r')
fw = open ('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question7/question7.1/output_index_7_1.txt','w')

lines = f.readlines()

for line in lines:
    line = line.strip()
    X = line.split('\t')
    try:
        fw.write(find_index(50,57,int(X[0]),int(X[-1]))+'\n')
    except:
        fw.write('index\n')

f.close()
fw.close()

#load in index and write out coordinates
f = open ('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question7/question7.1/input_index_7_1.txt','r')
fw = open ('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question7/question7.1/output_coordinates_7_1.txt','w')

lines = f.readlines()

for line in lines:
    line = line.strip()
    try:
        fw.write(find_cordinates(50,57,int(line))+'\n')
    except:
        fw.write('x1\tx2\n')

f.close()
fw.close()

print('done')
