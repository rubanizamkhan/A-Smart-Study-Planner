# A-Smart-Study-Planner

**#OVERVIEW**

A Smart Study Planner is a mini project for students to plan their day effectively and give required time to each subject based on their difficulty level.
The program distributes daily study hours across subjects and provide a Daily Progress Tracker.  
This project is beginner friendly.

**#FEATURES**

Takes 5 subjects as input.

Ask difficulty levels 

Ask daily available hours

Allocates study hours proptionally using difficulty weightage

Generates a Smart Study Planner

Shows completed subjects, pending subjects and daily progress percentage


**#TECH STACK**

Python 3
(No external libraries required)


**#USER INPUT REQUIRED**

Name of user

5 Subjects

Available hours

Difficulty of each subject

Completed subjects


**#CODE**
```python
# EDUCATION
#A SMART STUDY PLANNER 

Name=input("Enter your name: ")

Subject1=input("\nEnter 1 subject: ")
Subject2=input("Enter 2 subject: ")
Subject3=input("Enter 3 subject: ")
Subject4=input("Enter 4 subject: ")
Subject5=input("Enter 5 subject: ")

hour_available_per_day=float(input("Enter available hours per day: "))

print("\nNow enter the Difficulty Level of each subject" )
print("Type: easy / medium / hard")

D1=input(f"Difficulty level of {Subject1}: ")
D2=input(f"Difficulty level of {Subject2}: ")
D3=input(f"Difficulty level of {Subject3}: ")
D4=input(f"Difficulty level of {Subject4}: ")
D5=input(f"Difficulty level of {Subject5}: ")

weight={"easy":1, "medium":2, "hard":3}

w1=weight[D1]
w2=weight[D2]
w3=weight[D3]
w4=weight[D4]
w5=weight[D5]

total_weight=w1+w2+w3+w4+w5

time1=(w1/total_weight)*hour_available_per_day
time2=(w2/total_weight)*hour_available_per_day
time3=(w3/total_weight)*hour_available_per_day
time4=(w4/total_weight)*hour_available_per_day
time5=(w5/total_weight)*hour_available_per_day

print("\n-------------------------------")
print("YOUR SMART STUDY PLAN")
print("-------------------------------")

print(f"{Subject1}:{round(time1,2)}hours/day ")
print(f"{Subject2}:{round(time2,2)}hours/day ")
print(f"{Subject3}:{round(time3,2)}hours/day ")
print(f"{Subject4}:{round(time4,2)}hours/day ")
print(f"{Subject5}:{round(time5,2)}hours/day ")

print("\n--------------------------------")
print("Daily Progress Tracker")
print("--------------------------------")

completed=input("Enter the subjects you have completed today (coma separated): ")

completed_list=[x.strip() for x in completed.split(",")]

subjects=[Subject1, Subject2, Subject3, Subject4, Subject5]

pending_list=[s for s in subjects if s not in completed_list]

progress=(len(completed_list)/len(subjects))*100

print("\nCompleted List:", completed_list)
print("\nPending List:", pending_list)
print("\nToday's Progress:", round(progress, 2), "%")
```

**#PROGRAM OUTPUT**
```python
A Smart Daily Study Plan displaying the allocated hours for each subject.
A Daily Progress Report.


YOUR SMART STUDY PLAN

maths:2.18hours/day 

physics:1.45hours/day 

chemistry:1.45hours/day 

english:0.73hours/day 

python:2.18hours/day


DAILY PROGRESS TRACKER

Enter the subjects you have completed today (coma separated): python

Completed List: ['python']

Pending List: ['maths', 'physics', 'chemistry', 'english']

Today's Progress: 20.0%
```
