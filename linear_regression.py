import sys
import numpy as np
from model import get_row
from app import TARGET, LEARNING_RATE, ITERATIONS
from graphing import draw_scatter

def run(row, name):
    slope = 0
    intercept = 0
    error_list = []
    feature_data, target_data = _scrub_data(row, get_row(TARGET)) if name != 'river_var' else (row, get_row(TARGET))

    for i in range(ITERATIONS):
        slope, intercept = _gradient_descent(float(len(feature_data)), feature_data, target_data, slope, intercept)
        error = _mean_squared_error(float(len(feature_data)), feature_data, target_data, slope, intercept)
        error_list.append(error)
    print(f'ERROR: {error}\n NAME: {name}')
    draw_scatter(name, target_data, feature_data, slope, intercept)

def _gradient_descent(size, feature, target, slope, intercept):
    # update the new slope and intercept using the learning rate

    if size <= 0:
        sys.exit('Size of sample must be greater than 0')

    new_slope = slope - (LEARNING_RATE * _compute_slope(size, feature, target, slope, intercept))
    new_intercept = intercept - (LEARNING_RATE * _compute_intercept(size, feature, target, slope, intercept))
    return new_slope, new_intercept


def _mean_squared_error(size, feature, target, slope, intercept):
    # compute the error for the final slope and intercept (computed as sum)

    if size <= 0:
        sys.exit('Size of sample must be greater than 0')

    total_sum = 0
    for i in range(len(feature)):
        difference = (slope * target[i] + intercept) - feature[i]
        total_sum += difference**2
    return total_sum/size


def _compute_slope(size, feature, target, slope, intercept):
    # use partial derivative wrt slope to update slope
    total_sum = 0
    for i in range(len(feature)):
        total_sum += -target[i] * (feature[i] - ((slope * target[i]) + intercept))
    return (2/size) * total_sum


def _compute_intercept(size, feature, target, slope, intercept):
    # use partial derivative wrt intercept to update intercept
    total_sum = 0
    for i in range(len(feature)):
        total_sum += -(feature[i] - ((slope * target[i]) + intercept))
    return (2/size) * total_sum


def _scrub_data(feature, target):
    # if data is outside of 2.5 std. dev. throw it out
    ordered_pairs = [(x, y) for x, y in zip(feature, target)]
    feature_std_dev = np.std(feature)
    feature_mean = np.mean(feature)
    target_std_dev = np.std(target)
    target_mean = np.mean(target)
    
    # define scrubbed data
    scrubbed_feature = []
    scrubbed_target = []

    for x, y in ordered_pairs:
        if ((x >= (feature_mean - (feature_std_dev * 2.5)) and x <= (feature_mean + (feature_std_dev * 2.5))) and 
           (y >= (target_mean - (target_std_dev * 2.5)) and y <= (target_mean + (target_std_dev * 2.5)))):
            scrubbed_feature.append(x)
            scrubbed_target.append(y)

    return scrubbed_feature, scrubbed_target
