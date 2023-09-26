import math

def solveEquationDegree3(a,b,c):
    x1=0
    x2=0
    x3=0
    Delta=(-a)**2-3*1*b
    k=(9*1*(-a)*b-2*(-a)**3-27*1**2*(-c))/(2*math.sqrt(abs(Delta)**3))

    if Delta > 0 :
        if abs(k) <= 1 :
            x1=(2*math.sqrt(Delta)*math.cos(math.acos(k)/3)-(-a))/(3*1)
            x2=(2*math.sqrt(Delta)*math.cos(math.acos(k)/3-2*math.pi/3)-(-a))/(3*1)
            x3=(2*math.sqrt(Delta)*math.cos(math.acos(k)/3+2*math.pi/3)-(-a))/(3*1)
        else :
            x1=x2=x3=((math.sqrt(Delta)*abs(k))/(3*1*k))*((abs(k)+math.sqrt(k**2-1))**(1/3)+(abs(k)-math.sqrt(k**2-1))**(1/3))-(-a)/(3*1)

    if Delta == 0 :
        x1=x2=x3=(-(-a)+((-a)**3-27*1**2*(-c))**(1/3))/(3*1)

    if Delta < 0 :
        x1=x2=x3=((math.sqrt(abs(Delta)))/(3*1))*((k+math.sqrt(k**2+1))**(1/3)+(k-math.sqrt(k**2+1))**(1/3))-(-a)/(3*1)
    if x1 > x2 and x1 > x3:
        sigma_1 = x1
    elif x2 > x1 and x2 > x3:
        sigma_1 = x1
    else:
        sigma_1 = x3

    if sigma_1 == x1 and x2 > x3:
        sigma_2 = x2
        sigma_3 = x3
    elif sigma_1 == x1 and x3 > x2:
        sigma_2 = x3
        sigma_3 = x2
    elif sigma_1 == x2 and x1 > x3:
        sigma_2 = x1
        sigma_3 = x3
    elif sigma_1 == x2 and x3 > x1:
        sigma_2 = x3
        sigma_3 = x1
    elif sigma_1 == x3 and x1 > x2:
        sigma_2 = x1
        sigma_3 = x2
    elif sigma_1 == x3 and x2 > x1:
        sigma_2 = x2
        sigma_3 = x1
    return  sigma_1,sigma_2,sigma_3