import pandas as pd
import json

with open('car.json', 'r', encoding='utf-8') as f:
    data=json.load(f)
    
    vdid=[]
    status=[]
    datacollecttime=[]
    lane0_vsrdir=[]
    lane0_cars=[]
    lane0_laneoccupy=[]
    lane0_speed=[]
    lane0_vsrid=[]
    for d in data["data"]:
        vdid.append(d["vdid"])
        status.append(d["status"])
        datacollecttime.append(d["datacollecttime"])

        if  len(d["lane"])>=1:
            lane=d["lane"][0]
            lane0_vsrdir.append(lane["vsrdir"])
            lane0_cars.append(lane["cars"])
            lane0_laneoccupy.append(lane["laneoccupy"])
            lane0_speed.append(lane["speed"])
            lane0_vsrid.append(lane["vsrid"])

    df = pd.DataFrame({
        'vdid': vdid,
        'status':status,
        'datacollecttime':datacollecttime,
        'lane0_vsrdir':lane0_vsrdir,
        'lane0_cars':lane0_cars,
        'lane0_laneoccupy':lane0_laneoccupy,
        'lane0_speed':lane0_speed,
        'lane0_vsrid':lane0_vsrid
    })
    df.to_excel('car.xls')

    t1=df["lane0_speed"].max()
    print(t1)
    print(df[df['lane0_speed'] == t1])

    t1=df["lane0_speed"].mean()
    print(t1)
    t1=df["lane0_speed"].describe()
    print(t1)
    t1=df["lane0_speed"].median()
    print(t1)
