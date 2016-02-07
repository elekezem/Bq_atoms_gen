#
# Author:MAKE_DI Institute:University of York

import csv


ix = []
iy = []
iz = []
siso = []
br = 0.5291772083


def drange(start, stop, step):
    R = []
    r = start
    while r < stop:
        yield r
        R.append(r)
        r += step
    return R


def grid_gen(x_start, x_stop, y_start, y_stop, z_start, z_stop, delta):
    for x in drange(x_start, x_stop, delta):
        for y in drange(y_start, y_stop, delta):
            for z in drange(z_start, z_stop, delta):
                ix.append("%.6f" % round(x, 6))
                iy.append("%.6f" % round(y, 6))
                iz.append("%.6f" % round(z, 6))
    return ix, iy, iz


########################################################################################
grid_gen(-3.5, 3.5, 0.0, 4.5, -3.0, 4.0, 0.5)
print('Total Bq atoms number is', len(ix))
with open('cube_grid', 'w', newline='') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter='\t',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(ix)):
        cubewriter.writerow([ix[i], iy[i], iz[i]])
