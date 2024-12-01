from extract import extract_data
import pandas as pd

def transform_data(data):
    #remove unnecessary data
    data.drop(data.iloc[:,2:44],implace=True,axis=1)
    
    # remove missing values
    data_clean=data.dropna()

    # round consumption values to the nearest integer
    data_column_name=data_clean.columns[-1]
    Consumption_data=round(data_clean[data_column_name],2)

    new_consumption_data={
        data_column_name:Consumption_data
    }

    
