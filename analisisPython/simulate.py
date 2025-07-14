# simulate.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#1. import configuration
from config import config
#print(config)

#2. create dataframe
df = pd.DataFrame()

#3. create simulation
population = 10000

#3.1 population age
age = np.random.normal(30,10,population)
plt.figure()
plt.title('Population Histogram')
plt.hist(age,bins=100)
plt.show()

#jb_test = stats.jarque_bera(age)
#print(jb_test.pvalue)

#3.2 sex
sex_option = ['Male','Female']
sex = np.random.choice(sex_option, population, p=[0.49,0.51])

male_count = np.sum(sex == 'Male')
female_count = np.sum(sex == 'Female')
sex_count = [male_count,female_count]

plt.figure()
plt.bar(sex_option,sex_count)
plt.title('Gender Demography')
for i, c in enumerate(sex_count):
    plt.text(i, c + population*0.005, str(c), ha='center')
plt.show()

sex_binary = []
for p in sex:
    if p == 'Male':
        sex_binary.append(1)
    else:
        sex_binary.append(0)

#3.3 children
# each year increases the chance of having one child, by 1%
# females are as twice as problable to have a child than men
children = []
children_options = [0,1]
for i in range(population):
    child = age[i]/100 
    if sex[i] == 'Male':
        child += 0.10
    else:
        child += 0.20
    if child > 1:
        child = 1
    children_number = np.random.choice(children_options,p=[1-child,child])
    children.append(children_number)

#3.4 wage
wage = []
for i in range(population):
    w = 3750 + age[i]*125 + sex_binary[i]*3500 + children[i]*2700 + np.random.normal(1000,1000)
    wage.append(w)

#4. Insert simulation into dataframe
simulation = {
    'age': age.astype(int),
    'sex': sex_binary,
    'children': children,
    'wage': wage
    }

df = pd.DataFrame(simulation)

#5. save simulated data
df.to_csv(config['raw_path']+config['filename'],index=False)
