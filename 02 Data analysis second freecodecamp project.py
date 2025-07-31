import numpy as np
import sys
import pandas as pd
import csv
def demograghic_analysis(print_data = True):
    df = pd.read_csv(r"C:/users/alire/downloads/compressed/archive/adult_data.csv", sep = ',')
    race_count = df['race'].value_counts()
    #average age of men
    average_age_men = df[df['sex'] == "Male"]['age'].mean().round(1)
    #what is the percentage of people who have a Bachelors degree?
    num_bachelors = len(df[df['education'] == "Bachelors"])
    tot_bachelors = len(df)
    bachelors_percentage = round(num_bachelors/tot_bachelors * 100,1)
    #people with and without advanced education
    higher_education = df[df['education'].isin(["Bachelors","Masters","Doctorate"])]
    lower_education = df[~df['education'].isin(["Bachelors","Masters","Doctorate"])]
    #percentage with salary>50K
    higher_education_percentage = round(len(higher_education[higher_education['salary'] == ">50K"])/len(higher_education) * 100,1)
    lower_education_percentage = round(len(lower_education[lower_education['salary'] == ">50K"])/len(lower_education) * 100,1)
    #what is the minimum number of hours a person works per week? hours per week
    min_work_hours = df['hours-per-week'].min()
    #what percentage of the people who work the minimum number of hours per week have salary of >50K?
    num_min_work_hours = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_among_workers = round(len(num_min_work_hours[num_min_work_hours['salary'] == ">50K"])/len(num_min_work_hours) * 100,1)
    #what country has highest percentage of people that earn >50K?
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == ">50K"]['native-country'].value_counts()
    highest_earning_country = (country_rich_counts / country_counts *100).idxmax()
    highest_earning_country_percentage = round((country_rich_counts / country_counts *100).max(),1)
    #Identify the most popular occupation for those who has >50K in india?
    people_of_india = df[(df['native-country'] == "india") & (df['salary'] == ">50K")]
    occupation_counts = people_of_india['occupation'].value_counts()
    top_occupation_in_india = occupation_counts.max()
    if print_data :
            print("Number of each race:\n", race_count)
            print("average age of men:", average_age_men)
            print(f"Percentage with Bachelors degree: {bachelors_percentage}%")
            print(f"Percentage with higher education that earn >50K: {higher_education_percentage}%")
            print(f"Percentage with lower education that earn >50K: {lower_education_percentage}%")
            print(f"Min work time: {min_work_hours} hours per week")
            print(f"rich percentage among workers: {rich_percentage_among_workers}%")
            print("Country with highest percentage of rich:", highest_earning_country)
            print(f"rich people percentage earning in country: {highest_earning_country_percentage}%")
            print("Top occupation in India:",top_occupation_in_india)
            
    return{
            'race_count' : race_count,
            'average_age_of_men' : average_age_of_men,
            'Percentage with Bachelors degree' : bachelors_percentage,
            'Percentage with higher education that earn >50K' : higher_education_percentage,
            'Percentage with lower education that earn >50K' : lower_education_percentage,
            'Min work time' : min_work_hours,
            'rich percentage among workers' : rich_percentage,
            'Country with highest percentage of rich' : highest_earning_country,
            'rich people percentage earning in country' : highest_earning_country_percentage,
            'Top occupation in India' : top_occupation_in_india
        }