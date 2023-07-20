import matplotlib.pyplot as plt
import os
import sys
import math
import numpy as np
from scipy.spatial import distance
from astropy.coordinates import SkyCoord
from astropy import units as u


def gal_trans(l, b, l_unit="deg", b_unit="deg"):
    sky_gal = SkyCoord(l, b, frame="galactic", unit=(l_unit, b_unit))
    return sky_gal


def eq_trans(ra, dec, ra_unit="deg", dec_unit="deg"):
    sky_radec = SkyCoord(ra, dec, frame="icrs", unit=(ra_unit, dec_unit))
    return sky_radec

def trans_gal_to_eq(gal_coord):
    equational = gal_coord.transform_to("icrs")
    ra = equational.ra.deg
    dec = equational.dec.deg
    return (ra, dec)

def trans_eq_to_gal(eq_coord):
    galactic = eq_coord.transform_to("galactic")
    l = galactic.l.deg
    b = galactic.b.deg
    return (l, b)

def calc_offset(radec, angles, offsets):
    if len(angles) == len(offsets):
        coords = []
        for i in range(len(angles)):
            coord = radec.directional_offset_by(angles[i], offsets[i])
            coords.append(coord)
        return coords


def calc_distance(array1, array2):
    eucli_distance = distance.euclidean(array1, array2)
    return eucli_distance


def deg_to_dms(deg):
    degrees = int(deg)
    tmp = 60*(deg - degrees)
    minutes = int(tmp)
    seconds = tmp - minutes
    return (degrees, minutes, seconds)


def read_lblist(lb_list):
    with open(lb_list) as list:
        lines = [l.strip() for l in list.readlines()]
        l = []
        b = []
        for lb in lines:
            l.append(float(lb.split()[1]))
            b.append(float(lb.split()[2]))
        return (l, b)


def get_angset(angset_list):
    with open(angset_list, "r") as angset:
        lines = angset.readlines()
        lines = [line.strip() for line in lines]
    angles = []
    offsets = []
    for l in lines:
        (angle, offset) = l.split()
        angles.append(float(angle)*u.deg)
        offsets.append(float(offset)*u.deg)
    return (angles, offsets)


def change_lblist(eq_list):
    Ls = []
    Bs = []
    for eq in eq_list:
        (l, b) = trans_eq_to_gal(eq)
        if l > 180:
            l = l - 360
        Ls.append(l)
        Bs.append(b)
    return (Ls, Bs)


def mk_lbs_file(eq_result, outfile):
    Ls = []
    Bs = []
    with open (outfile, "a") as lb_re:
        for eq_re in eq_result:
            (l, b) = trans_eq_to_gal(eq_re)
            if l > 180:
                l = l - 360
            print (l, b, file=lb_re)



def plot_result(lb_file):
    (Ls, Bs) = read_lblist(lb_file)
    plt.plot(Ls, Bs)
    plt.show()


def check_file(out_file):
    if os.path.isfile(out_file):
        print ("remove" + " " + out_file)
        os.remove(out_file)


def mk_cangset(ver, hor, rot):
    thre = ver/hor
    theta = math.degrees(math.atan(thre))
    angles = [theta - rot, 180 - theta - rot, 180 + theta - rot, 360 - theta - rot]*u.deg
    offset = math.sqrt(ver**2 + hor**2)
    offsets = []
    for d in angles:
        offsets.append(offset)
    offsets = offsets*u.deg

    return (angles, offsets)


def search_best_rot(eq_cent):
    ver = 1.2/2
    hor = 1.2/2
    rot_arr = np.arange(0, 90, 0.1)
    inners = []
    el = [1, 0]
    eb = [0, 1]
    for rot in rot_arr:
        (angles, offsets) = mk_cangset(ver, hor, rot)
        eq_result = calc_offset(eq_cent, angles, offsets)
        (Ls, Bs) = change_lblist(eq_result)
        vec1 = [Ls[0] - Ls[1], Bs[0] - Bs[1]]
        vec2 = [Ls[1] - Ls[2], Bs[1] - Bs[2]]
        vec3 = [Ls[2] - Ls[3], Bs[2] - Bs[3]]
        vec4 = [Ls[3] - Ls[0], Bs[3] - Bs[0]]
        inner1 = np.dot(vec1, el)**2 + np.dot(vec2, eb)**2 + np.dot(vec3, el)**2 + np.dot(vec4, eb)**2
        inner2 = np.dot(vec1, eb)**2 + np.dot(vec2, el)**2 + np.dot(vec3, eb)**2 + np.dot(vec4, el)**2
        inner = min(inner1, inner2)
        inners.append(inner)
    best_rot = rot_arr[inners.index(min(inners))]

    return (best_rot, rot_arr, inners)

#def change_hmsdms(ra, dec):
#    eq = (ra, dec)
#    (ra_hms, dec_dms) = eq.to_string('hmsdms')

#    return (ra_hms, dec_dms)

if __name__ == "__main__":
    offset = 48
#    gal_coord = gal_trans(sys.argv[1], sys.argv[2])
#    gal_coord = gal_trans(0.125, -0.125)
    (l, b) = read_lblist(sys.argv[1])
    check_file("clb_results")
    check_file("lb_rot.list")
    for i in range(len(l)):
        gal_cent = gal_trans(l[i], b[i])  #trans (l,b) for skycoord format
        (ra, dec) = trans_gal_to_eq(gal_cent)  #trans (l,b) to (ra,dec)
        eq_cent = eq_trans(ra, dec)  #trans (ra,dec) for skycoord format
        print(eq_cent)
        (best_rot, rot_arr, inners) = search_best_rot(eq_cent) #search best rotation
#        (ra_hms, dec_dms) = change_hmsdms(ra, dec)
        with open ("lb_rot.list", "a") as lb_rot:
#            print (l[i], b[i], ra, dec, round(best_rot, 5), file=lb_rot)
            print (ra, dec, round(-best_rot + offset, 5), file=lb_rot)
        with open ("rot_inners", "w") as rin:
            for i in range(len(rot_arr)):
                print (rot_arr[i], inners[i], file=rin)
        (angles, offsets) = mk_cangset(1.2/2, 1.2/2, best_rot)
        eq_result = calc_offset(eq_cent, angles, offsets) #calcurate changed (ra,dec)s by using (center,angle,offset)s
        mk_lbs_file(eq_result, "clb_results")
    print ("now plot ...")
    plot_result("clb_results")



