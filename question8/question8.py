#coding=utf-8
import matplotlib.pyplot as plt

#build the function in 8.1
def E(e,s,es,p):
    de=(600+150)*es-100*e*s
    return de

def S(e,s,es,p):
    ds=-100*e*s+600*es
    return ds

def ES(e,s,es,p):
    des=-(600+150)*es+100*e*s
    return des
def P(e,s,es,p):
    dp=150*es
    return dp

#build fourth-order Runge-Kutta method
def  fourthorder_R_K(e,s,es,p,M):
    ee=[e]
    ss=[s]
    eses=[es]
    pp=[p]

    N =[0]
    h = 0.0001
    n = 0
    while n < M:

        n = n + h
        N.append(n)

        #first step
        E1=E(e,s,es,p)
        S1=S(e,s,es,p)
        ES1=ES(e,s,es,p)
        P1=P(e,s,es,p)
        #second step
        E2=E(e+E1*h/2,s+S1*h/2,es+ES1*h/2,p+P1*h/2)
        S2=S(e+E1*h/2,s+S1*h/2,es+ES1*h/2,p+P1*h/2)
        ES2=ES(e+E1*h/2,s+S1*h/2,es+ES1*h/2,p+P1*h/2)
        P2=P(e+E1*h/2,s+S1*h/2,es+ES1*h/2,p+P1*h/2)
        #third step
        E3=E(e+E2*h/2,s+S2*h/2,es+ES2*h/2,p+P2*h/2)
        S3=S(e+E2*h/2,s+S2*h/2,es+ES2*h/2,p+P2*h/2)
        ES3=ES(e+E2*h/2,s+S2*h/2,es+ES2*h/2,p+P2*h/2)
        P3=P(e+E2*h/2,s+S2*h/2,es+ES2*h/2,p+P2*h/2)
        #fourth step
        E4=E(e+E3*h,s+S3*h,es+ES3*h,p+P3*h)
        S4=S(e+E3*h,s+S3*h,es+ES3*h,p+P3*h)
        ES4=ES(e+E3*h,s+S3*h,es+ES3*h,p+P3*h)
        P4=P(e+E3*h,s+S3*h,es+ES3*h,p+P3*h)

        e=e+(E1+2*E2+2*E3+E4)*h/6
        s=s+(S1+2*S2+2*S3+S4)*h/6
        es=es+(ES1+2*ES2+2*ES3+ES4)*h/6
        p=p+(P1+2*P2+2*P3+P4)*h/6

        ee.append(e)
        ss.append(s)
        eses.append(es)
        pp.append(p)
    return (N,ee,ss,eses,pp)

p = fourthorder_R_K(1,10,0,0,0.3)

##search the quantity of each substanceat at time t min
#def find_value(t):
#    for i in range (len(p[0])):
#        if t <= p[0][i]:
#            return p[1][i],p[2][i],p[3][i],p[4][i]
#print(find_value(0.1))

#plot result of 8.1
plt.plot(p[0],p[1],label = 'E')
plt.plot(p[0],p[2],label = 'S')
plt.plot(p[0],p[3],label = 'ES')
plt.plot(p[0],p[4],label = 'P')
plt.legend()
plt.xlabel('time in min')
plt.savefig('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question8/fig_8_2.pdf')
plt.close()

V=[]
#calculate V
for i in range(len(p[0])-1):
    V.append((p[4][i+1] - p[4][i])/0.0001)
#find responding S
S=p[2]
del(S[-1])

plt.plot(S,V)
plt.plot(S[V.index(max(V))],max(V),'ro')
plt.text(S[V.index(max(V))]-4,max(V)+3,(S[V.index(max(V))],max(V)),color='r')
plt.xlabel('S')
plt.ylabel('V')
plt.savefig('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question8/fig_8_3.pdf')
plt.close()
print('done')
