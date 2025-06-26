import pandas as pd

file_path = "data/StudentsPerformance.xlsx"

df = pd.read_excel(file_path)

print('student performance data:')
print(df.head())

#calculating score by gender
gender_average = df.groupby('gender')[["math score","reading score","writing score"]].mean()
print(gender_average)


#Analyzing the Effect of a Test Prep Course on Performance
prep_course_effect = df.groupby('test preparation course')[["math score","reading score","writing score"]].mean()
print(prep_course_effect)

#Analysis of Performance by Parental Education Level
performance_by_parent_education_level = df.groupby('parental level of education')[["math score","reading score","writing score"]].mean()
print(performance_by_parent_education_level)

#Finding the Highest and Lowest Scoring Students
df['overall average'] = (df["math score"] + df["reading score"] + df["writing score"]) / 3
max_average = df.loc[df['overall average'].idxmax()]
min_average = df.loc[df['overall average'].idxmin()]
print("Student with the highest average:")
print(max_average)
print("\nStudent with the lowest average:")
print(min_average)

#Sort students by overall average:
overall_sorted = df.sort_values('overall average', ascending=False)[["gender", "overall average","math score","reading score","writing score"]]
print(overall_sorted.head())

#Calculate average scores by Race/Ethnicity:
race_ethnicity_average = df.groupby("race/ethnicity")[["math score","reading score","writing score"]].mean()
print(race_ethnicity_average)

#Calculate average scores by Lunch status:
lunch_average = df.groupby("lunch")[["math score","reading score","writing score"]].mean()
print(lunch_average)

