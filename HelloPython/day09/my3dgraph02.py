
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

import pymysql as pysql
from array import array

conn = pysql.connect(host='localhost', port=3307, user='root', password='python', db='pydb', charset='utf8')
cur = conn.cursor()

#sql = "SELECT s_name, price, crw_date from stock where s_name = '삼성전자' or s_name = 'LG전자' or s_name = '현대중공업지주' order by s_name, crw_date"
sql = "SELECT s_name, price, crw_date from stock where s_name = '삼성전자' order by crw_date"
cur.execute(sql)

conn.commit()

rows = cur.fetchall()
print(rows)

samsung = []
samsung.append(rows)
print(samsung[0][0][1])
lg = []
hyundae = []

conn.close()
##삼성 LG 현대의 그래프를 그려오시오.



# Open the drawing window 1, draw in 3D space
fig = plt.figure(1)
ax = fig.gca(projection='3d')
 
 # Give points (0, 0, 0) and (100, 200, 300)
y = range(10)
for i in range(10):
    x = np.zeros(3)
    
     # Connect the first two points in the array
    figure = ax.plot(x, y, samsung[0][0][i], c='b')

plt.show() 