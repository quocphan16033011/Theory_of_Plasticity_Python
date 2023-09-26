def systemEquation(tensor,sigma):
    system_equation_1 = [tensor[0][0] - sigma, tensor[0][1], tensor[0][2]]
    system_equation_2 = [tensor[1][0], tensor[1][1] - sigma, tensor[1][2]]
    system_equation_3 = [tensor[2][0], tensor[2][1], tensor[2][2] - sigma]
    
    return [system_equation_1,system_equation_2,system_equation_3]