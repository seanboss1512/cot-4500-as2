
import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)
x=[3.6,3.8,3.9]
y=[1.675,1.436,1.318]
x_input= 3.7
q=[7.2,7.4,7.5,7.6]
w=[23.5492,25.3913,26.8224,27.4589]
value=7.3
def neville(x,y,x_input):
    calculated_matrix= np.zeros([len(x),len(x)])
    for i in range(len(x)):
        calculated_matrix[i][0]= y[i]
    for i in range(1,len(x)):
        for o in range(1,len(x)):
            numer = (x_input-x[i-o])*calculated_matrix[i][o-1]-(x_input-x[i])*calculated_matrix[i-1][o-1]
            denom= x[i]-x[i-1]
            result= numer/denom
            calculated_matrix[i][o]=result
    print(calculated_matrix[1][1])
print(neville(x,y,x_input),"\n", end="[")
def divided_table(q,w):
    divided_matrix=np.zeros([len(q),len(w)])
    for i in range(len(q)):
        divided_matrix[i][0]=w[i]
    for i in range(1,len(q)):
        for o in range(1,len(q)):
            divided_matrix[i][o]=(divided_matrix[i][o-1]-divided_matrix[i-1][o-1])/(q[i]-q[i-o])
    print(divided_matrix[1][1],divided_matrix[2][2],divided_matrix[3][3], sep=", ", end="]\n")
    
    return(divided_matrix)

divided_matrix= divided_table(q,w)
def get_approximate_result(divided_matrix, q, value):
    x_span = 1
    px_result = 23.5492

    for i in range(1,len(divided_matrix)):
        for j in range(1,len(divided_matrix)):
            if (i==j):
                coeff = divided_matrix[i][j]
        x_span *= (value - q[i-1])
        multiply = coeff * x_span
        px_result += multiply
    

    print(px_result)
def hermite_interpolation():
    slopes = [-1.195, -1.188, -1.182]
    num_of_points = len(x)
    hermite = np.zeros((2*num_of_points,2*num_of_points))
    for i in range(0,3):
        hermite[2*i][0]= x[i]
        hermite[2*i+1][0]= x[i]

    for i in range(0,3):
        hermite[2*i][1]=y[i]
        hermite[2*i+1][1]= y[i]
            
            
    
    for i in range (0,3):
        hermite[2*i+1][2]= slopes[i]
       
get_approximate_result(divided_matrix,q,value)
