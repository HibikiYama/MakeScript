import numpy as np
import matplotlib.pyplot as plt
import csv
import function as fun
import FitRotator as fr
import sys
import re
import subprocess
import math
from astropy import units as u
from astropy.coordinates import SkyCoord

argv = sys.argv


header = np.array(['Priority', 'BlockID', 'Observer', 'ObjectName', 'ObjectType', 'RA', 'DEC', 'RAoffset', 'DECoffset', 'ROToffset', 'Filter1', 'Filter2', 'DitherType', 'DitherRadius', 'DitherPhase', 'DitherTotal', 'Images', 'IntegrationTime', 'Comment1', 'Comment2'])

ROT = 48
############################################################

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

def CustomScript(Offset):

    if int(Offset[15]) <= 0 :
        Offset[15] = '1'

    Priority = Offset[0]
    Observer = Offset[2]
    ObjectName = Offset[3]
    ObjectType = Offset[4]
    RA = Offset[5]
    DEC = Offset[6]
    RAoffset = Offset[7]
    DECoffset = Offset[8]
    ROToffset = Offset[9]
    Filter1 = Offset[10]
    Filter2 = Offset[11]
    DitherType = Offset[12]
    DitherRadius = Offset[13]
    DitherPhase = Offset[14]
    DitherTotal = Offset[15]
    Images = Offset[16]
    IntegrationTime = Offset[17]
    Comment1 = Offset[18]
    Comment2 = Offset[19]


    print('[ Offset values @',OffsetName,']')
    print('**********************************')
    print('1.  Priority         :',Offset[0])
    print('2.  BlockID          :',BlockID)
    print('3.  Observer         :',Offset[2])
    print('4.  ObjectName       :',Offset[3])
    print('5.  ObjectType       :',Offset[4])
    print('6.  RA               :',Offset[5])
    print('7.  DEC              :',Offset[6])
    print('8.  RAoffset         :',Offset[7])
    print('9.  DECoffset        :',Offset[8])
    print('10. ROToffset        :',Offset[9])
    print('11. Filter1          :',Offset[10])
    print('12. Filter2          :',Offset[11])
    print('13. DitherType       :',Offset[12])
    print('14. DitherRadius     :',Offset[13])
    print('15. DitherPhase      :',Offset[14])
    print('16. DitherTotal      :',Offset[15])
    print('17. Images           :',Offset[16])
    print('18. IntegrationTime  :',Offset[17])
    print('19. Comment1         :',Offset[18])
    print('20. Comment2         :',Offset[19])
    print('********************************** \n')


    while True:
        print('Do you want to change ObjectName?\nPress y (yes) or n (no).')
        yn = fun.YesNo()
        while not yn == 'y' and not yn == 'n':
            print('')
            print('Press y (yes) or n (no).')
            yn = fun.YesNo()

        if yn == 'y':
            ObjectName = CheckValue(fun.AddObjectName())

        elif yn == 'n':
            ObjectName = Offset[3]

        print('Do you want to change ObjectType?\nPress y (yes) or n (no).')
        yn = fun.YesNo()
        while not yn == 'y' and not yn == 'n':
            print('')
            print('Press y (yes) or n (no).')
            yn = fun.YesNo()

        if yn == 'y':
            ObjectType = CheckValue(fun.AddObjectType())

        elif yn == 'n':
            ObjectType = Offset[4]

        print('Please set Priority, RA and DEC.\n')
        Priority = CheckValue(fun.AddPriority())
        RA = CheckValue(fun.AddRA())
        DEC = CheckValue(fun.AddDEC())

        print('[ Latest values @',OffsetName,']')
        print('**********************************')
        print('1.  Priority         :',Priority)
        print('2.  BlockID          :',BlockID)
        print('3.  Observer         :',Offset[2])
        print('4.  ObjectName       :',ObjectName)
        print('5.  ObjectType       :',ObjectType)
        print('6.  RA               :',RA)
        print('7.  DEC              :',DEC)
        print('8.  RAoffset         :',Offset[7])
        print('9.  DECoffset        :',Offset[8])
        print('10. ROToffset        :',Offset[9])
        print('11. Filter1          :',Offset[10])
        print('12. Filter2          :',Offset[11])
        print('13. DitherType       :',Offset[12])
        print('14. DitherRadius     :',Offset[13])
        print('15. DitherPhase      :',Offset[14])
        print('16. DitherTotal      :',Offset[15])
        print('17. Images           :',Offset[16])
        print('18. IntegrationTime  :',Offset[17])
        print('19. Comment1         :',Offset[18])
        print('20. Comment2         :',Offset[19])
        print('********************************** \n')

        print('Are Priority, RA and DEC perfect?\nPress y (yes) or n (no).')
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
            print('')
            continue;

    while True:
        print("Press number you want change and Enter-Key. (Except for 2.) \nPress 'e' when you finish your selection.")
        arr = np.empty([0])
        while True:
            n = input('Enter:')
            if n == 'e':
                break;
            else:
                try:
                    ni = int(n)
                except:
                    ni = 0.0
                    print('Only number!')
                add = np.array([ni])
                arr = np.r_[arr,add]

        for i in list(arr):
            if i == 1.0:
                Priority = CheckValue(fun.AddPriority())
            elif i == 3.0:
                Observer = CheckValue(fun.AddObserver())
            elif i == 4.0:
                ObjectName = CheckValue(fun.AddObjectName())
            elif i == 5.0:
                ObjectType = CheckValue(fun.AddObjectType())
            elif i == 6.0:
                RA = CheckValue(fun.AddRA())
            elif i == 7.0:
                DEC = CheckValue(fun.AddDEC())
            elif i == 8.0:
                RAoffset = CheckValue(fun.AddRAoffset())
            elif i == 9.0:
                DECoffset = CheckValue(fun.AddDECoffset())
            elif i == 10.0:
                ROToffset = CheckValue(fun.AddROToffset())
            elif i == 11.0:
                Filter1 = CheckValue(fun.AddFilter1())
            elif i == 12.0:
                Filter2 = CheckValue(fun.AddFilter2())
            elif i == 13.0:
                DitherType = CheckValue(fun.AddDitherType())
            elif i == 14.0:
                DitherRadius = CheckValue(fun.AddDitherRadius())
            elif i == 15.0:
                DitherPhase = CheckValue(fun.AddDitherPhase())
            elif i == 16.0:
                DitherTotal = CheckValue(fun.AddDitherTotal())
            elif i == 17.0:
                Images = CheckValue(fun.AddImages())
            elif i == 18.0:
                IntegrationTime = CheckValue(fun.AddIntegrationTime())
            elif i == 19.0:
                Comment1 = CheckValue(fun.AddComment1())
            elif i == 20.0:
                Comment2 = CheckValue(fun.AddComment2())
            else:
                pass;

        print('[ Latest values @',OffsetName,']')
        print('**********************************')
        print('1.  Priority         :',Priority)
        print('2.  BlockID          :',BlockID)
        print('3.  Observer         :',Observer)
        print('4.  ObjectName       :',ObjectName)
        print('5.  ObjectType       :',ObjectType)
        print('6.  RA               :',RA)
        print('7.  DEC              :',DEC)
        print('8.  RAoffset         :',RAoffset)
        print('9.  DECoffset        :',DECoffset)
        print('10. ROToffset        :',ROToffset)
        print('11. Filter1          :',Filter1)
        print('12. Filter2          :',Filter2)
        print('13. DitherType       :',DitherType)
        print('14. DitherRadius     :',DitherRadius)
        print('15. DitherPhase      :',DitherPhase)
        print('16. DitherTotal      :',DitherTotal)
        print('17. Images           :',Images)
        print('18. IntegrationTime  :',IntegrationTime)
        print('19. Comment1         :',Comment1)
        print('20. Comment2         :',Comment2)
        print('********************************** \n')
        print('Are latest values perfect?\nPress y (yes) or n (no).')
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
            print('')
            continue;

    writer = csv.writer(f)
    writer.writerow([Priority, BlockID, Observer, ObjectName, ObjectType, RA, DEC, RAoffset, DECoffset, ROToffset, Filter1, Filter2, DitherType, DitherRadius, DitherPhase, DitherTotal, Images, IntegrationTime, Comment1, Comment2])

    return print('Added new target!\n')

def deg2HMS(ra='', dec='', i=False):
    RA, DEC, rs, ds = '', '', '', ''
    if dec:
        if str(dec)[0] == '-':
            ds, dec = '-', abs(dec)
            deg = int(dec)
            decM = abs(int((dec-deg)*60))
        if i:
            decS = int((abs((dec-deg)*60)-decM)*60)
        else:
            decS = (abs((dec-deg)*60)-decM)*60
            decS = round(decS,1)
            DEC = '{0}{1}:{2}:{3}'.format(ds, deg, decM, decS)

    if ra:
        if str(ra)[0] == '-':
            rs, ra = '-', abs(ra)
            raH = int(ra/15)
            raM = int(((ra/15)-raH)*60)
        if i:
            raS = int(((((ra/15)-raH)*60)-raM)*60)
        else:
            raS = ((((ra/15)-raH)*60)-raM)*60
            raS = round(raS,1)
            RA = '{0}{1}:{2}:{3}'.format(rs, raH, raM, raS)

    if ra and dec:
        return (RA, DEC)
    else:
        return RA or DEC



############################################################
if len(argv) < 3:
    print('Please select offset!!')
    sys.exit()

for k in range(0,len(argv)):
    if argv[k] == '-offset':
        OffsetName = argv[k+1]
        Offset = np.loadtxt('Offset/' + OffsetName, dtype='str')

if len(argv) < 4:
    print("\nFull-Custom mode start!\n")
    BlockID = Offset[1]

    print('Mode select.\n Make new script(Custom-Making mode): y\n Add new targets(Custom-Adding mode): n \n Press y or n.')
    yn = fun.YesNo()
    print('------------------------------------ \n')
    while not yn == 'y' and not yn == 'n':
        print('')
        print('Press y (yes) or n (no).')
        yn = fun.YesNo()

    if yn == 'y':
        print('\nCustom-Making mode start!\n')
        ScriptName = CheckValue(fun.MakeScriptName())
        print('New script name is',"'",ScriptName,"'.")
        print("Let's making a new observation script!")
        print('------------------------------------ \n')

        with open('Script/' + ScriptName + '.csv' ,mode='w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            CustomScript(Offset)
            print('------------------------------------ \n')
        print('Do you continue to add targets?\nPress y (yes) or n (no).')

        n=1
        while True:
            yn = fun.YesNo()
            while not yn == 'y' and not yn == 'n':
                print('')
                print('Press y (yes) or n (no).')
                yn = fun.YesNo()

            if yn == 'y':
                print('------------------------------------ \n')
                print("\nLet's add!\n")
                print('------------------------------------ \n')
                n = n+1
                ns = str(n)
                n_zero = ns.zfill(5)
                BlockID = 'P'+n_zero
                with open('Script/' + ScriptName + '.csv', mode = 'a', newline = '') as f:
                    CustomScript(Offset)
                print('Do you continue to add targets?\nPress y (yes) or n (no).')

            elif yn == 'n':
                print('------------------------------------ \nCompleted new script!')
                break;

    elif yn == 'n':
        print('\nCustom-Adding mode start!\n')
        ScriptName = CheckValue(fun.AddScriptName())
        print('Script name is',"'",ScriptName,"'.")
        print("Let's making add new targets !")
        print('------------------------------------ \n')

        with open('Script/' + ScriptName + '.csv' ,mode='a',newline='') as f:
            writer = csv.writer(f)
            # writer.writerow(header)
            with open('Script/' + ScriptName + '.csv' ,mode='r') as file:
                lines = file.readlines()
            n_lines = str(len(lines))
            n_zero = n_lines.zfill(5)
            BlockID = 'P'+n_zero
            CustomScript(Offset)
            print('------------------------------------ \n')
        print('Do you continue to add targets?\nPress y (yes) or n (no).')

        n=1
        while True:
            yn = fun.YesNo()
            while not yn == 'y' and not yn == 'n':
                print('')
                print('Press y (yes) or n (no).')
                yn = fun.YesNo()

            if yn == 'y':
                print('------------------------------------ \n')
                print("\nLet's add!\n")
                print('------------------------------------ \n')
                n = n+1
                ns = str(n)
                n_zero = ns.zfill(5)
                BlockID = 'P'+n_zero
                with open('Script/' + ScriptName + '.csv', mode = 'a', newline = '') as f:
                    CustomScript(Offset)
                print('Do you continue to add targets?\nPress y (yes) or n (no).')

            elif yn == 'n':
                print('------------------------------------ \nCompleted new script!')
                break;

else:
    for i in range(0,len(argv)):
        if argv[i] == '-list':
            print("\nAuto-Read mode start!\n" )
            listname = argv[i+1]
            ScriptName = listname.split('.')

            for j in range(0,len(argv)):
                if argv[j] == '-add':
                    ScriptName = argv[j+1]
                    ScriptName = ScriptName.split('.')
                    print('Add to',"'",ScriptName[0],"'.")
                    with open('List/'+listname, encoding='utf-8') as f:
                        list = f.readlines()
                        numbers = len(list)

                        n = 0
                        for i, row in enumerate(list):
                            row_tmp = row.rstrip('\n')
                            row_tmp = re.split(',', row)
                            if i == 0 and row_tmp[0] == '\ufeffObserver(PI institute)':
                                continue

                            elif i == 0 and row_tmp[0] == 'Observer(PI institute)':
                                continue

                            elif row_tmp[0] == '':
                                continue

                            elif not row.isspace():
                                row = row.rstrip('\n')
                                row = re.split(',', row)
                                n = n+1
                                ns = str(n)
                                n_zero = ns.zfill(5)

                                with open('Script/' + ScriptName[0] + '.csv', mode = 'a', newline = '', encoding='utf-8') as f:

                                    Observer = row[0]

                                    ObjectType = row[2]

                                    for k in range(0,len(argv)):
                                        if argv[k] == '-lb':
                                            galactic_coord = SkyCoord(l=float(row[3])*u.degree, b=float(row[4])*u.degree, frame='galactic')
                                            equatorial_coord = galactic_coord.transform_to('icrs')
                                            RA = equatorial_coord.ra.to_string(unit=u.hour, sep=':', precision=2)
                                            DEC = equatorial_coord.dec.to_string(unit=u.degree, sep=':', precision=2)
                                            (best_rot, rot_arr, inners) = fr.search_best_rot(equatorial_coord)
                                            ROToffset = round(3600*(-best_rot+ROT),1)

                                        elif argv[k] == '-rd':
                                            if ':' in row[3] and row[4]:
                                                RA = row[3]  #* h:m:s
                                                RA = re.split(':',RA)
                                                RAh = RA[0]
                                                if str(RAh)[0] == '-':
                                                    rs = str(RAh)[0]
                                                    RAh = int(abs(float(RAh)))
                                                    RAm = RA[1]
                                                    RAs = round(float(RA[2]),1)
                                                    RA = '{0}{1}:{2}:{3}'.format(rs, RAh, RAm, RAs)
                                                else:
                                                    RAh = int(abs(float(RAh)))
                                                    RAm = RA[1]
                                                    RAs = round(float(RA[2]),1)
                                                    RA = '{0}:{1}:{2}'.format(RAh, RAm, RAs)

                                                DEC = row[4]  #* d:m:s
                                                DEC = re.split(':',DEC)
                                                DECd = DEC[0]
                                                if str(DECd)[0] == '-':
                                                    rs = str(DECd)[0]
                                                    DECd = int(abs(float(DECd)))
                                                    DECm = DEC[1]
                                                    DECs = round(float(DEC[2]),1)
                                                    DEC = '{0}{1}:{2}:{3}'.format(rs, DECd, DECm, DECs)
                                                else:
                                                    DECd = int(abs(float(DECd)))
                                                    DECm = DEC[1]
                                                    DECs = round(float(DEC[2]),1)
                                                    DEC = '{0}:{1}:{2}'.format(DECd, DECm, DECs)

                                            # else:
                                            #     RA = deg2HMS(ra= float(row[3]))  #degree
                                            #     DEC = deg2HMS(dec= float(row[4]))  #degree

                                    RAoffset = row[5]
                                    DECoffset = row[6]

                                    if row[1] == 'All-sky-grid':
                                        closest_object = fun.find_closest_object(RA, DEC, 'List/grid_20230711.txt', num_closest=1)
                                        ObjectName = f'field{int(closest_object[0][0])}'
                                        RA = closest_object[0][1]
                                        DEC = closest_object[0][2]
                                        ROToffset = round(3600*ROT,1)
                                        fun.plot_closest_objects_all_sky(ObjectName, row[3], row[4], RA, DEC, RAoffset, DECoffset)

                                    elif row[1] == 'Bulge-grid':
                                        closest_object = fun.find_closest_object(RA, DEC, 'List/PRIME_LB_20230719_deg.txt', num_closest=1)
                                        ObjectName = f'GB{int(closest_object[0][0])}'
                                        RA = closest_object[0][1]
                                        DEC = closest_object[0][2]
                                        ROToffset = closest_object[0][3]
                                        fun.plot_closest_objects_bulge(ObjectName, row[3], row[4], RA, DEC, RAoffset, DECoffset, ROT*3600-ROToffset)

                                    else :
                                        ObjectName = row[1]
                                        ROToffset = round(3600*ROT,1)

                                    Filter1 = row[7]
                                    Filter2 = row[8]
                                    DitherType = row[9]
                                    DitherRadius = row[10]
                                    DitherPhase = row[11]
                                    DitherTotal = row[12]
                                    Images = row[13]
                                    IntegrationTime = 0.1*math.floor(10*float(row[14]))
                                    Comment1 = row[15]
                                    Comment2 = row[16]

                                    Priority = Offset[0]
                                    BlockID = 'P'+n_zero
                                    # Observer = Offset[2]
                                    #ObjectName = Offset[3]
                                    # ObjectType = Offset[4]
                                    #RA = Offset[5]
                                    #DEC = Offset[6]
                                    # RAoffset = Offset[7]
                                    # DECoffset = Offset[8]
                                    # ROToffset = Offset[9]
                                    # Filter1 = Offset[10]
                                    # Filter2 = Offset[11]
                                    # DitherType = Offset[12]
                                    # DitherRadius = Offset[13]
                                    # DitherPhase = Offset[14]
                                    # DitherTotal = Offset[15]
                                    # Images = Offset[16]
                                    # IntegrationTime = Offset[17]
                                    # Comment1 = Offset[18]
                                    # Comment2 = Offset[19]

                                    writer = csv.writer(f)
                                    writer.writerow([Priority, BlockID, Observer, ObjectName, ObjectType, RA, DEC, RAoffset, DECoffset, ROToffset, Filter1, Filter2, DitherType, DitherRadius, DitherPhase, DitherTotal, Images, IntegrationTime, Comment1, Comment2])
                        print('------------------------------------ \nCompleted new script!')
                        sys.exit()


            print('New script name is',"'",ScriptName[0],"'.")
            command = ['rm','-rf', 'Script/'+ ScriptName[0]+'.csv']
            subprocess.call(command)
            with open('Script/' + ScriptName[0] + '.csv', mode = 'a', newline = '', encoding='utf-8') as F:
                writer = csv.writer(F)
                writer.writerow(header)
                with open('List/'+listname, encoding='utf-8') as f:
                    list = f.readlines()
                    numbers = len(list)

                    n = 0
                    for i, row in enumerate(list):
                        row_tmp = row.rstrip('\n')
                        row_tmp = re.split(',', row)
                        if i == 0 and row_tmp[0] == '\ufeffObserver(PI institute)':
                            continue

                        elif i == 0 and row_tmp[0] == 'Observer(PI institute)':
                            continue

                        elif row_tmp[0] == '':
                            continue

                        elif not row.isspace():
                            row = row.rstrip('\n')
                            row = re.split(',', row)
                            n = n+1
                            ns = str(n)
                            n_zero = ns.zfill(5)

#########################################################################
###########################　Read values from a list. ###################
#########################################################################
                            Observer = row[0]

                            if OffsetName == 'bulge.txt':
                                ObjectName = 'GB' + row[1]
                            else :
                                ObjectName = row[1]

                            ObjectType = row[2]

                            for k in range(0,len(argv)):
                                if argv[k] == '-lb':
                                    galactic_coord = SkyCoord(l=float(row[3])*u.degree, b=float(row[4])*u.degree, frame='galactic')
                                    equatorial_coord = galactic_coord.transform_to('icrs')
                                    RA = equatorial_coord.ra.to_string(unit=u.hour, sep=':', precision=2)
                                    DEC = equatorial_coord.dec.to_string(unit=u.degree, sep=':', precision=2)
                                    (best_rot, rot_arr, inners) = fr.search_best_rot(equatorial_coord)
                                    ROToffset = round(3600*(-best_rot+ROT),1)

                                elif argv[k] == '-rd':
                                    if ':' in row[3] and row[4]:
                                        RA = row[3]  #h:m:s
                                        RA = re.split(':',RA)
                                        RAh = RA[0]
                                        if str(RAh)[0] == '-':
                                            rs = str(RAh)[0]
                                            RAh = int(abs(float(RAh)))
                                            RAm = RA[1]
                                            RAs = round(float(RA[2]),1)
                                            RA = '{0}{1}:{2}:{3}'.format(rs, RAh, RAm, RAs)
                                        else:
                                            RAh = int(abs(float(RAh)))
                                            RAm = RA[1]
                                            RAs = round(float(RA[2]),1)
                                            RA = '{0}:{1}:{2}'.format(RAh, RAm, RAs)

                                        DEC = row[4]  #d:m:s
                                        DEC = re.split(':',DEC)
                                        DECd = DEC[0]
                                        if str(DECd)[0] == '-':
                                            rs = str(DECd)[0]
                                            DECd = int(abs(float(DECd)))
                                            DECm = DEC[1]
                                            DECs = round(float(DEC[2]),1)
                                            DEC = '{0}{1}:{2}:{3}'.format(rs, DECd, DECm, DECs)
                                        else:
                                            DECd = int(abs(float(DECd)))
                                            DECm = DEC[1]
                                            DECs = round(float(DEC[2]),1)
                                            DEC = '{0}:{1}:{2}'.format(DECd, DECm, DECs)

                                    # else:
                                    #     RA = deg2HMS(ra= float(row[3]))  #degree
                                    #     DEC = deg2HMS(dec= float(row[4]))  #degree

                            RAoffset = row[5]
                            DECoffset = row[6]

                            if row[1] == 'All-sky-grid':
                                closest_object = fun.find_closest_object(RA, DEC, 'List/grid_20230711.txt', num_closest=1)
                                ObjectName = f'field{int(closest_object[0][0])}'
                                RA = closest_object[0][1]
                                DEC = closest_object[0][2]
                                ROToffset = round(3600*ROT,1)
                                fun.plot_closest_objects_all_sky(ObjectName, row[3], row[4], RA, DEC, RAoffset, DECoffset)

                            elif row[1] == 'Bulge-grid':
                                closest_object = fun.find_closest_object(RA, DEC, 'List/PRIME_LB_20230719_deg.txt', num_closest=1)
                                ObjectName = f'GB{int(closest_object[0][0])}'
                                RA = closest_object[0][1]
                                DEC = closest_object[0][2]
                                ROToffset = closest_object[0][3]
                                fun.plot_closest_objects_bulge(ObjectName, row[3], row[4], RA, DEC, RAoffset, DECoffset, ROT*3600-ROToffset)

                            else :
                                ObjectName = row[1]
                                ROToffset = round(3600*ROT,1)

                            Filter1 = row[7]
                            Filter2 = row[8]
                            DitherType = row[9]
                            DitherRadius = row[10]
                            DitherPhase = row[11]
                            DitherTotal = row[12]
                            Images = row[13]
                            IntegrationTime = 0.1*math.floor(10*float(row[14]))
                            Comment1 = row[15]
                            Comment2 = row[16]

#########################################################################
#########################################################################


#########################################################################
###########################　Read values from a offset. #################
#########################################################################

                            Priority = Offset[0]
                            BlockID = 'P'+n_zero
                            # Observer = Offset[2]
                            #ObjectName = Offset[3]
                            # ObjectType = Offset[4]
                            #RA = Offset[5]
                            #DEC = Offset[6]
                            # RAoffset = Offset[7]
                            # DECoffset = Offset[8]
                            # ROToffset = Offset[9]
                            # Filter1 = Offset[10]
                            # Filter2 = Offset[11]
                            # DitherType = Offset[12]
                            # DitherRadius = Offset[13]
                            # DitherPhase = Offset[14]
                            # DitherTotal = Offset[15]
                            # Images = Offset[16]
                            # IntegrationTime = Offset[17]
                            # Comment1 = Offset[18]
                            # Comment2 = Offset[19]
#########################################################################
#########################################################################

                            writer = csv.writer(F)
                            writer.writerow([Priority, BlockID, Observer, ObjectName, ObjectType, RA, DEC, RAoffset, DECoffset, ROToffset, Filter1, Filter2, DitherType, DitherRadius, DitherPhase, DitherTotal, Images, IntegrationTime, Comment1, Comment2])
                print('------------------------------------ \nCompleted new script!!')
