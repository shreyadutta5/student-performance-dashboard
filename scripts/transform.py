import pandas as pd

def normalize_marks(df):
    df['normalize_marks'] = (df['marks'] - df['marks'].min()) / (df['marks'].max() - df['marks'].min())
    return df

def calculate_average(df):
    avg = df.groupby('student_id')['marks'].mean().reset_index()
    avg.rename(columns={'marks': 'average_marks'}, inplace=True)
    return avg

def validate_data(df):
    df = df[df['marks'] >= 0]
    return df
