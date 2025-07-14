# analysis.py

from config import config
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

#read raw database
df = pd.read_csv(config['raw_path']+config['filename'])

# 1) Pairplot of all variables
sns.pairplot(df)
plt.suptitle("Pairwise relationships", y=1.02)
plt.show()

# 2) OLS regression: wage ~ age + sex + children
model = smf.ols('wage ~ age + sex + children', data=df).fit()
print(model.summary())