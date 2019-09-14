from model import setup_db, get_rows

CSV_FILE = './data/housing.csv'

if __name__ == '__main__':
    setup_db(CSV_FILE)
    get_rows()