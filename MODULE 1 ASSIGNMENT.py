# lists of employees names to be dynamically created
import random
import pandas as pd

first_names = ["Yomi", "Fike", "Sayo", "Tundun", "Gbenga", "Adesola", "Tonia", "Gibson", "Toriola", "Amokachi"]
last_names = ["Nathaniel", "Anthony", "Tinubu", "Godson", "Peterson", "Adekola", "Osamudiamen", "Egetton", "Briggs", "Alabo"]
employees = []

for _ in range(400):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"
    
# generate salary range for the employees lists between 3000 and 30000
    salary = random.randint(3000,30000)
    
 #include column to indicate employees gender
    
    gender = random.choice(["Male","Female"])
    
 #indicate employees level based on salary grade
    if salary > 10000 and salary < 20000:
        level = 'A1'
    elif salary > 7500 and salary < 30000 and gender == "Female":
        level = "A5-F"
    else: level = " "
    
    employees.append({'Full Name': full_name, 'salary': salary, 'Gender': gender, "level": level})
    
# adding exception handling lines for potential error 
try:

    df =pd.DataFrame(employees)
    df.to_excel("employees.xlsx", index=False)
    print(df)
except:
    print("somthing is wrong")
    
    