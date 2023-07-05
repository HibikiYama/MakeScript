from astropy import units as u
from astropy.coordinates import SkyCoord

# 銀河座標系での座標を定義
galactic_coord = SkyCoord(l=10.62*u.degree, b=41.38*u.degree, frame='galactic')

# 座標系を赤道座標系に変換
equatorial_coord = galactic_coord.transform_to('icrs')

# 赤経 (RA) を取得し、時分秒 (hms) 形式に変換
ra_hms = equatorial_coord.ra.to_string(unit=u.hour, sep=':', precision=2)
# 赤緯 (DEC) を取得し、度分秒 (dms) 形式に変換
dec_dms = equatorial_coord.dec.to_string(unit=u.degree, sep=':', precision=2)

print(f"RA: {ra_hms}, DEC: {dec_dms}")
