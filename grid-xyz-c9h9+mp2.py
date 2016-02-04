#
# Reflects the partial 3d grid for C2 c9h9+ as
# (x,y,z) -> (-x,-y,z)
# and prints GAUSSIAN cube data in x, y, z order
# (z changes fastest, followed by y and x)
import csv
import operator


ix = []
iy = []
iz = []
siso = []
br = 0.5291772083
nx = 70
ny = 90
nz = 70
delta = 0.05

def grid_gen():
    for x in range(-nx, nx + 1, 1):
        x = x * delta
        for y in range(-ny, ny + 1, 1):
            y = y * delta
            for z in range(-nz + 10, nz + 11, 1):
                z = z * delta
                ix.append(round(x, 6))
                iy.append(round(y, 6))
                iz.append(round(z, 6))
    return ix, iy, iz


########################################################################################
grid_gen()
print(len(ix))
with open('cube_grid', 'w', newline='') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter='\t',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(ix)):
        cubewriter.writerow([ix[i],iy[i],iz[i]])
    pass

