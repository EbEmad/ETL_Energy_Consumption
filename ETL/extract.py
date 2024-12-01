import pandas as pd
 

 # read dataset
def extract_data(file):
    data=pd.read_csv(file)
    return data 