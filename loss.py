import numpy as np

def mse_loss(y_true,y_pred):
    #y_true and y_pred are numpy arrays of the same length.
    return ((y_true-y_pred)**2).mean()

y_true = np.array([1,0,0,1])
y_pred = np.array([0,0,0,0])

print(mse_loss(y_true,y_pred))