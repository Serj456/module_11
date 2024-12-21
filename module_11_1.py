import requests
import os
r = requests.get("https://sanshaspb.ru/wp-content/uploads/2024/10/s162v-pink-_4__1500x1500.jpg")
if r.status_code == 200:
    with open('image.png', 'wb') as image:
        image.write(r.content)
        print("картинка загружена")
else:
    print('Что то написано неверно')
os.system('image.png') - открываем картинку


import pandas as pd
df = pd.read_csv("import_ou_csv.csv")
print(df.head())
print(df.dtypes)
print(df.describe())

import numpy as np
import random
massive = np.array([[5,2,3],[6,2,1]])
print(massive)
print(massive.ndim)
print(massive.shape)
print(massive[1,1])
massive_random = np.random.randint(-2,2, size=(3,3))
print(massive_random)
massive_random_2 = massive_random + 2
print(massive_random_2)
print(massive_random.sum())
print(massive_random_2.sum())