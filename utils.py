
import numpy as np

def ReadPL(text = None):

# expected input:
  '''

  3 3       -> n_restrictions and n_variables
  2 4 8     -> c_vector
  1 0 0 1  \
  0 1 0 1   -> restrictions
  0 0 1 1  /

  PL in FPI (standart form)

  [2 4 8] x
  [1 0 0        [1
   0 1 0  * x =  1  
   0 0 1]        1]

  '''
  ## Get number of retrictions and variables as ints
  _restrictions_and_variables = input(text)
  _n_restrictions, n_variables = [int(value) for value in _restrictions_and_variables.split(' ')]
  restrictions = []

  ## Read and fill c_array
  c_aux = [float(value) for value in input().split(' ')]
  c_array = np.array(c_aux)
  
  restrictions_aux = []
  restrictions_and_b = []
  b_aux = []
  ## Read and Fill restrictions(A) and b
  for i in range(_n_restrictions):
    restrictions_and_b.append([float(value) for value in input().split(' ')])
    restrictions_aux.append(restrictions_and_b[i][:-1])
    b_aux.append(restrictions_and_b[i][-1])
  restrictions = np.array(restrictions_aux)
  b_array = np.array(b_aux)

  
  return c_array, restrictions, b_array