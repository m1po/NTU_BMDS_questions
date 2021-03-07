import pandas as pd
#load in polygon
#here, we assume the polygon is draw by the order of given vertex, otherwise it will be more complex to be concave
polygon = pd.read_csv('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question6/input_question_6_polygon.txt',sep=' ',header=None)
X = polygon[0].tolist()
Y = polygon[1].tolist()
#load in points
p = pd.read_csv('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question6/input_question_6_points.txt',sep=' ',header=None)
x = p[0].tolist()
y = p[1].tolist()

f = open ('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question6/output_question_6','w')

def inpolygon(i):
    det=[]
    for j in range(len(X)-1):
        #calculate determinant
        det.append((X[j]-x[i])*(Y[j+1]-y[i])-(X[j+1]-x[i])*(Y[j]-y[i]))
    #find the sign
    for k in range(len(det)):
        if det[k]>0:
            det[k]=1
        elif det[k] == 0:
            return str(x[i])+' '+str(y[i])+' inside'
        else:
            det[k]=-1

    if len(set(det)) == 1:
        return str(x[i])+' '+str(y[i])+' inside'
    else:
        return str(x[i])+' '+str(y[i])+' outside'

for i in range(len(x)):
    f.write(inpolygon(i)+'\n')

f.close()
print('done')
