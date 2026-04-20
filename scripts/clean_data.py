import pandas as pd
from transform import normalize_marks, calculate_average, validate_data

#Read data
marks = pd.read_csv('../data/marks.csv')

#Cleaning
marks['marks'] = marks['marks'].replace(0, pd.NA)
marks = marks.dropna(subset=['marks'])
marks['marks'] = marks['marks'].astype(int)

#Validation
marks = validate_data(marks)

#Transformation
marks = normalize_marks(marks)
avg_marks = calculate_average(marks)

#Save files
marks.to_csv('../data/cleaned_marks.csv', index=False)
avg_marks.to_csv('../data/avg_marks.csv', index=False)

print("Transformation completed successfully!")
