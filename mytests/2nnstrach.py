# https://www.youtube.com/watch?v=gmjzbpSVY1A&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=5
# https://www.youtube.com/watch?v=omz_NdFgWyU&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=6

# RELU Activation function
import numpy as np
import nnfs
from nnfs.datasets import spiral_data

# np.random.seed(0)

nnfs.init()

X = [[1, 2, 3, 2.5],
     [2, 5, -1, 2],
     [-1.5, 2.7, 3.3, -0.8]]

X, y = spiral_data(100, 3)

# inputs = [0, 20 -1, 3.3, -2.7, 1.1, 2.2, -100]
# output = []

# for i in inputs:
#     output.append(max, i)

# print(output)

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
class Activation_ReLu:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

layer1 = Layer_Dense(2,5) # Number of inputs, number of neurons
# layer2 = Layer_Dense(5,2)
activation1 = Activation_ReLu()

layer1.forward(X)
print(layer1.output)
print("************")
# layer2.forward(layer1.output)
# print(layer2.output)
print(layer1.output)
activation1.forward(layer1.output)
print(activation1.output)