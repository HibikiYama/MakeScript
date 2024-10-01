import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
from astropy.coordinates import SkyCoord
from astropy.coordinates import Angle
from astropy import units as u
from astropy.io import ascii

def MakeScriptName():
    print('New script name is ...')
    name = input('Enter:')
    print('')
    return name

def AddScriptName():
    print('Script name is ...')
    name = input('Enter:')
    print('')
    return name

def YesNo():
    yesno = input('Enter:')
    return yesno

def AddPriority():
    print('Priority is ...')
    Priority = input('Enter:')
    print('')
    return Priority

def AddBlockID():
    print('BlockID is ...')
    BlockID = input('Enter:')
    print('')
    return BlockID

def AddObserver():
    print('Observer is ...')
    Observer = input('Enter:')
    print('')
    return Observer

def AddObjectName():
    print('ObjectName is ...')
    ObjectName = input('Enter:')
    print('')
    return ObjectName

def AddObjectType():
    print('ObjectType is ...')
    ObjectType = input('Enter:')
    print('')
    return ObjectType

def AddRA():
    print('RA is ...')
    RA = input('Enter:')
    print('')
    return RA

def AddDEC():
    print('DEC is ...')
    DEC = input('Enter:')
    print('')
    return DEC

def AddRAoffset():
    print('RAoffset is ...')
    RAoffset = input('Enter:')
    print('')
    return RAoffset

def AddDECoffset():
    print('DECoffset is ...')
    DECoffset = input('Enter:')
    print('')
    return DECoffset

def AddROToffset():
    print('ROToffset is ...')
    ROToffset = input('Enter')
    print('')
    return ROToffset

def AddFilter1():
    print('Filter1 is ...')
    Filter1 = input('Enter:')
    print('')
    return Filter1

def AddFilter2():
    print('Filter2 is ...')
    Filter2 = input('Enter:')
    print('')
    return Filter2

def AddDitherType():
    print('DitherType is ...')
    DitherType = input('Enter:')
    print('')
    return DitherType

def AddDitherRadius():
    print('DitherRadius is ...')
    while True:
        DitherRadius = input('Enter:')
        if int(DitherRadius) >=0:
            print('')
            break;
        else :
            print('Please set a value greater than or equal to 0.')
            continue;
    return DitherRadius

def AddDitherPhase():
    print('DitherPhase is ...')
    while True:
        DitherPhase = input('Enter:')
        if int(DitherPhase) > 0:
            print('')
            break;
        else :
            print('Please set a value greater than or equal to 1.')
            continue;
    return DitherPhase

def AddDitherTotal():
    print('DitherTotal is ...')
    while True:
        DitherTotal = input('Enter:')
        if int(DitherTotal) > 0:
            print('')
            break;
        else :
            print('Please set a value greater than or equal to 1.')
            continue;
    return DitherTotal

def AddImages():
    print('Images is ...')
    while True:
        Images = input('Enter:')
        if int(Images) > 0:
            print('')
            break;
        else :
            print('Please set a value greater than or equal to 1.')
            continue;
    return Images

def AddIntegrationTime():
    print('IntegrationTime is ...')
    while True:
        IntegrationTime = input('Enter:')
        if int(IntegrationTime) > 0:
            print('')
            break;
        else :
            print('Please set a value greater than or equal to 1.')
            continue;
    return IntegrationTime

def AddComment1():
    print('Comment1 is ...')
    Comment1 = input('Enter:')
    print('')
    return Comment1

def AddComment2():
    print('Comment2 is ...')
    Comment2 = input('Enter:')
    print('')
    return Comment2

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
    min = int((angle - deg) * 60)
    sec = int((angle - deg - min/60) * 3600)

    return f"{deg:02d}:{abs(min):02d}:{abs(sec):05.2f}"

def calc_extend_ratio(width, dec):
    a = 2*np.pi*((90-np.abs(dec))/360)
    R = (np.arccos(np.sin(np.deg2rad(width))))/(np.arccos(np.sin(np.deg2rad(width))*np.sin(a)**2+np.cos(a)**2))
    return R

def calc_dec_correction(width_extended, dec):
    dec_correction = (1-np.cos(np.deg2rad(width_extended)))*np.sin(np.deg2rad(dec))
    return dec_correction

def calc_rotation(x, y, degree, x_c=0, y_c=0):
    rad = np.deg2rad(degree)
    x_r = (x-x_c)*np.cos(rad) - (y-y_c)*np.sin(rad) + x_c
    y_r = (x-x_c)*np.sin(rad) + (y-y_c)*np.cos(rad) + y_c
    return x_r, y_r

def lb2radec(l, b):
    galactic_coord = SkyCoord(l=float(l)*u.degree, b=float(b)*u.degree, frame='galactic')
    equatorial_coord = galactic_coord.transform_to('icrs')
    RA = equatorial_coord.ra.deg
    DEC = equatorial_coord.dec.deg
    return RA, DEC

def find_closest_object(ra, dec, csv_path, num_closest=20):
    #*CSVを読み込む
    df = pd.read_table(csv_path, sep=" ", header=None)
    #*RA, DECが適切な範囲内にある行のみを保持
    df = df[df[1].between(0, 360)]
    df = df[df[2].between(-90, 90)]

    ra_deg_target = hms_to_deg(ra)
    dec_deg_target = dms_to_deg(dec)

    # df = df[df[1].between(ra_deg_target-90, ra_deg_target+90)]
    df = df[df[2].between(dec_deg_target-10, dec_deg_target+10)]

    #*天球座標を作成
    df_coords = SkyCoord(df[1], df[2], frame='icrs', unit=(u.deg, u.deg))
    target_coord = SkyCoord(ra, dec, frame='icrs', unit=(u.hourangle, u.deg))

    #*距離を計算
    dists = target_coord.separation(df_coords)

    #*距離でソート
    df['dist'] = dists.deg
    df = df.sort_values('dist')

    #*最も近いnum_closest個のオブジェクトを取得
    # if np.abs(dec_deg_target) < 80:
    #   num_closest=4
    # else :
    #   num_closest=8
    closest_objects = df.head(num_closest)

    # # RA, DECを元の形式に戻す
    # closest_objects['RA'] = closest_objects['RA'].apply(deg_to_hms)
    # closest_objects['DEC'] = closest_objects['DEC'].apply(deg_to_dms)

    closest_objects = np.array(closest_objects).tolist()

    closest_objects[0][1] = deg_to_hms(closest_objects[0][1])
    closest_objects[0][2] = deg_to_dms(closest_objects[0][2])

    return closest_objects

def plot_closest_objects_all_sky(Object_name, RA_target, DEC_target, RA_closest, DEC_closest, RAoffset, DECoffset):
    pix_scale = 0.5 #*["]
    n_pix = 4096 #*[pix]
    gap_pix = 490 #*[pix]
    gap = gap_pix*pix_scale

    fig, ax = plt.subplots(figsize=(6,6))

    RA_target = hms_to_deg(RA_target)
    DEC_target = dms_to_deg(DEC_target)
    RA_closest = hms_to_deg(RA_closest)
    DEC_closest = dms_to_deg(DEC_closest)

    if RAoffset == '0' and DECoffset == '0':
        ax.scatter(RA_target, DEC_target, color='black', label='target', marker='*')
    else:
        ax.scatter(RA_target, DEC_target, color='red', label='target', marker='*')

    RA_det, DEC_det = RA_closest+int(RAoffset)/3600, DEC_closest+int(DECoffset)/3600
    rect_width = (n_pix*pix_scale)/3600 #[deg]
    rect_height = (n_pix*pix_scale)/3600 #[deg]
    gap_deg = gap/3600 #[deg]

    dec_u = DEC_det+rect_height+gap_deg/2
    dec_d = DEC_det-rect_height-gap_deg/2

    R_u = calc_extend_ratio(2*rect_width+gap_deg, dec_u)
    R_d = calc_extend_ratio(2*rect_width+gap_deg, dec_d)
    R_gap_u = calc_extend_ratio(gap_deg, dec_u)
    R_gap_mu = calc_extend_ratio(gap_deg, DEC_det+gap_deg/2)
    R_mu = calc_extend_ratio(2*rect_width+gap_deg, DEC_det+gap_deg/2)
    R_gap_md = calc_extend_ratio(gap_deg, DEC_det-gap_deg/2)
    R_md = calc_extend_ratio(2*rect_width+gap_deg, DEC_det-gap_deg/2)
    R_gap_d = calc_extend_ratio(gap_deg, dec_d)

    width_u = (2*rect_width+gap_deg)*R_u
    width_d = (2*rect_width+gap_deg)*R_d

    width_gap_u = (gap_deg)*R_gap_u
    width_gap_mu = (gap_deg)*R_gap_mu
    width_mu = (2*rect_width+gap_deg)*R_mu
    width_gap_md = (gap_deg)*R_gap_md
    width_md = (2*rect_width+gap_deg)*R_md
    width_gap_d = (gap_deg)*R_gap_d

    dec_corr_u = calc_dec_correction(2*width_u/2, dec_u)
    dec_corr_mu = calc_dec_correction(2*width_mu/2, DEC_det+gap_deg/2)
    dec_corr_md = calc_dec_correction(2*width_md/2, DEC_det-gap_deg/2)
    dec_corr_d = calc_dec_correction(2*width_d/2, dec_d)
    """
    I don't know why "2*" is needed.
    """

    rect_vertex_3 = [(RA_det-width_d/2, dec_d-dec_corr_d), (RA_det-width_md/2, DEC_det-gap_deg/2-dec_corr_md), (RA_det-width_gap_md/2, DEC_det-gap_deg/2), (RA_det-width_gap_d/2, dec_d)]
    rect_vertex_1 = [(RA_det-width_mu/2, DEC_det+gap_deg/2-dec_corr_mu), (RA_det-width_u/2, dec_u-dec_corr_u), (RA_det-width_gap_u/2, dec_u), (RA_det-width_gap_mu/2, DEC_det+gap_deg/2)]
    rect_vertex_2 = [(RA_det+width_gap_mu/2, DEC_det+gap_deg/2), (RA_det+width_gap_u/2, dec_u), (RA_det+width_u/2, dec_u-dec_corr_u), (RA_det+width_mu/2, DEC_det+gap_deg/2-dec_corr_mu)]
    rect_vertex_4 = [(RA_det+width_gap_d/2, dec_d), (RA_det+width_gap_md/2, DEC_det-gap_deg/2), (RA_det+width_md/2, DEC_det-gap_deg/2-dec_corr_md), (RA_det+width_d/2, dec_d-dec_corr_d)]

    center_3 = ((rect_vertex_3[0][0]+rect_vertex_3[1][0]+rect_vertex_3[2][0]+rect_vertex_3[3][0])/4, (rect_vertex_3[0][1]+rect_vertex_3[1][1]+rect_vertex_3[2][1]+rect_vertex_3[3][1])/4)
    center_1 = ((rect_vertex_1[0][0]+rect_vertex_1[1][0]+rect_vertex_1[2][0]+rect_vertex_1[3][0])/4, (rect_vertex_1[0][1]+rect_vertex_1[1][1]+rect_vertex_1[2][1]+rect_vertex_1[3][1])/4)
    center_2 = ((rect_vertex_2[0][0]+rect_vertex_2[1][0]+rect_vertex_2[2][0]+rect_vertex_2[3][0])/4, (rect_vertex_2[0][1]+rect_vertex_2[1][1]+rect_vertex_2[2][1]+rect_vertex_2[3][1])/4)
    center_4 = ((rect_vertex_4[0][0]+rect_vertex_4[1][0]+rect_vertex_4[2][0]+rect_vertex_4[3][0])/4, (rect_vertex_4[0][1]+rect_vertex_4[1][1]+rect_vertex_4[2][1]+rect_vertex_4[3][1])/4)

    if RAoffset == '0' and DECoffset == '0':
        FieldName = Object_name
    else:
        FieldName = Object_name+' w/ offset'

    polygon_3 = patches.Polygon(rect_vertex_3, facecolor=f'C0', alpha=0.2, label=FieldName)
    polygon_1 = patches.Polygon(rect_vertex_1, facecolor=f'C0', alpha=0.2)
    polygon_2 = patches.Polygon(rect_vertex_2, facecolor=f'C0', alpha=0.2)
    polygon_4 = patches.Polygon(rect_vertex_4, facecolor=f'C0', alpha=0.2)
    ax.add_patch(polygon_3)
    ax.add_patch(polygon_1)
    ax.add_patch(polygon_2)
    ax.add_patch(polygon_4)

    ax.text(center_3[0], center_3[1], s='C3', color=f'C0', fontsize=12)
    ax.text(center_1[0], center_1[1], s='C1', color=f'C0', fontsize=12)
    ax.text(center_2[0], center_2[1], s='C2', color=f'C0', fontsize=12)
    ax.text(center_4[0], center_4[1], s='C4', color=f'C0', fontsize=12)

    rect_vertex_GB = [lb2radec(10,-7), lb2radec(10,6.203), lb2radec(-10.405,6.203), lb2radec(-10.405,-7)]
    polygon_GB = patches.Polygon(rect_vertex_GB, facecolor='black', alpha=1.0)
    ax.add_patch(polygon_GB)
    ax.set_xlim(RA_target-1.5, RA_target+1.5)
    ax.set_ylim(DEC_target-1.5, DEC_target+1.5)
    plt.legend()
    plt.locator_params(axis='x',nbins=5)
    plt.locator_params(axis='y',nbins=5)
    x_ticks = ax.get_xticks()
    y_ticks = ax.get_yticks()
    y_ticks_dms = []
    for i in y_ticks:
        y_ticks_dms.append(deg_to_dms(i))

    plt.xticks(x_ticks,
                deg_to_hms(x_ticks))
    plt.yticks(y_ticks,
                y_ticks_dms)
    plt.xlabel('RA [h:m:s]', fontsize=12)
    plt.ylabel('Dec [d:m:s]', fontsize=12)
    ax.tick_params(labelsize=12)
    ax.invert_xaxis()
    plt.tight_layout()
    plt.show(block=False)

    response = input("After confirming the target and the optimal grid positions, press enter to continue: \n")
    plt.close(fig)

def plot_closest_objects_bulge(Object_name, RA_target, DEC_target, RA_closest, DEC_closest, RAoffset, DECoffset, rot):
    pix_scale = 0.5 #*["]
    n_pix = 4096 #*[pix]
    gap_pix = 490 #*[pix]
    gap = gap_pix*pix_scale

    fig, ax = plt.subplots(figsize=(6,6))

    RA_target = hms_to_deg(RA_target)
    DEC_target = dms_to_deg(DEC_target)
    RA_closest = hms_to_deg(RA_closest)
    DEC_closest = dms_to_deg(DEC_closest)

    if RAoffset == '0' and DECoffset == '0':
        ax.scatter(RA_target, DEC_target, color='black', label='target', marker='*')
    else:
        ax.scatter(RA_target, DEC_target, color='red', label='target', marker='*')

    RA_det, DEC_det = RA_closest+int(RAoffset)/3600, DEC_closest+int(DECoffset)/3600
    rect_width = (n_pix*pix_scale)/3600 #[deg]
    rect_height = (n_pix*pix_scale)/3600 #[deg]
    gap_deg = gap/3600 #[deg]
    rot = rot/3600 #[deg]

    dec_u = DEC_det+rect_height+gap_deg/2
    dec_d = DEC_det-rect_height-gap_deg/2

    R_u = calc_extend_ratio(2*rect_width+gap_deg, dec_u)
    R_d = calc_extend_ratio(2*rect_width+gap_deg, dec_d)
    R_gap_u = calc_extend_ratio(gap_deg, dec_u)
    R_gap_mu = calc_extend_ratio(gap_deg, DEC_det+gap_deg/2)
    R_mu = calc_extend_ratio(2*rect_width+gap_deg, DEC_det+gap_deg/2)
    R_gap_md = calc_extend_ratio(gap_deg, DEC_det-gap_deg/2)
    R_md = calc_extend_ratio(2*rect_width+gap_deg, DEC_det-gap_deg/2)
    R_gap_d = calc_extend_ratio(gap_deg, dec_d)

    width_u = (2*rect_width+gap_deg)*R_u
    width_d = (2*rect_width+gap_deg)*R_d

    width_gap_u = (gap_deg)*R_gap_u
    width_gap_mu = (gap_deg)*R_gap_mu
    width_mu = (2*rect_width+gap_deg)*R_mu
    width_gap_md = (gap_deg)*R_gap_md
    width_md = (2*rect_width+gap_deg)*R_md
    width_gap_d = (gap_deg)*R_gap_d

    dec_corr_u = calc_dec_correction(2*width_u/2, dec_u)
    dec_corr_mu = calc_dec_correction(2*width_mu/2, DEC_det+gap_deg/2)
    dec_corr_md = calc_dec_correction(2*width_md/2, DEC_det-gap_deg/2)
    dec_corr_d = calc_dec_correction(2*width_d/2, dec_d)
    """
    I don't know why "2*" is needed.
    """

    rect_vertex_3 = [(RA_det-width_d/2, dec_d-dec_corr_d), (RA_det-width_md/2, DEC_det-gap_deg/2-dec_corr_md), (RA_det-width_gap_md/2, DEC_det-gap_deg/2), (RA_det-width_gap_d/2, dec_d)]
    rect_vertex_1 = [(RA_det-width_mu/2, DEC_det+gap_deg/2-dec_corr_mu), (RA_det-width_u/2, dec_u-dec_corr_u), (RA_det-width_gap_u/2, dec_u), (RA_det-width_gap_mu/2, DEC_det+gap_deg/2)]
    rect_vertex_2 = [(RA_det+width_gap_mu/2, DEC_det+gap_deg/2), (RA_det+width_gap_u/2, dec_u), (RA_det+width_u/2, dec_u-dec_corr_u), (RA_det+width_mu/2, DEC_det+gap_deg/2-dec_corr_mu)]
    rect_vertex_4 = [(RA_det+width_gap_d/2, dec_d), (RA_det+width_gap_md/2, DEC_det-gap_deg/2), (RA_det+width_md/2, DEC_det-gap_deg/2-dec_corr_md), (RA_det+width_d/2, dec_d-dec_corr_d)]

    rect_vertex_3_rot = [(calc_rotation(rect_vertex_3[0][0], rect_vertex_3[0][1], rot, RA_det, DEC_det)), (calc_rotation(rect_vertex_3[1][0], rect_vertex_3[1][1], rot, RA_det, DEC_det)), (calc_rotation(rect_vertex_3[2][0], rect_vertex_3[2][1], rot, RA_det, DEC_det)), (calc_rotation(rect_vertex_3[3][0], rect_vertex_3[3][1], rot, RA_det, DEC_det))]
    rect_vertex_1_rot = [(calc_rotation(rect_vertex_1[0][0], rect_vertex_1[0][1], rot, RA_det, DEC_det)), (calc_rotation(rect_vertex_1[1][0], rect_vertex_1[1][1], rot, RA_det, DEC_det)), (calc_rotation(rect_vertex_1[2][0], rect_vertex_1[2][1], rot, RA_det, DEC_det)), (calc_rotation(rect_vertex_1[3][0], rect_vertex_1[3][1], rot, RA_det, DEC_det))]
    rect_vertex_2_rot = [(calc_rotation(rect_vertex_2[0][0], rect_vertex_2[0][1], rot, RA_det, DEC_det)), (calc_rotation(rect_vertex_2[1][0], rect_vertex_2[1][1], rot, RA_det, DEC_det)), (calc_rotation(rect_vertex_2[2][0], rect_vertex_2[2][1], rot, RA_det, DEC_det)), (calc_rotation(rect_vertex_2[3][0], rect_vertex_2[3][1], rot, RA_det, DEC_det))]
    rect_vertex_4_rot = [(calc_rotation(rect_vertex_4[0][0], rect_vertex_4[0][1], rot, RA_det, DEC_det)), (calc_rotation(rect_vertex_4[1][0], rect_vertex_4[1][1], rot, RA_det, DEC_det)), (calc_rotation(rect_vertex_4[2][0], rect_vertex_4[2][1], rot, RA_det, DEC_det)), (calc_rotation(rect_vertex_4[3][0], rect_vertex_4[3][1], rot, RA_det, DEC_det))]

    center_3 = ((rect_vertex_3_rot[0][0]+rect_vertex_3_rot[1][0]+rect_vertex_3_rot[2][0]+rect_vertex_3_rot[3][0])/4, (rect_vertex_3_rot[0][1]+rect_vertex_3_rot[1][1]+rect_vertex_3_rot[2][1]+rect_vertex_3_rot[3][1])/4)
    center_1 = ((rect_vertex_1_rot[0][0]+rect_vertex_1_rot[1][0]+rect_vertex_1_rot[2][0]+rect_vertex_1_rot[3][0])/4, (rect_vertex_1_rot[0][1]+rect_vertex_1_rot[1][1]+rect_vertex_1_rot[2][1]+rect_vertex_1_rot[3][1])/4)
    center_2 = ((rect_vertex_2_rot[0][0]+rect_vertex_2_rot[1][0]+rect_vertex_2_rot[2][0]+rect_vertex_2_rot[3][0])/4, (rect_vertex_2_rot[0][1]+rect_vertex_2_rot[1][1]+rect_vertex_2_rot[2][1]+rect_vertex_2_rot[3][1])/4)
    center_4 = ((rect_vertex_4_rot[0][0]+rect_vertex_4_rot[1][0]+rect_vertex_4_rot[2][0]+rect_vertex_4_rot[3][0])/4, (rect_vertex_4_rot[0][1]+rect_vertex_4_rot[1][1]+rect_vertex_4_rot[2][1]+rect_vertex_4_rot[3][1])/4)

    if RAoffset == '0' and DECoffset == '0':
        FieldName = Object_name
    else:
        FieldName = Object_name+' w/ offset'

    polygon_3 = patches.Polygon(rect_vertex_3_rot, facecolor=f'C0', alpha=0.2, label=FieldName)
    polygon_1 = patches.Polygon(rect_vertex_1_rot, facecolor=f'C0', alpha=0.2)
    polygon_2 = patches.Polygon(rect_vertex_2_rot, facecolor=f'C0', alpha=0.2)
    polygon_4 = patches.Polygon(rect_vertex_4_rot, facecolor=f'C0', alpha=0.2)

    ax.add_patch(polygon_3)
    ax.add_patch(polygon_1)
    ax.add_patch(polygon_2)
    ax.add_patch(polygon_4)

    ax.text(center_3[0], center_3[1], s='C3', color=f'C0', fontsize=12)
    ax.text(center_1[0], center_1[1], s='C1', color=f'C0', fontsize=12)
    ax.text(center_2[0], center_2[1], s='C2', color=f'C0', fontsize=12)
    ax.text(center_4[0], center_4[1], s='C4', color=f'C0', fontsize=12)

    plt.legend()
    plt.locator_params(axis='x',nbins=5)
    plt.locator_params(axis='y',nbins=5)
    x_ticks = ax.get_xticks()
    y_ticks = ax.get_yticks()
    y_ticks_dms = []
    for i in y_ticks:
        y_ticks_dms.append(deg_to_dms(i))

    plt.xticks(x_ticks,
                deg_to_hms(x_ticks))
    plt.yticks(y_ticks,
                y_ticks_dms)
    plt.xlabel('RA [h:m:s]', fontsize=12)
    plt.ylabel('Dec [d:m:s]', fontsize=12)
    ax.tick_params(labelsize=12)
    ax.invert_xaxis()
    plt.tight_layout()
    plt.show(block=False)

    response = input("After confirming the target and the optimal grid positions, press enter to continue: \n")
    plt.close(fig)

def plot_closest_objects_nogrid(Object_name, RA_target, DEC_target, RAoffset, DECoffset):
    pix_scale = 0.5 #*["]
    n_pix = 4096 #*[pix]
    gap_pix = 490 #*[pix]
    gap = gap_pix*pix_scale

    fig, ax = plt.subplots(figsize=(6,6))

    RA_target = hms_to_deg(RA_target)
    DEC_target = dms_to_deg(DEC_target)

    if RAoffset == '0' and DECoffset == '0':
        ax.scatter(RA_target, DEC_target, color='black', label=Object_name, marker='*')
    else:
        ax.scatter(RA_target, DEC_target, color='red', label=Object_name, marker='*')

    RA_det, DEC_det = RA_target+int(RAoffset)/3600, DEC_target+int(DECoffset)/3600
    rect_width = (n_pix*pix_scale)/3600 #[deg]
    rect_height = (n_pix*pix_scale)/3600 #[deg]
    gap_deg = gap/3600 #[deg]

    dec_u = DEC_det+rect_height+gap_deg/2
    dec_d = DEC_det-rect_height-gap_deg/2

    R_u = calc_extend_ratio(2*rect_width+gap_deg, dec_u)
    R_d = calc_extend_ratio(2*rect_width+gap_deg, dec_d)
    R_gap_u = calc_extend_ratio(gap_deg, dec_u)
    R_gap_mu = calc_extend_ratio(gap_deg, DEC_det+gap_deg/2)
    R_mu = calc_extend_ratio(2*rect_width+gap_deg, DEC_det+gap_deg/2)
    R_gap_md = calc_extend_ratio(gap_deg, DEC_det-gap_deg/2)
    R_md = calc_extend_ratio(2*rect_width+gap_deg, DEC_det-gap_deg/2)
    R_gap_d = calc_extend_ratio(gap_deg, dec_d)

    width_u = (2*rect_width+gap_deg)*R_u
    width_d = (2*rect_width+gap_deg)*R_d

    width_gap_u = (gap_deg)*R_gap_u
    width_gap_mu = (gap_deg)*R_gap_mu
    width_mu = (2*rect_width+gap_deg)*R_mu
    width_gap_md = (gap_deg)*R_gap_md
    width_md = (2*rect_width+gap_deg)*R_md
    width_gap_d = (gap_deg)*R_gap_d

    dec_corr_u = calc_dec_correction(2*width_u/2, dec_u)
    dec_corr_mu = calc_dec_correction(2*width_mu/2, DEC_det+gap_deg/2)
    dec_corr_md = calc_dec_correction(2*width_md/2, DEC_det-gap_deg/2)
    dec_corr_d = calc_dec_correction(2*width_d/2, dec_d)
    """
    I don't know why "2*" is needed.
    """

    rect_vertex_3 = [(RA_det-width_d/2, dec_d-dec_corr_d), (RA_det-width_md/2, DEC_det-gap_deg/2-dec_corr_md), (RA_det-width_gap_md/2, DEC_det-gap_deg/2), (RA_det-width_gap_d/2, dec_d)]
    rect_vertex_1 = [(RA_det-width_mu/2, DEC_det+gap_deg/2-dec_corr_mu), (RA_det-width_u/2, dec_u-dec_corr_u), (RA_det-width_gap_u/2, dec_u), (RA_det-width_gap_mu/2, DEC_det+gap_deg/2)]
    rect_vertex_2 = [(RA_det+width_gap_mu/2, DEC_det+gap_deg/2), (RA_det+width_gap_u/2, dec_u), (RA_det+width_u/2, dec_u-dec_corr_u), (RA_det+width_mu/2, DEC_det+gap_deg/2-dec_corr_mu)]
    rect_vertex_4 = [(RA_det+width_gap_d/2, dec_d), (RA_det+width_gap_md/2, DEC_det-gap_deg/2), (RA_det+width_md/2, DEC_det-gap_deg/2-dec_corr_md), (RA_det+width_d/2, dec_d-dec_corr_d)]

    center_3 = ((rect_vertex_3[0][0]+rect_vertex_3[1][0]+rect_vertex_3[2][0]+rect_vertex_3[3][0])/4, (rect_vertex_3[0][1]+rect_vertex_3[1][1]+rect_vertex_3[2][1]+rect_vertex_3[3][1])/4)
    center_1 = ((rect_vertex_1[0][0]+rect_vertex_1[1][0]+rect_vertex_1[2][0]+rect_vertex_1[3][0])/4, (rect_vertex_1[0][1]+rect_vertex_1[1][1]+rect_vertex_1[2][1]+rect_vertex_1[3][1])/4)
    center_2 = ((rect_vertex_2[0][0]+rect_vertex_2[1][0]+rect_vertex_2[2][0]+rect_vertex_2[3][0])/4, (rect_vertex_2[0][1]+rect_vertex_2[1][1]+rect_vertex_2[2][1]+rect_vertex_2[3][1])/4)
    center_4 = ((rect_vertex_4[0][0]+rect_vertex_4[1][0]+rect_vertex_4[2][0]+rect_vertex_4[3][0])/4, (rect_vertex_4[0][1]+rect_vertex_4[1][1]+rect_vertex_4[2][1]+rect_vertex_4[3][1])/4)

    if RAoffset == '0' and DECoffset == '0':
        FieldName = 'FOV'
    else:
        FieldName = 'FOV'+' w/ offset'

    polygon_3 = patches.Polygon(rect_vertex_3, facecolor=f'C0', alpha=0.2, label=FieldName)
    polygon_1 = patches.Polygon(rect_vertex_1, facecolor=f'C0', alpha=0.2)
    polygon_2 = patches.Polygon(rect_vertex_2, facecolor=f'C0', alpha=0.2)
    polygon_4 = patches.Polygon(rect_vertex_4, facecolor=f'C0', alpha=0.2)
    ax.add_patch(polygon_3)
    ax.add_patch(polygon_1)
    ax.add_patch(polygon_2)
    ax.add_patch(polygon_4)

    ax.text(center_3[0], center_3[1], s='C3', color=f'C0', fontsize=12)
    ax.text(center_1[0], center_1[1], s='C1', color=f'C0', fontsize=12)
    ax.text(center_2[0], center_2[1], s='C2', color=f'C0', fontsize=12)
    ax.text(center_4[0], center_4[1], s='C4', color=f'C0', fontsize=12)

    rect_vertex_GB = [lb2radec(10,-7), lb2radec(10,6.203), lb2radec(-10.405,6.203), lb2radec(-10.405,-7)]
    polygon_GB = patches.Polygon(rect_vertex_GB, facecolor='black', alpha=1.0)
    ax.add_patch(polygon_GB)
    ax.set_xlim(RA_target-1.5, RA_target+1.5)
    ax.set_ylim(DEC_target-1.5, DEC_target+1.5)
    plt.legend()
    plt.locator_params(axis='x',nbins=5)
    plt.locator_params(axis='y',nbins=5)
    x_ticks = ax.get_xticks()
    y_ticks = ax.get_yticks()
    y_ticks_dms = []
    for i in y_ticks:
        y_ticks_dms.append(deg_to_dms(i))

    plt.xticks(x_ticks,
                deg_to_hms(x_ticks))
    plt.yticks(y_ticks,
                y_ticks_dms)
    plt.xlabel('RA [h:m:s]', fontsize=12)
    plt.ylabel('Dec [d:m:s]', fontsize=12)
    ax.tick_params(labelsize=12)
    ax.invert_xaxis()
    plt.tight_layout()
    plt.show(block=False)

    response = input("After confirming the target and the optimal grid positions, press enter to continue: \n")