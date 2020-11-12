# Heart-Disease-Diagnosis-System

INTRODUCTION

Heart disease is one of the diseases that causes a significant effect on patients who suffer from this disease. Currently, the diagnosis of having heart disease or not is by the test blood, which takes time to get the results. Moreover, using machine learning in healthcare, such as in heart disease prediction, is an essential field that helps the doctors to get the patient`s data and determines the probability of heart disease. The predicting of this kind of disease can minimize the percentage of risk, and the doctors can manage and control this disease at the right time. Machine learning algorithms aim to get an accurate prediction of the presence of heart disease to save the patient's life before it's too late. The algorithms that we will use on the dataset are Random Forest algorithm. This report consists of the problem statement to define the problem, the methodology to explain the progress of the chosen algorithm, and the result of the best algorithm that predicting heart disease with high accuracy.

PROBLEM STATEMENT

Heart disease considered a dangerous disease that harms human health and the main reason for death for both gender men and women. As the statistics say that about half of the death of men because of heart disease in 2009. So, we are going to solve the problem by predicting the presence of heart diseases using classifications algorithms.  

The dataset consists of 303 individuals and 14 attributes (columns) in the dataset. The description of these attributes as the following:
1.	Age, it shows the age of each individual.
2.	Sex, it shows the gender of each individual using the symbols 0 and 1. The meaning of them is (0=female) and (1= male).
3.	Chest-pain type, it shows the type of chest-pain of each individual using the symbols 1, 2, 3, 4, and 5. The meaning of them are (1 = Typical Angina), (2 = Atypical angina), (3 = Non-Anginal Pain), and (4 = Asymptotic).
4.	Resting Blood Pressure, it shows the value of resting blood pressure of each individual in mmHg (unit).
5.	Serum Cholesterol: it shows the serum cholesterol in mg/dl (unit).
6.	Fasting Blood Sugar: it shows the comparison of the fasting blood sugar value of each individual in 120mg/dl. The comparison using the symbols 0 and 1 as the following:
If fasting blood sugar > 120mg/dl then: (1=true)
else:  (0=false)
7.	Resting ECG: it shows the resting electrocardiographic results using the symbols 0, 1, and 2. The meaning of them is(0 = normal), (1 = having ST-T wave abnormality) and, (2 = left ventricular hypertrophy)
8.	Max heart rate achieved: it shows the maximum heart rate achieved of each individual.
9.	Exercise-induced angina using the symbols 0 and 1. The meaning of them is(1 = Yes) and, (0 = No).
10.	ST depression induced by exercise relative to rest: it shows the value in the format of integer or float.
11.	Peak exercise ST segment, using the symbols 1, 2, and 3. The meaning of them are (1 = Upsloping), (2 = Flat), (3 = Down Sloping).
12.	The number of major vessels (0-3) colored by fluoroscopy: shows the value in the format of integer or float.
13.	Thal: it shows the thalassemia, using symbols 3, 6, and 7. The meaning of them are (3 = Normal), (6 = Fixed Defect) and, (7 = Reversible Defect).
14.	Diagnosis of heart disease (target), it shows whether the individual is suffering from heart disease or not using the symbols 0 and 1. The meaning of them are (0 = absence) and (1 = present).

The algorithm chosen to address heart diseases problem is Random Forest (RF). RF is offering high accuracy. The researchers used a system that predicts heart diseases based on Chi square feature selection measure. And this system applied the Random forest algorithm and chi-square to predict heart disease on the historical information of the patients to make a prediction of coronary heart disease with higher accuracy as possible.

