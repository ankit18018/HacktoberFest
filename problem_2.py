import numpy as np
import math

def f(x):
    ans=[]
    temp=x[0][0]*2+x[2][0]2+x[1][0]*2
    ans.append([math.sqrt(temp)])
    temp=math.acos(x[2][0]/ans[0][0])
    ans.append([temp])
    temp=math.atan2(x[1][0],x[0][0])
    ans.append([temp])
    return ans

def J(x):

    return [[math.sin(x[1][0])*math.cos(x[2][0]),x[0][0]*math.cos(x[1][0])*math.cos(x[2][0]),-1*x[0][0]*math.sin(x[1][0])*math.sin(x[2][0])],
    [math.sin(x[1][0])*math.sin(x[2][0]),x[0][0]*math.cos(x[1][0])*math.sin(x[2][0]),x[0][0]*math.sin(x[1][0])*math.cos(x[2][0])],
    [math.cos(x[1][0]),-1*x[0][0]*math.sin(x[1][0]),0]]


def rel_ressi(a,b):
    return np.linalg.norm(a-b)/np.linalg.norm(b)

def carte(x):
  ans=[]
  ans.append(math.sin(x[1][0])*x[0][0]*math.cos(x[2][0]))
  ans.append(math.sin(x[1][0])*x[0][0]*math.sin(x[2][0]))
  ans.append(math.cos(x[1][0])*x[0][0])
  return ans
def cal_rel_resi(x,y):
  return rel_ressi(carte(x),y)

def new(f,J,x,act_x,tol=10**-12,maxit=100):
    iter=0
    while(iter<maxit and cal_rel_resi(x,act_x)>=tol ):
        Jx=np.array(J(x))
        fx=np.array(carte(x)-np.array(act_x))
        for i in fx:
          i[0]*=-1
        s=np.matmul(np.linalg.inv(Jx),fx)
        x=x+s
        iter+=1
        print("Iteration no.",iter,"error =", rel_ressi(carte(x),act_x))
    print("Final_residual=",rel_ressi(carte(x),act_x))
    return x
