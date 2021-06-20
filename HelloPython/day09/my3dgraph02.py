
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

import pymysql as pysql
from array import array

conn = pysql.connect(host='localhost', port=3307, user='root', password='python', db='pydb', charset='utf8')
cur = conn.cursor()
cur1 = conn.cursor()
cur2 = conn.cursor()

#sql = "SELECT s_name, price, crw_date from stock where s_name = '�궪�꽦�쟾�옄' or s_name = 'LG�쟾�옄' or s_name = '�쁽��以묎났�뾽吏�二�' order by s_name, crw_date"
sql = "SELECT s_name, price, crw_date from stock where s_name = '삼성전자' order by crw_date"
sql1 = "SELECT s_name, price, crw_date from stock where s_name = 'LG전자' order by crw_date"
sql2 = "SELECT s_name, price, crw_date from stock where s_name = '현대중공업지주' order by crw_date"
cur.execute(sql)
cur1.execute(sql1)
cur2.execute(sql2)

conn.commit()

rows = cur.fetchall()
rows1 = cur1.fetchall()
rows2 = cur2.fetchall()

print(rows)
print(rows1)
print(rows2)

samsung = []
ss = []
samsung.append(rows)
for k in range(10):
    print(samsung[0][k][1])
    ss.append(samsung[0][k][1])
    ss_i = [int(b) for b in ss]
    ss_n = np.array(ss_i)
print(ss_n)

lg = []
lg.append(rows1)

lg1 = []
hyundae = []
hyundae.append(rows2)
hy = []
for k in range(10):
    print(lg[0][k][1])
    lg1.append(lg[0][k][1])
    lg_i = [int(b) for b in lg1]
    lg_n = np.array(lg_i)
print(lg_n)

for k in range(10):
    print(hyundae[0][k][1])
    hy.append(hyundae[0][k][1])
    hy_i = [int(b) for b in hy]
    hy_n = np.array(hy_i)
print(hy_n)
#print(samsung[0][0][1])

conn.close()
##�궪�꽦 LG �쁽���쓽 洹몃옒�봽瑜� 洹몃젮�삤�떆�삤.



# Open the drawing window 1, draw in 3D space
fig = plt.figure(1)
ax = fig.gca(projection='3d')
 
 # Give points (0, 0, 0) and (100, 200, 300)
y = range(10)
for i in range(10):
    x = np.zeros(10)
    print(x)
    z = samsung[0][i][1]
    
     # Connect the first two points in the array
    figure = ax.plot(x, y, ss_n, c='b')
    b = 1
    figure = ax.plot(x+b, y, lg_n, c='r')
    b += 1
    figure = ax.plot(x+b, y, hy_n, c='g')
    b += 1
plt.show() 