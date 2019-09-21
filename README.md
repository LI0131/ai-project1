# CSCI 315 - Project 1 #

## Resources Used ##
https://towardsdatascience.com/introduction-to-machine-learning-algorithms-linear-regression-14c4e325882a
https://towardsdatascience.com/understanding-the-mathematics-behind-gradient-descent-dde5dc9be06e
https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html
https://scriptverse.academy/tutorials/python-matplotlib-plot-straight-line.html
https://medium.com/@Aj.Cheng/linear-regression-by-gradient-decent-bb198724eb2c
https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html

## Dev Setup ##
1. `pip install pipenv`
2. `pipenv install`

## Running This Project ##
This project has the ability to pull variables from the local environment of types `CSV_FILE`, `TARGET`, `LEARNING_RATE`, `ITERATIONS`, and `FEATURE`. If you would like to run one feature against the target variable set that variable using `export TARGET=your_variable`. This is great for quick testing of various learning rates and iterations.

To run this project with my defined learning rates and iterations, run `bash run.sh` from inside this directory. This will run through each feature vector, print output to the shell, and save graphs to the `/figures` directory. Read me about this in the section to follow.

## Graphing ##
Graph output can be found in the `/figures` directory. This directory contains subdirectories labeled by `{FEATURE}_{LEARNING_RATE}_{ITERATIONS}`

## Analysis ##
In this section I will discuss the purpose of each function in the `linear_regression.py` module. The other modules (`app.py`, `model.py`, and `graphing.py`) provide supporting roles to the linear_regression functionality. The app.py module starts the application and defines global constants, which are either defined in the local environment or within the script itself. It also initializes the database and runs the linear regression algorithm. The `model.py` class is responsible for converting the provided `.csv` file into rows in a sqlite database. The rows can be pulled individually using the get_row() function. The graphing.py module is used to draw the scatter plot of points -- of the form (feature value, target value) -- and to draw the line of best-fit as derived by the machine learning model.

Linear Regression is a statistical technique used to derive a predictive model for a dataset. This is done by computing, in this case, two predictive values m, and b (corrosponding to the slope and intercept of a line of the form y=mx+b), and then comparing those values against actual values to determine an amount of error. The error is then propogated back through the model in order to better hone the predictive values. 

We used Mean Squared Error as our metric. The equation y=mx+b is very important in understanding our calculation of Mean Squared Error. In this model, we created datapoints from our dataset by taking an x-variable from the target vector and a y-variable from the feature vector. This means our feature is plotted on the y-axis and our target is plotted on the x-axis. We know that slope and intercept are predicted values as determined by the model, and that ideally y=mx+b should hold. Therefore, we calculate mx+b using our predicted values and a variable x_i and subtract its value from it's corresponding y_i. This is done for all x_i and y_i in the sets x and y (target vector and feature vector). In order to avoid adding negative and positive amounts of error, the calculated y - mx+b is squared for each pair x_i, y_i. The total sum divided by the number of ordered pairs (x_i, y_i) is referred to as the Mean Squared Error.

I said in the beginning that Linear Regression is an iterative technique, and that we define a number of iterations in the app.py module. We use each iteration to improve upon the previous predicted values. We used the Gradient Descent Algorithm to improve upon our predictions on each successive iteration. The Gradient Descent Algorithm attempts to find a local minima in the error function by taking small steps determined by the defined learning rate and the slope of the error function at a given point. We determine this slope by computing the partial derivative of the error function (Mean Squared Error) with respect to b and the partial derivative with respect to m. This allows us to propagate our error back into the slope and intercept values using the learning rate. The learning rate multiplied by the computed partial derivative value gives the size step that should be taken for the slope and intercept values. The step is then applied by subtracting the step from and then updating the existing slope and intercept values. This process is then repeated for the defined number of iterations, over which the error function should reach its local minimum.

In my implementation, the updating process occurs in the `_gradient_descent()` function (which takes the feature vector, target vector, size of the sample, and the existing slope and intercept). The `_compute_slope()` and `_compute_intercept()` functions are used to take the partial derivative of the error function with respect to the slope and intercept respectively. These functions take the target vector, feature vector, existing slope, existing intercept, and size of the sample to make the calculation. The `_mean_squared_error()` function is used to compute the final error after all iterations of the gradient descent algorithm are run.

I also included the function `_scrub_data()` in my implementation. This function computes the standard deviation and mean for both the feature and target vectors and then removes any datapoints lying outside of 2.5 standard deviations from the mean of either the target or the feature. This removes potential outliers that might be lingering in the dataset.
 
