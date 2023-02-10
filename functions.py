import pandas as pd
import new_lib as nl
import wrangle as w
from matplotlib import pyplot as plt
import seaborn as sns
from datetime import datetime
import statsmodels.api as sm
from statsmodels.tsa.api import Holt, ExponentialSmoothing
from sklearn.metrics import mean_squared_error
from math import sqrt
import warnings
warnings.filterwarnings("ignore")
city = w.wrangle_temp()
city

train_size = int(round(city.shape[0] * 0.5))
val_size = int(round(city.shape[0] * 0.3))
val_index = train_size + val_size
test_size = int(round(city.shape[0] * .2))
train = city[:train_size]
val = city[train_size:val_index]
test = city[val_index:]


def evaluate(target, preds):
    '''
    Fast way to find RMSE for models
    '''
    rmse = round(sqrt(mean_squared_error(val[target], preds[target])), 0)
    return rmse
# Function to evaluate rmse of a model


def plot_and_eval(target, preds):
    '''
This function will plot and evaluate a model using target predicitons from a dataset and return a graph of the data
It will also calculate the rmse of the data and report that along with the data
    '''
    plt.figure(figsize = (14,6))
    plt.plot(train[target], label='Train', linewidth=1, color='#2E2EFE')
    plt.plot(val[target], label='Validate', linewidth=1, color='#33EBDC')
    plt.plot(preds[target], label='predictions', linewidth=2, color='#EF080C')
    plt.legend()
    plt.title('Average Temperature of London')
    rmse = evaluate(target, preds)
    print(target, '-- RMSE: {:.0f}'.format(rmse))
    plt.show()
# Plot the model and state Rmse

def make_baseline_predictions(temp_preds = None):
    preds = pd.DataFrame({'AverageTemperature': [temp_preds]},
                          index=val.index)
    return preds
# creating a function to examine rolling average baseline values to see if they are any better


def final_plot(target, preds):
    plt.figure(figsize=(12,4))
    plt.plot(train[target], color='#9E05EF', label='train')
    plt.plot(val[target], color='#223CDF', label='validate')
    plt.plot(test[target], color='#06F5F8',label='test')
    plt.plot(preds[target], color='#2DD702', label='predictions')
    plt.legend()
    plt.title('10 Year Forcast for London Temperatures')
    plt.ylabel('Temperature')
    plt.show()
# Create a final plot function