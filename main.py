from Determinant import *
from SolveEquationDegree3 import *
from SystemEquation import *
from SolveSystemEquation import *

print("Input tress tensor")
tensor = [[0 for x in range(3)] for y in range(3)]
for i in range(3):
    for j in range(3):
        print("epsilon_" + str(i + 1) + str(j + 1))
        tensor[i][j] = float(input())

det = det(tensor)
I1=tensor[0][0]+tensor[1][1]+tensor[2][2]
I2=(tensor[0][0]*tensor[1][1]-tensor[0][1]**2)+(tensor[1][1]*tensor[2][2]-tensor[1][2]**2)+(tensor[0][0]*tensor[2][2]-tensor[2][0]**2)
I3=det

[sigma_1,sigma_2,sigma_3] = solveEquationDegree3(I1,I2,I3)

print("Main Stress")
print("sigma_1",sigma_1)
print("sigma_2",sigma_2)
print("sigma_3",sigma_3)

system_equation_1 = systemEquation(tensor,sigma_1)
system_equation_2 = systemEquation(tensor,sigma_2)
system_equation_3 = systemEquation(tensor,sigma_3)

first_main_direction = solveSystemEquation(system_equation_1)
second_main_direction = solveSystemEquation(system_equation_2)
third_main_direction = solveSystemEquation(system_equation_3)

print("Main Direction")
print("The First Main Direction")
print(first_main_direction)
print("The Second Main Direction")
print(second_main_direction)
print("The Third Main Direction")
print(third_main_direction)