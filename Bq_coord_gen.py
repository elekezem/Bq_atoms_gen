#
# Author:MAKE_DI Institute:University of York

import csv


ix = []
iy = []
iz = []
br = 0.5291772083


def d_range(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


def grid_gen(x_start, x_stop, y_start, y_stop, z_start, z_stop, delta):
    for x in d_range(x_start, x_stop, delta):
        for y in d_range(y_start, y_stop, delta):
            for z in d_range(z_start, z_stop, delta):
                ix.append("%.6f" % round(x, 6))
                iy.append("%.6f" % round(y, 6))
                iz.append("%.6f" % round(z, 6))
    return ix, iy, iz


########################################################################################
# x_start, x_stop, y_start, y_stop, z_start, z_stop, delta
grid_gen(-3.5, 3.5, 0.0, 4.5, -3.0, 4.0, 0.5)
print('Total Bq atoms number is', len(ix))
with open('cube_grid', 'w', newline='') as csv_file:
    cube_writer = csv.writer(csv_file, delimiter='\t',
                             quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(ix)):
        cube_writer.writerow([ix[i], iy[i], iz[i]])
