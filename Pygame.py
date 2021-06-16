import pandas as pd

data=pd.read_csv('pygame.stats.csv')
print(data.columns)

def read_csv(path):
    data=pd.read_csv(path)
    return data


data=read_csv('pygame.stats.csv')
print(data)


    