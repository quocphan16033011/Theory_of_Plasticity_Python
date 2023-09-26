import math
def solveSystemEquation(system_equation):
    system_equation_delete_3 = [[0,0],[0,0]]
    for i in range(len(system_equation)):
        for j in range(len(system_equation)):
            if (i==0 and j!=2):
                system_equation_delete_3[i][j]=system_equation[i][j]*(-system_equation[1][2])
            elif (i==1 and j!=2):
                system_equation_delete_3[i][j]=system_equation[i][j]*system_equation[0][2]
    plus_2_system = [0,0]
    plus_2_system[0] = system_equation_delete_3[0][0]+system_equation_delete_3[1][0]
    plus_2_system[1] = system_equation_delete_3[0][1]+system_equation_delete_3[1][1]
    n_1_follow_2=-plus_2_system[1]/plus_2_system[0]
    n_3_follow_2=-(system_equation[1][0]*n_1_follow_2+system_equation[1][1])/system_equation[1][2]
    n_2=math.sqrt(1/(n_1_follow_2**2+1+n_3_follow_2**2))
    n_2_op=-n_2
    n_1=n_2*n_1_follow_2
    n_1_op=-n_1
    n_3=n_2*n_3_follow_2
    n_3_op=-n_3
    return [[n_1,n_2,n_3],[n_1_op,n_2_op,n_3_op]]