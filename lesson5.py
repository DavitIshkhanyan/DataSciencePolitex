import pandas as pd
import numpy as np
data = {'color': ['blue', 'green','yellow','red','white'],
        'object': ['ball','pen','pencil', 'paper', 'mug'], 
        'price': [1.2,1.0,0.6,0.9,1.7]}
frame = pd.DataFrame(data, index=['one','two','tree','four','five'])
# print(frame)

# ////////////////////////////////////////

# print(frame.color)
# print(frame.index)
# print(type(frame))

# print(frame.values)
# print(frame['price'])

# print(frame.iloc[2])
# print(frame.iloc[[2,3]])

# print(frame[0:1])
# print(frame[1:3])

print(frame['color'][1])

# ////////////////////////////////

# frame.index.name = 'id'
# frame.columns.name = 'item'
# print(frame)

# //////////////////////////////////////////

frame['new'] = 12
# print(frame)

frame['new']['three'] = 5
print(frame)

frame['new'] = [1,2,3,4,5]
print(frame)

# //////////////////////////////////
data = {'color': ['blue', 'green','yellow','red','white'],
        'object': ['ball','pen','pencil', 'paper', 'mug'], 
        'price': [1.2,1.0,0.6,0.9,1.7]}
frame = pd.DataFrame(data)

ser = pd.Series(np.arange(5))
frame['new'] = ser
print(np.arange(5))
print(frame)