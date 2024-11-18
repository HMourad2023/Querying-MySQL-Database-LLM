import pandas as pd

def dataframe_to_json(df):
    json_data = df.to_json(orient='records')
    return json_data