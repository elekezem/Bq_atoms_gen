#
"""Author:MAKE_DI Institute:University of York"""

import csv


max_bq_num = 95
ix = []
iy = []
iz = []
br = 0.5291772083


def d_range(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step
    # return R


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]


def grid_gen(x_start, x_stop, y_start, y_stop, z_start, z_stop, delta):
    for x in d_range(x_start, x_stop, delta):
        for y in d_range(y_start, y_stop, delta):
            for z in d_range(z_start, z_stop, delta):
                ix.append("%.6f" % round(x, 6))
                iy.append("%.6f" % round(y, 6))
                iz.append("%.6f" % round(z, 6))
    return ix, iy, iz


# --------------------------------Main----------------------------------------#
grid_gen(-3.5, 3.5, 0.0, 4.5, -3.0, 4.0, 0.5)
chunks_by_bq = list(chunks(ix, max_bq_num))
print'Total Bq atoms number is', len(ix)
print'Total Files Number is ', len(chunks_by_bq)


for i in range(len(chunks_by_bq)):

    # set name and extension for import file:run for g09;mol for dalton

    with open("{}.mol".format("%06d" % i), "w") as csv_file:
        cube_writer = csv.writer(csv_file, delimiter='\t')

        # set Bq atom coord in number of max_bq_num

        for j in range(len(chunks_by_bq[1])):
            cube_writer.writerow(['Bq', ix[j], iy[j], iz[j]])

        csv_file.close()
