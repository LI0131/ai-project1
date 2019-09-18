import pandas
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)


DB_ROWS = [
    'crime_rate', 'zoned_over_25000', 'business_acres', 'river_var', 'nitric_oxide',
    'rooms_per_home', 'built_prior_1940', 'distance_to_centers', 'highway_availability',
    'property_tax', 'student_teacher_ratio', 'ethicity_demo', 'percent_lower_status',
    'median_home_value'
]


def setup_db(data):
    df = pandas.read_csv(data, delim_whitespace=True, usecols=DB_ROWS)
    df.to_sql('housing', con=engine, if_exists='append', index=False)


def get_row(row):
    row = engine.execute(f'SELECT {row} FROM housing').fetchall()
    return [datapoint.items()[0][1] for datapoint in row]
