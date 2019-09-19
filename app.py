from model import setup_db
import linear_regression


CSV_FILE = './data/housing.csv'
TARGET = 'median_home_value'
LEARNING_RATE = 0.001
ITERATIONS = 10000


if __name__ == '__main__':
    setup_db(CSV_FILE)
    linear_regression.run()