import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data1 = pd.DataFrame({'robot':lst , 'human':lst} )
data1.loc[data1['robot'] == 'robot', 'robot'] = 1
data1.loc[data1['robot'] == 'human', 'robot'] = 0
data1.loc[data1['human'] == 'human', 'human'] = 1
data1.loc[data1['human'] == 'robot', 'human'] = 0
data1.head()