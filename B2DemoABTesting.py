# ctrl+/ multiple annotation!
# Demo project based on mock data to see if new webdesign has better performance then old one
# Fetch data, csv file as example.
# 1.read csv need Plus r in front of the path or Replace with a forward slash /!
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataFrame = pd.read_csv(r'e:\abtest.csv')
dataFrame = dataFrame.rename(columns={'action (0=view, 1=click)': 'action'})
# 2.Clean data first, good, very clean! And get real customer amounts without any duplicates
print(dataFrame['group'].unique())
print(dataFrame['landing_page'].unique())
print(dataFrame['action'].unique())
userSize = len(dataFrame['user_id'].drop_duplicates())
print(userSize)
# 3.Calculate clickThough rate for control/treatment group
# control_group = dataFrame.query('group=="control"')
# control_view = control_group.query('action==0')['user_id'].nunique()
# control_click = control_group.query('action==1')['user_id'].nunique()
# control_ctr = control_click/control_view
# print("Old web CTR: ", control_ctr)
#
# treatment_group = dataFrame.query('group=="treatment"')
# treatment_view = treatment_group.query('action==0')['user_id'].nunique()
# treatment_click = treatment_group.query('action==1')['user_id'].nunique()
# treatment_ctr = treatment_click/control_view
# print("New web CTR: ", treatment_ctr)

# 4.A\B testing, p-value<0.05
diffs = []
for _ in range(3000):
    sample = dataFrame.sample(userSize, replace=True)

    control_group = sample.query('group=="control"')
    control_view = control_group.query('action==0')['user_id'].nunique()
    control_click = control_group.query('action==1')['user_id'].nunique()
    control_ctr = control_click / control_view

    treatment_group = sample.query('group=="treatment"')
    treatment_view = treatment_group.query('action==0')['user_id'].nunique()
    treatment_click = treatment_group.query('action==1')['user_id'].nunique()
    treatment_ctr = treatment_click / treatment_view

    diff = treatment_ctr - control_ctr
    diffs.append(diff)
    diffs = np.array(diffs)

normalize_list = np.random.normal(0, diffs.std(), size)
# plt.hist(normalize_list)
# plt.axvline(x=diff_ctr, color="red")
# plt.show()

# p值<0.05
p_value = (normalize_list > diff_ctr).mean()
print("p-value：", p_value)
print("p是否<0.05:", p_value < 0.05)
