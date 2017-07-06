import math
import geoShapes as GS
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

geoFileName = './405_nm.geo'


tube_included = True
# 'air', 'water', 'mineraloil'
substance = "air"


masterString = ''

##### Create the world first
world = GS.boxVolume('world', 400, 400, 400)
world.material = 'acrylic_black'
world.mother = ''
world.invisible = 1
masterString = world.writeToString(masterString)



# air inside world

# sapphire tube

# air inside sapphire tube

# sample

# vaccuum shell cylinder to check for reflected entering photons





##### Write geo out to file.
#print masterString

print 'Saving file...'
geoOutFile = open(geoFileName,'w+')
geoOutFile.write(masterString)
geoOutFile.close()

