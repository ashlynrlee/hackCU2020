import pandas as pd

data_filepath = '../data.csv'

def load() :
    global data_filepath
    global df
    df = pd.read_csv(data_filepath)
    return df
    

if __name__=='__main__' :
    load()