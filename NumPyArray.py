import numpy as np


#mtz = np.arange(1, 10, 1).reshape(3, 3)
#print(mtz)

#print(mtz>5)

#print("")
#print("")
#print("")
#print("")


#arr = np.array(['Goku', 'Goten', 'Gohan', 'Trunks', 'Bulma'])
#np.char.upper(arr)
#print(arr)
#print(np.char.find(arr, 'GO')>=0)
#print(arr[np.char.find(arr, 'GO')>=0])

ds = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')
print(ds[0, :])
ds_cost = ds[1:, 6]
ds_cost=ds_cost.astype(float)
print(ds_cost.mean())