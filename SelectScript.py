import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import function as fun
from astropy.coordinates import SkyCoord
from astropy.coordinates import Angle
from astropy import units as u
from astropy.io import ascii

argv = sys.argv

def CheckValue(func):
    value = func
    while True:
        print('Is',"'",value,"'",'true?\nPress y (yes) or n (no).')
        yn = fun.YesNo()
        while not yn == 'y' and not yn == 'n':
            print('')
            print('Press y (yes) or n (no).')
            yn = fun.YesNo()

        if yn == 'y':
            print('\nOK!')
            print('------------------------------------ \n')
            break;

        elif yn == 'n':
            print('\nRetry ...')
            value = input()
            print('')
            continue;

    return value

def hms_to_deg(hms):
    return Angle(hms, unit=u.hourangle).deg

def dms_to_deg(dms):
    return Angle(dms, unit=u.deg).deg

def deg_to_hms(deg):
    return Angle(deg, unit=u.deg).to_string(unit=u.hourangle, sep=':', pad=True)

def deg_to_dms(angle):
    """
    This function converts an angle from the decimal degrees to degrees, minutes, and seconds.
    """
    deg = int(angle)
    min = int((angle*60) % 60)
    sec = (angle*3600) % 60

    return f"{deg:02d}:{abs(min):02d}:{abs(sec):05.2f}"

def find_closest_object(ra, dec, csv_path, num_closest=20):
    # CSVを読み込む
    df = pd.read_csv(csv_path)
    # RA, DECを角度に変換
    df['RA'] = df['RA'].apply(hms_to_deg)
    df['DEC'] = df['DEC'].apply(dms_to_deg)

    # RA, DECが適切な範囲内にある行のみを保持
    df = df[df['RA'].between(0, 360)]
    df = df[df['DEC'].between(-90, 90)]

    # 天球座標を作成
    df_coords = SkyCoord(df['RA'], df['DEC'], frame='icrs', unit=(u.deg, u.deg))
    target_coord = SkyCoord(ra, dec, frame='icrs', unit=(u.hourangle, u.deg))
    
    # 距離を計算
    dists = target_coord.separation(df_coords)
    
    # 距離でソート
    df['dist'] = dists.deg
    df = df.sort_values('dist')
    
    # 最も近いnum_closest個のオブジェクトを取得
    closest_objects = df.head(num_closest)

    # RA, DECを元の形式に戻す
    closest_objects['RA'] = closest_objects['RA'].apply(deg_to_hms)
    closest_objects['DEC'] = closest_objects['DEC'].apply(deg_to_dms)

    # CSVに出力
    closest_objects_copy = closest_objects
    closest_objects = closest_objects.drop(columns='dist')
    closest_objects.to_csv("Script/"+newname+".csv",na_rep='None',index=False)

    return closest_objects_copy[['ObjectName', 'RA', 'DEC', 'dist']][:20]



if len(argv) < 7:
    print('Please select script and set RA and DEC!!\n(eg. python SelectScript.py -script script.csv -RA 2:30:40 -DEC -10:20:30)')
    sys.exit()

for i in range(0,len(argv)):
    if argv[i] == '-script':
        scriptname = argv[i+1]
        csv_path = 'Script/'+scriptname
        print('Got Script!')
        
        for j in range(0,len(argv)):
            if argv[j] == '-RA':
                ra = argv[j+1]
                print('\nSet RA!\nRA =',ra)

                for k in range(0,len(argv)):
                    if argv[k] == '-DEC':
                        dec = argv[k+1]
                        print('\nSet DEC!\nDEC =',dec,'\n')

                        for l in range(0,len(argv)):
                            if argv[l] == '-num':
                                num_closest = int(argv[l+1])
                                print('Set number of select!\nNum =',num_closest,'\n')
                                newname = CheckValue(fun.AddScriptName())
                                print('\nScript name is',"'",newname,"'.\n")  
                                closest_object = find_closest_object(ra, dec, csv_path, num_closest)
                                print(closest_object)
                                sys.exit()
                        
                        newname = CheckValue(fun.AddScriptName())
                        print('\nScript name is',"'",newname,"'.\n")  
                        closest_object = find_closest_object(ra, dec, csv_path)
                        print(closest_object)
