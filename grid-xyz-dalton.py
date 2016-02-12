# --------------------------------Import----------------------------------------#
import csv

max_bq_num = 18
atoms_num = 18
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
        yield l[i:i + n]


def grid_gen(x_start, x_stop, y_start, y_stop, z_start, z_stop, delta):
    for x in d_range(x_start, x_stop, delta):
        for y in d_range(y_start, y_stop, delta):
            for z in d_range(z_start, z_stop, delta):
                ix.append("%.6f" % round(x, 6))
                iy.append("%.6f" % round(y, 6))
                iz.append("%.6f" % round(z, 6))
    return ix, iy, iz


def print_logo():
    logo_string = '''

.______     ______                ___   .___________. ______   .___  ___.      _______.       _______  _______ .__   __.  __
|   _  \   /  __  \              /   \  |           |/  __  \  |   \/   |     /       |      /  _____||   ____||  \ |  | |  |
|  |_)  | |  |  |  |            /  ^  \ `---|  |----|  |  |  | |  \  /  |    |   (----`     |  |  __  |  |__   |   \|  | |  |
|   _  <  |  |  |  |           /  /_\  \    |  |    |  |  |  | |  |\/|  |     \   \         |  | |_ | |   __|  |  . `  | |  |
|  |_)  | |  `--'  '--.       /  _____  \   |  |    |  `--'  | |  |  |  | .----)   |        |  |__| | |  |____ |  |\   | |__|
|______/   \_____\_____\_____/__/     \__\  |__|     \______/  |__|  |__| |_______/     _____\______| |_______||__| \__| (__)
                       |______|                                                        |______|   2016/02/04

 _______   ______   .______          _______       ___       __      .___________.  ______   .__   __.
|   ____| /  __  \  |   _  \        |       \     /   \     |  |     |           | /  __  \  |  \ |  |
|  |__   |  |  |  | |  |_)  |       |  .--.  |   /  ^  \    |  |     `---|  |----`|  |  |  | |   \|  |
|   __|  |  |  |  | |      /        |  |  |  |  /  /_\  \   |  |         |  |     |  |  |  | |  . `  |
|  |     |  `--'  | |  |\  \----.   |  '--'  | /  _____  \  |  `----.    |  |     |  `--'  | |  |\   |
|__|      \______/  | _| `._____|   |_______/ /__/     \__\ |_______|    |__|      \______/  |__| \__|

    '''
    print(logo_string)


# --------------------------------Main----------------------------------------#
def main():
    print_logo()
    # x_start, x_stop, y_start, y_stop, z_start, z_stop, delta
    grid_gen(-3.5, 3.5, 0.0, 4.5, -3.0, 4.0, 0.1)
    chunks_by_bq = list(chunks(ix, max_bq_num))
    print('Total Bq atoms number is', len(ix))
    print('Total Files Number is', len(chunks_by_bq))
    print('Last file Bq number is', len(chunks_by_bq[-1]))

    for i in range(len(chunks_by_bq)):
        # set name and extension for import file:run for g09;mol for dalton

        with open("c9h9+HF.6-31g.{}.mol".format("%06d" % i), "w") as csv_file:
            cube_writer = csv.writer(csv_file, delimiter=' ')

            # set cores number to calculate
            cube_writer.writerow(['ATOMBASIS'])

            # set mem size to calculate
            cube_writer.writerow(['C9H9+[CASSCF(8,9)]'])

            # space line
            cube_writer.writerow(['THIS/FILE/CREATED/BY//BQ_ATOMS_GEN/FOR/DALTON//'])

            # g09 key words
            cube_writer.writerow(['Atomtypes=5','Charge=1','Generator=1','XY','Angstrom Spherical'])

            # Geo
            cube_writer.writerow(['Charge=6.0','Atoms=1','Basis=6-31G'])

            # Geo
            cube_writer.writerow(['C','0.00000','0.00000','1.64501'])

            # Geo
            cube_writer.writerow(['Charge=6.0','Atoms=4','Basis=6-31G'])

            cube_writer.writerow(['C','0.49050','1.24277','1.15544'])
            # cube_writer.writerow(['C         -0.49050       -1.24277        1.15544'])
            cube_writer.writerow(['C','0.01006','2.09281','0.10408'])
            # cube_writer.writerow(['C         -0.01006       -2.09281        0.10408'])
            cube_writer.writerow(['C','-0.81521','1.64109','-0.93549'])
            # cube_writer.writerow(['C          0.81521       -1.64109       -0.93549'])
            cube_writer.writerow(['C','-0.65693','0.28329','-1.25195'])
            # cube_writer.writerow(['C          0.65693       -0.28329       -1.25195'])

            cube_writer.writerow(['Charge=1.0','Atoms=1','Basis=6-31G'])

            cube_writer.writerow(['H','0.00000','0.00000','2.74594'])

            cube_writer.writerow(['Charge=1.0','Atoms=4','Basis=6-31G'])

            cube_writer.writerow(['H','1.06998','1.78589','1.91375'])
            # cube_writer.writerow(['H         -1.06998       -1.78589        1.91375'])
            cube_writer.writerow(['H','0.12964','3.16773','0.28597'])
            # cube_writer.writerow(['H         -0.12964       -3.16773        0.28597'])
            cube_writer.writerow(['H','-1.59364','2.27904','-1.36655'])
            # cube_writer.writerow(['H          1.59364       -2.27904       -1.36655'])
            # cube_writer.writerow(['H         -1.49081       -0.33259       -1.61098'])
            cube_writer.writerow(['H','1.49081','0.33259','-1.61098'])

            cube_writer.writerow(['Charge=0.0','Atoms=10','Basis=pointcharge'])

            # set Bq atom coord in number of max_bq_num
            for j in range(len(chunks_by_bq[i])):
                cube_writer.writerow(["X{}".format("%02d" % j),
                                      ix[max_bq_num * i + j],
                                      iy[max_bq_num * i + j],
                                      iz[max_bq_num * i + j]])
            cube_writer.writerow(['%EOF%'])
            print('creat',"c9h9+HF.6-31g.{}.mol".format("%06d" % i))
            csv_file.close()
            # # set weak conductivity with bq
            # for c in range(len(chunks_by_bq[i]) + atoms_num):
            #     cube_writer.writerow([c+1])
            # cube_writer.writerow([])
            # csv_file.close()

    with open("run.sh", "w") as run_file:
        cube_writer = csv.writer(run_file, delimiter=' ')
        # cube_writer.writerow(['#!/bin/bash'])
        # cube_writer.writerow(['export', 'PATH=$PATH:/usr/local/dalton'])
        # cube_writer.writerow(['export', 'DALTON_TMPDIR=/home/md971/scratch'])
        # cube_writer.writerow([])
        for i in range(len(chunks_by_bq)):
            cube_writer.writerow(['dalton', '-mb', '6144', '-noarch', 'casscf.dal', "c9h9+HF.6-31g.{}.mol".format("%06d" % i)])
    run_file.close()


if __name__ == '__main__':
    main()
