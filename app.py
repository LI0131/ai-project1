import os
from model import setup_db, DB_ROWS, get_row
import linear_regression
import graphing


CSV_FILE = os.environ.get('CSV_FILE', './data/housing.csv')
TARGET = os.environ.get('TARGET', 'median_home_value')
LEARNING_RATE = float(os.environ.get('LEARNING_RATE', '0.001'))
ITERATIONS = int(os.environ.get('ITERATIONS', '10000'))


if __name__ == '__main__':
    setup_db(CSV_FILE)
    feature = os.getenv('FEATURE')
    if feature:
        graphing.draw_scatter(feature, get_row(TARGET), get_row(feature), None, None, 'start', showLine=False)
        linear_regression.run(get_row(feature), feature)
    else:
        for name in DB_ROWS:
            graphing.draw_scatter(name, get_row(TARGET), get_row(name), None, None, 'start', showLine=False)
            linear_regression.run(get_row(name), name)
