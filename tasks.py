import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Завдання 1.
# Створити датафрейм з такими даними (колонками):
# ім’я студента; середній бал; оцінка за іспит; кількість спроб здачі іспиту.

# Завдання 2.
# Додати до датафрейму колонку "Доступ студента до іспиту".

# Завдання 3.
# Вивести мін., макс., серед., медіанний показники середнього бала.

# Завдання 4.
# Вивести кількість студентів, які склали іспит з першого разу.

# Завдання 5.
# Вивести Будь-які дані з датафрейму у вигляді серії.


print('--- Task 1 ---')

# Index of the dataframe.
row_lables = [1, 2, 3, 4, 5]
# Values of the dataframe.
students_df = {
    'Name': ['Oleksii', 'Mariia', 'Sergii', 'Dariia', 'Oleg'],
    'Aver_score': [89.2, 78.3, 80.5, 95.1, 70.2],
    'Exam_score': [80, 81, 90, 79, 75],
    'Attempts': [2, 4, 3, 5, 1],
}

# Create the dataframe.
df = pd.DataFrame(data=students_df, index=row_lables)
print('Progress of students:\n')
print('Current dataframe:')
print(df)

print('\nData types of the dataframe:')
print(df.dtypes)
print('=========' * 10, '\n')


print('--- Task 2 ---')
# # Add a new column to the dataframe.
df['Admission'] = np.array(
    ['admitted', 'admitted', 'admitted', 'admitted', 'not admitted'])

print('Added a new column "Admission_to_the_next_course:\n')
print(df, '\n')

# Add a new row to dataframe.
marta = pd.Series(['Marta', 90.6, 85, 1, 'admitted'],
                  index=df.columns, name=6)
print('Created a new row:')
print(marta, '\n')

# Add the new row to the dataframe.
# pd.concat([df, marta.to_frame().T], ignore_index=True)

df = df.append(marta)
print('Current dataframe:')
print(df, '\n')

# Delete a row from the dataframe.
# df = df.drop(labels=[6])
# print(df)


print('--- Task 3 ---')
# Max, min, median, sum of Average score.
print(df.groupby(['Name'])['Aver_score'].agg(
    ['max', 'min', 'mean', 'median', 'sum']), '\n')

print('Average score of all students:')
print(df['Aver_score'].mean(), '\n')

print('Total describe of the dataframe:')
print(df.describe())
print('=========' * 10, '\n')


print('--- Task 4 ---')
print('Students who passed the exam the first time:')
print(df[df.Attempts == 1]
      [['Name', 'Exam_score']])
print('=========' * 10, '\n')


print('--- Task 5 ---')
# Access to series.
print('One serie of the dataframe:')
print(df['Name'], '\n')

# Save the dataframe to csv-file.
df.to_csv('student.csv')

# # Read the dataframe from the csv-file.
df_2 = pd.read_csv('student.csv', index_col=0)
print('Read from the csv-file "students.csv"')
print(df_2)
print('=========' * 10, '\n')


print('Visualisation of dataframe:')
print('Look at the right!')
aver_score = [70, 78.3, 80.5, 95.1, 70.2, 90.6]
exam_score = [89, 81, 90, 79, 75, 85]
attempts = [2, 4, 3, 5, 7, 1]
index = ['Oleksii', 'Mariia', 'Sergii', 'Dariia', 'Oleg', 'Marta']

df = pd.DataFrame(
    {'Average score': aver_score, 'Current exam score': exam_score,
     'Attempts': attempts}, index=index)

ax = df.plot.bar(rot=0)
plt.show()
