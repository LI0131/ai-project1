import sys
import numpy as np
from model import DB_ROWS, get_row
from app import TARGET
from graphing import draw_scatter

SLOPE=0
INTERCEPT=0


def run():
    for name in DB_ROWS:
        row = get_row(name)
        feature_data, target_data = _scrub_data(row, get_row(TARGET))
        draw_scatter(name, target_data, feature_data)
        MSE = _mean_squared_error(
            len(feature_data), _compute_slope(len(target_data), feature_data, target_data),
            _compute_intercept(len(target_data), feature_data, target_data), 
            feature_data, target_data)
        print(MSE)


def _mean_squared_error(size, slope, intercept, feature, target):

    SLOPE = slope
    print(f'SLOPE: {SLOPE}')
    INTERCEPT = intercept
    print(f'INTERCEPT: {INTERCEPT}')

    if size <= 0:
        sys.exit('Size of sample must be greater than 0')

    total_sum = 0
    for i in range(size):
        difference = (SLOPE * target[i] + INTERCEPT) - feature[i]
        total_sum += difference**2
    return total_sum/size


def _compute_slope(size, feature, target):
    total_sum = 0
    for i in range(len(feature)):
        total_sum += -target[i] * (feature[i] - ((SLOPE * target[i]) + INTERCEPT))
    return (2/size) * total_sum


def _compute_intercept(size, feature, target):
    total_sum = 0
    for i in range(len(feature)):
        total_sum += -(feature[i] - ((SLOPE * target[i]) + INTERCEPT))
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
