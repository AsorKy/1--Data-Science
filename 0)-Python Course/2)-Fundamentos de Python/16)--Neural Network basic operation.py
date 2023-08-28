"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Basic Neural Network operation
FILE TYPE   : Basic Neural Network operation
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#//////////////// Python Program Basic Neural Network operation ////////////////
#//////////////// Python Program Basic Neural Network operation ////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#EXERCISE:
# Write a function neural_network, which will apply a neural network operation 
# with 2 inputs and 1 output and a given weight matrix.
#///////////////////////////////////////////


#///////////////////////////////////////////
#User Inputs
#///////////////////////////////////////////

I = np.random.random([2,1])
W = np.random.random([2,1])

def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    #Your code here
    inputs = np.array(inputs)
    weights = np.array(weights)
    dot = np.matmul(weights.transpose(),inputs)
    z = np.tanh(dot)
    return z

print(neural_network(W, I))

