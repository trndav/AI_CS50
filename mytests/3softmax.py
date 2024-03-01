# Softmax
# 1. exponentiate values
# 2. Normalization of values
# 3. Convert to numpy

# import math # Not needed anymore bc we use np.exp instead of math.e
import numpy as np
# import nnfs # To get values same as in tutorial book
# nnfs.init() # To get values same as in tutorial book
# layer_outputs = [4.8, 1.21, 2.385]
# Implement as a batch, not single vector
layer_outputs = [[4.8, 1.21, 2.385],
                 [8.9, -1.81, 0.2],
                 [1.41, 1.051, 0.026]]

# E = 2.71828182846 defined in math library
# E = math.e # Not needed anymore bc we use np.exp

# exp_values = []
# for output in layer_outputs:
#     exp_values.append(E**output)
# Shorter version:
exp_values = np.exp(layer_outputs)

# Exponentiated values
# print(exp_values)

# print(np.sum(layer_outputs, axis=0)) # Sum of columns
# print(np.sum(layer_outputs, axis=1, keepdims=True)) # Sum of rows, keepdims same dimensions

norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)

# norm_base = sum(exp_values)
# norm_values = []
# for value in exp_values:
#     norm_values.append(value / norm_base)
# Shorter version:
# norm_values = exp_values / np.sum(exp_values) # This is for single vector

# Normalized explonential values
print(norm_values)
'''print(sum(norm_values))'''