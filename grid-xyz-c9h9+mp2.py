#
"""Author:MAKE_DI Institute:University of York"""

import csv


max_bq_num = 95
ix = []
iy = []
iz = []
br = 0.5291772083


def drange(start, stop, step):
    R = []
    r = start
    while r < stop:
        yield r
        R.append(r)
        r += step
    return R


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]


def grid_gen(x_start, x_stop, y_start, y_stop, z_start, z_stop, delta):
    for x in drange(x_start, x_stop, delta):
        for y in drange(y_start, y_stop, delta):
            for z in drange(z_start, z_stop, delta):
                ix.append("%.6f" % round(x, 6))
                iy.append("%.6f" % round(y, 6))
                iz.append("%.6f" % round(z, 6))
    return ix, iy, iz

grid_gen(-3.5, 3.5, 0.0, 4.5, -3.0, 4.0, 0.05)
chunks_by_bq = list(chunks(ix, max_bq_num))
print('Total Bq atoms number is', len(ix))
print('Total Files Number is ', len(chunks_by_bq))


for i in range(len(chunks_by_bq)):

    # set name and extention for import file:run for g09;mol for dalton

    with open("{}.mol".format("%06d" % i), "w") as csv_file:
        cubewriter = csv.writer(csv_file, delimiter='\t')

        for j in range(len(chunks_by_bq[1])):
            cubewriter.writerow(['Bq', ix[j], iy[j], iz[j]])
        csv_file.close()