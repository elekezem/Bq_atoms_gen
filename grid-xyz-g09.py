# --------------------------------Import----------------------------------------#
import csv

max_bq_num = 95
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
        yield l[i:i+n]


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
                       |______|  Author:MAKE_DI Institute:University of York           |______|   2016/02/04

 _______   ______   .______           _______   ___     ___
|   ____| /  __  \  |   _  \         /  _____| / _ \   / _ /
|  |__   |  |  |  | |  |_)  |       |  |  __  | | | | | (_) |
|   __|  |  |  |  | |      /        |  | |_ | | | | |  \__, |
|  |     |  `--'  | |  |\  \----.   |  |__| | | |_| |    / /
|__|      \______/  | _| `._____|    \______|  \___/    /_/

    '''
    print(logo_string)


# --------------------------------Main----------------------------------------#
def main():

    print_logo()
    # x_start, x_stop, y_start, y_stop, z_start, z_stop, delta
    grid_gen(-3.5, 3.5, 0.0, 4.5, -3.0, 4.0, 0.5)
    chunks_by_bq = list(chunks(ix, max_bq_num))

    print('Total Bq atoms number is', len(ix))
    print('Total Files Number is', len(chunks_by_bq))
    print('Last file Bq number is', len(chunks_by_bq[-1]))

    for i in range(len(chunks_by_bq)):
        # set name and extension for import file:run for g09;mol for dalton

        with open("{}.run".format("%06d" % i), "w") as csv_file:
            cube_writer = csv.writer(csv_file, delimiter='\t')

            # set cores number to calculate
            cube_writer.writerow(['%NProc=2'])

            # set mem size to calculate
            cube_writer.writerow(['%Mem=2Gb'])

            # g09 key words
            cube_writer.writerow(['# HF/6-311++G(d,p) SCF(Tight) NMR CPHF(Separate) Test'])

            # space line
            cube_writer.writerow([])

            # job title
            cube_writer.writerow(['C9H9+ HF/6-311++G(d,p) nmr partial 3d grid'])

            # space line
            cube_writer.writerow([])

            # eletron
            cube_writer.writerow(['+1 1'])

            # Geo
            cube_writer.writerow(['C,0,0.,0.,1.645014194'])
            cube_writer.writerow(['C,0,0.4905022324,1.2427684773,1.1554414148'])
            cube_writer.writerow(['C,0,-0.4905022324,-1.2427684773,1.1554414148'])
            cube_writer.writerow(['C,0,0.0100585215,2.0928052569,0.1040785875'])
            cube_writer.writerow(['C,0,-0.0100585215,-2.0928052569,0.1040785875'])
            cube_writer.writerow(['C,0,-0.8152087457,1.6410894083,-0.9354914584'])
            cube_writer.writerow(['C,0,0.8152087457,-1.6410894083,-0.9354914584'])
            cube_writer.writerow(['C,0,-0.6569284614,0.2832859329,-1.251946014'])
            cube_writer.writerow(['C,0,0.6569284614,-0.2832859329,-1.251946014'])
            cube_writer.writerow(['H,0,0.,0.,2.7459418542'])
            cube_writer.writerow(['H,0,1.0699783805,1.7858874614,1.9137457041'])
            cube_writer.writerow(['H,0,-1.0699783805,-1.7858874614,1.9137457041'])
            cube_writer.writerow(['H,0,0.12964425,3.1677255378,0.2859658405'])
            cube_writer.writerow(['H,0,-0.12964425,-3.1677255378,0.2859658405'])
            cube_writer.writerow(['H,0,-1.5936377795,2.2790433661,-1.3665504299'])
            cube_writer.writerow(['H,0,1.5936377795,-2.2790433661,-1.3665504299'])
            cube_writer.writerow(['H,0,-1.490812806,-0.3325910524,-1.6109751404'])
            cube_writer.writerow(['H,0,1.490812806,0.3325910524,-1.6109751404'])

            # space line
            cube_writer.writerow([])

            # set Bq atom coord in number of max_bq_num
            for j in range(len(chunks_by_bq[i])):
                cube_writer.writerow(['Bq', '0',
                                      ix[max_bq_num*i+j],
                                      iy[max_bq_num*i+j],
                                      iz[max_bq_num*i+j]])
            cube_writer.writerow([])

            # set weak conductivity with bq
            for c in range(len(chunks_by_bq[i]) + atoms_num):
                cube_writer.writerow([c+1])
            cube_writer.writerow([])
            csv_file.close()

if __name__ == '__main__':
    main()

