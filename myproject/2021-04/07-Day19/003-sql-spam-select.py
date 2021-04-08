# project 4
import random
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import pymysql as mysql

db = mysql.connect(host="127.0.0.1",
                   user="admin",
                   passwd="admin",
                   db="mydatabase")
cursor = db.cursor()
cursor.execute("""
    SELECT `time`,`spam`,`user_id`,`chat_id` 
    FROM `spamtable` 
    WHERE id BETWEEN 6900 AND 7000;
""")
result = cursor.fetchall()

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

data = {
    'bar': {
        'chats': [],
        'positive_count': [],
        'negative_count': []},
    'distribution': {
        'positive_time': [],
        'negative_time': [],
        'positive_user_id': [],
        'negative_user_id': []
    },
    'cumulative': {}
}

""" cumulative
'chat_id':{
    'color':''
    'positive_time': [],
    'negative_time': [],
    'positive_user_count': [],
    'negative_user_count': []
}
"""

timeStart = result[0][0]
for row in result:
    dataTime = row[0]
    user_id = int(row[2])
    chat_id = row[3]

    if chat_id not in data['cumulative']:
        data['cumulative'][chat_id] = {}
        data['cumulative'][chat_id]['positive_time'] = [timeStart]
        data['cumulative'][chat_id]['negative_time'] = [timeStart]
        data['cumulative'][chat_id]['positive_user_count'] = [0]
        data['cumulative'][chat_id]['negative_user_count'] = [0]

    if int(row[1]) == 1:
        count = data['cumulative'][chat_id]['positive_user_count'][-1]
        count += 1
        data['cumulative'][chat_id]['positive_time'].append(dataTime)
        data['cumulative'][chat_id]['positive_user_count'].append(count)
        data['distribution']['positive_time'].append(dataTime)
        data['distribution']['positive_user_id'].append(user_id)
    else:
        count = data['cumulative'][chat_id]['negative_user_count'][-1]
        count += 1
        data['cumulative'][chat_id]['negative_time'].append(dataTime)
        data['cumulative'][chat_id]['negative_user_count'].append(count)
        data['distribution']['negative_time'].append(dataTime)
        data['distribution']['negative_user_id'].append(user_id)

for key, val in data['cumulative'].items():
    data['cumulative'][key]['color'] = (
        random.random(), random.random(), random.random())
    data['bar']['chats'].append(key)
    positive_count = data['cumulative'][key]['positive_user_count'][-1]
    data['bar']['positive_count'].append(positive_count)
    negative_count = data['cumulative'][key]['negative_user_count'][-1]
    data['bar']['negative_count'].append(negative_count)

fig = plt.figure(constrained_layout=True, figsize=(16, 9))

gs = GridSpec(7, 3, figure=fig)
ax1 = fig.add_subplot(gs[:3, :])  # x:chat_id, y:count, label:not spam & spam
ax1.bar(data['bar']['chats'],
        data['bar']['positive_count'],
        color='red',
        label="spam")
ax1.bar(data['bar']['chats'],
        data['bar']['negative_count'],
        bottom=data['bar']['positive_count'],
        color='green',
        label="not spam")
plt.xticks(rotation=45)
plt.xlabel('chat')
plt.ylabel('count')
plt.title('各群組比較')
plt.legend()

ax2 = fig.add_subplot(gs[4:, 0:1])  # x:time, y:id, label:spam
ax2.plot(data['distribution']['positive_time'],
         data['distribution']['positive_user_id'],
         'ro',
         label="spam")
ax2.plot(data['distribution']['negative_time'],
         data['distribution']['negative_user_id'],
         'go',
         label="not spam")
plt.xticks(rotation=45)
plt.xlabel('time')
plt.ylabel('id')
plt.title('id 分布圖')
plt.legend()

ax3 = fig.add_subplot(gs[4:, 1:2])  # x:time, y:spam count, label:group
for key, val in data['cumulative'].items():
    ax3.plot(val['positive_time'],
             val['positive_user_count'],
             c=val['color'],
             label=key)
plt.xticks(rotation=45)
plt.xlabel('time')
plt.ylabel('count')
plt.title('spam 數量累計圖')
plt.legend()

ax4 = fig.add_subplot(gs[4:, 2:3])  # x:time, y:not spam count, label:group
for key, val in data['cumulative'].items():
    rgb = (random.random(), random.random(), random.random())
    ax4.plot(val['negative_time'],
             val['negative_user_count'],
             c=val['color'],
             label=key)
plt.xticks(rotation=45)
plt.xlabel('time')
plt.ylabel('count')
plt.title('not spam 數量累計圖')
plt.legend()

fig.suptitle("spam 數量圖")

plt.legend()
plt.show()
