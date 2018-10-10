#!usr/bin/python
import webbrowser
#taking search input from user
search_input=raw_input(what do you want to search: ")
print "Plz Wait youtube is  about to open!!!!"
#adding two strings
z="https://www.youtube.com/results?search_query=",search_input
webbrowser.open_new_tab(z)
 import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import math
import pickle

## Data extraction from txt file

dataframe = pd.read_csv('CustomersData.txt')
dataframe.drop(['Address','Avatar', 'Email', 'Time on Website'], 1 , inplace = True)
# We drop the Time on Website as it has outliers and the gradient descent sometimes shoots up 
print(dataframe.shape)


## Separating the features and the Expected values
Input = dataframe.iloc[:, 0:3]
ones = np.ones( [Input.shape[0] , 1 ] )
Input = np.concatenate( (ones, Input), axis = 1)


Output = dataframe.iloc[:, 3:4].values

theta = np.zeros( [ 1, 4] )

# Learning rate alpha and iterations
alpha  = 0.0003
iters = 10000000

X_train , X_test, Y_train, Y_test = model_selection.train_test_split(Input, Output, test_size = 0.2)



def cost_function(X, Y, theta):
	tobesummed = np.power( ( (X @ theta.T) - Y ), 2 )
	return np.sum(tobesummed)/( 2*len(X) )


def gradient_descent( X, Y , theta, iters , alpha ):
	## This is not necessary this is just to plot the cost function values with each iter
	cost = np.zeros(iters)
	for i in range(iters):
		theta = theta - ( alpha/len(X)*2 )*( np.sum( X*( (X@theta.T) - Y), axis = 0) )
		cost[i] = cost_function(X,Y, theta)
	
	return theta , cost	

####### The following line will run the gradient descent and give the least cost value

Revised_theta, cost = gradient_descent(X_train , Y_train ,theta, iters, alpha)
print(Revised_theta)

### Here we save our Revised theta list into .pickle file
with open ('GradientDescent.pickle' , 'wb') as f:
	pickle.dump(Revised_theta, f)

finalCost = cost_function(X_train, Y_train , Revised_theta)
print(finalCost)

## Plotting the  cost function with each iteration to have a graphical idea of how our cost function is decreasing.
 
fig, ax = plt.subplots()
ax.plot( np.arange(iters) , cost , 'r')
ax.set_xlabel( 'Iterartions' )
ax.set_ylabel( 'COST' )
ax.set_title( ' Error vs Training Epoch' )
plt.show()
