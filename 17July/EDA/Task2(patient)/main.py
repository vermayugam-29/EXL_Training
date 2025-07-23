import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('patient_data.csv')
df['VisitDatete'] = pd.to_datetime(df['VisitDate'])


#Bar chart - Number of Patients by Region
region_patient = df['Region'].value_counts()
region_patient.plot(kind='bar',title='Number of Patients by Region', color='skyblue')
plt.xlabel('Region')
plt.ylabel('Number of Patients')
plt.tight_layout()
plt.show()

#Pie chart - Distribution of Diagnosis
dignostics_distribute = df['Diagnosis'].value_counts()
dignostics_distribute.plot(kind='pie',title='Distribution of Diagnostic', startangle = 90)
plt.tight_layout()
plt.show()

#Line chart - Total Treatment Cost Over Time
cost = df.groupby('VisitDatete')['TreatmentCost'].sum()
cost.plot(kind='line',color='red',title='Total Treatment Cost Over Time')
plt.xlabel('Date')
plt.ylabel('Total Treatment Cost')
plt.tight_layout()
plt.show()

#Histogram - Age Distribution of Patients
plt.hist(df['Age'], bins=10, color='green', edgecolor='black')
plt.title('Age Distribution of Patients')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.show()

#Scatter Plot - Age vs Treatment Cost
plt.scatter(df['Age'], df['TreatmentCost'],  color='purple')
plt.title('Age vs Treatment Cost')
plt.xlabel('Age')
plt.ylabel('Treatment Cost')
plt.tight_layout()
plt.show()