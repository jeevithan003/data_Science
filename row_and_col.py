import pandas as pd

d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

df = pd.DataFrame(data=d)
#counting row and rows and col in using range 
col=df.shape[1]
print(col)
print("my data sciense  demo project ")
