import pandas as pd
import new_lib as nl
from datetime import datetime
def wrangle_temp():
    '''
    This function will access the Major City csv file and return the temperature data for the City of London from
    1960 until 2013 as a sorted dataframe.
    '''
    major = pd.read_csv('GlobalLandTemperaturesByMajorCity.csv')
    city = major[major['City'] == 'London']
    city['dt'] = pd.to_datetime(city['dt'])
    city = city.drop(columns = ['City', 'Country', 'Latitude', 'Longitude', 'AverageTemperatureUncertainty'])
    city = city.dropna()
    city = city.set_index('dt').sort_index()
    city = city['1960-01-01':]
    city['AverageTemperature'] = city['AverageTemperature'] * 9 / 5 + 32
    return city