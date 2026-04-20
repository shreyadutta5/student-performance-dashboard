import pandas as pd

def normalize_marks(df):
    df['normalize_marks'] = (df['marks'] - df['marks'].min()) / (df['marks'].max() - df['marks'].min())
    return df

def calculate_average(marks):
    # Calculate average marks per student
    avg_marks = marks.groupby('name')['marks'].mean().reset_index()
    
    # Rename column for clarity
    avg_marks.rename(columns={'marks': 'avg_marks'}, inplace=True)
    
    return avg_marks

def validate_data(df):
    df = df[df['marks'] >= 0]
    return df
