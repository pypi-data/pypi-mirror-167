
import time
from heinlein import load_dataset
import astropy.units as u
des_center = (13.4349,-20.2091)
hsc_center = (141.23246, 2.32358)
des_mutli_center = (19.546018,  -28.189612)
radius = 120*u.arcsec


setup_start = time.time()
d = load_dataset("hsc")

setup_end = time.time()
print(f"Setup took {setup_end - setup_start} seconds")


get_start = time.time()
a = d.cone_search(hsc_center, radius, dtypes=["catalog", "mask"])
get_end = time.time()

print(f"Get took {get_end - get_start} seconds!")


start = time.time()
masked = a["catalog"][a["mask"]]
end = time.time()
print(f"Masking took {end - start} seconds")

get_start = time.time()
a = d.cone_search(hsc_center, radius, dtypes=["catalog", "mask"])
get_end = time.time()

print(f"Get took {get_end - get_start} seconds!")


import matplotlib.pyplot as plt
plt.scatter(a["catalog"]['ra'], a["catalog"]["dec"], c="red")
plt.scatter(masked["ra"], masked["dec"], c="blue")
plt.show()

