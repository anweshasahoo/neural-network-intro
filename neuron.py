import numpy as np

def sigmoid(x):
    #activation function: f(x)=1/(1+e^(-x))
    return 1/(1+np.exp(-x))

class Neuron:
    def __init__(self,weights,bias):
         self.weights=weights
         self.bias=bias

    def feedforward(self,inputs):
        #weight inputs,add bias, then use activation function
        total = np.dot(self.weights, inputs)+ self.bias
        return sigmoid(total)

weights= np.array([0,1]) #w1=0, w2=1
bias=4
n= Neuron(weights,bias)

x=np.array([2,3])  #x1=2,x2=3
print(n.feedforward(x))   

class OurNeuralNetwork:
     # a neural netwokr with 2 inputs, a hidden layer with two neurons(h1,h2)
     # an output layer with 1 neuron (o1)

     #each neuron has same weights and biases. (w=[0,1], b=0)

     def __init__(self):
         weights= np.array([0,1])
         bias=0

         self.h1=Neuron(weights,bias)
         self.h2=Neuron(weights,bias)
         self.o1=Neuron(weights,bias)
     def feedforward(self,x):
         out_h1=self.h1.feedforward(x)
         out_h2=self.h2.feedforward(x)

         #inputs of o1 are the outputs from h1 and h2
         out_o1=self.o1.feedforward(np.array([out_h1,out_h2]))
         return out_o1
     
network=OurNeuralNetwork()
x=np.array([2,3])
print(network.feedforward(x))

