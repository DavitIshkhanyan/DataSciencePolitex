import numpy as np
import pandas as pd

ser = pd.Series(np.arange(4.), index=['red','blue','yellow','white']);
# print(ser)
# print(ser.drop('yellow'))
# print(ser.drop(['blue','white']))

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])

# print(frame.drop(['blue','yellow']))
# print(frame.drop(['pen','pencil'], axis=1))

# s1 = pd.Series([3,2,5,1],['white','yellow','green','blue'])
# s2 = pd.Series([1,4,7,2,1],['white','yellow','black','blue','brown'])
# print(s1 + s2)

frame1 = pd.DataFrame(np.arange(16).reshape((4,4)), index=['red','blue','yellow','white'], columns=['ball','pen','pencil','paper'])

# frame2 = pd.DataFrame(np.arange(12).reshape((4,3)), index=['blue','green','white','yellow'], columns=['mug','pen','ball'])
# print(frame1)
# print(frame2)
# print(frame1 + frame2)
# print(frame1.add(frame2))
# print(frame1.sub(frame2))

# ser = pd.Series(np.arange(4),index=['ball','pen','pencil','paper'])
# ser['mug'] = 9
# print(frame - ser)

print(np.sqrt(frame))

f = lambda x: x.max() - x.min()

print(frame.apply(f))
print(frame.apply(f, axis=1))

def f(x):
    return pd.Series([x.min(), x.max()], index=['min','max'])
print(frame.apply(f))
