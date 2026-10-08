import pandas as pd

data = {
    'Name': ['Aditya', 'Riya', None, 'Pratik', 'Gauri'],
    'Age': [25, None, 30, 22, 28],
    'Weight': [65, 55, None, 70, 60],
    'Height': [1.70, 1.60, 1.75, 1.80, 1.65],
    'BloodPressure': [120, 118, 125, 130, 115]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df['Age'] = df['Age'].fillna(df['Age'].mean())

df['Weight'] = df['Weight'].fillna(df['Weight'].mean())

df = df.dropna(subset=['Name'])

df['BMI'] = df['Weight'] / (df['Height'] ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

df['BMI_Category'] = df['BMI'].apply(bmi_category)

df['Age_Category'] = df['Age'].apply(
    lambda x: 'Young' if x < 25 else 'Adult'
)
df.loc[df['BloodPressure'] > 125, 'BloodPressure_Status'] = 'High'
df.loc[df['BloodPressure'] <= 125, 'BloodPressure_Status'] = 'Normal'

print("\nPeople with Weight > 60:")
print(df[df['Weight'] > 60])

df = df.sort_values(by='Age')

df['BMI'] = df['BMI'].round(2)

print("\nFinal DataFrame:")
print(df)

print("\nStatistical Summary:")
print(df[['Age', 'Weight', 'Height', 'BloodPressure', 'BMI']].describe())

print("\nAverage Age:", round(df['Age'].mean(), 2))
print("Average Weight:", round(df['Weight'].mean(), 2))
print("Average BMI:", round(df['BMI'].mean(), 2))
