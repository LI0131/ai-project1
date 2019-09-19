import os
from model import setup_db
import linear_regression


CSV_FILE = os.environ.get('CSV_FILE', './data/housing.csv')
TARGET = os.environ.get('TARGET', 'median_home_value')
LEARNING_RATE = float(os.environ.get('LEARNING_RATE', '0.001'))
ITERATIONS = int(os.environ.get('ITERATIONS', '10000'))


if __name__ == '__main__':
    setup_db(CSV_FILE)
    linear_regression.run()