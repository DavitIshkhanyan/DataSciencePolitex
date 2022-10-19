import numpy as np
import pandas as pd

nestdict = {'red': {2012:22,2013:33},
                'white': {2011: 13, 2012: 22, 2013: 16},
                'blue': {2011: 17, 2012: 27, 2013: 18}}
frame = pd.DataFrame(nestdict)

# ser = pd.Series([5,0,3,8,4], index=['red','blue','yellow','white','green'])
# print(ser.index)
# print(ser.idxmin())
# print(ser.idxmax())

# /////////////////////////////////

# serd = pd.Series(range(6), index=['white','white', 'blue', 'green', 'green', 'yellow'])
# print(serd)
# print(serd['white'])

# print(serd.index.is_unique)
# print(frame.index.is_unique)

# //////////////////////////////////////////
# ser = pd.Series([2,5,7,4], index=['one','two','three','four'])
# print(ser)

# print(ser.reindex(['three','four','five','one']))

# /////////////////////////////////

# ser3 = pd.Series([1,5,6,3], index=[0,3,5,6])
# print(ser3)

# ser3 = ser3.reindex(range(6), method='ffill')
# print(ser3)
# ser3 = ser3.reindex(range(6), method='bfill')
# print(ser3)

# ///////////////////////////////////////
data = {'color': ['blue', 'green','yellow','red','white'],
        'object': ['ball','pen','pencil', 'paper', 'mug'], 
        'price': [1.2,1.0,0.6,0.9,1.7]}
frame = pd.DataFrame(data)

ser = pd.Series(np.arange(5))
# frame['new'] = ser
print(frame)

frame = frame.reindex(range(5), method='ffill', columns=['color','price','new','object'])
print(frame)