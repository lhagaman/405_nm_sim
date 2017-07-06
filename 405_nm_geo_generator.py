import math
import geoShapes as GS
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

geoFileName = './405_nm.geo'


tube_included = True
# 'air', 'water', 'mineraloil'
substance = "air"
# incident angle of beam with respect to sample in degrees
theta_i = "45"

tube_radius = 1.75 / 2
tube_wall_width = 0.125
tube_height = 2

sample_radius = 0.5
sample_thickness = 0.175

masterString = ''

##### Create the world first
world = GS.boxVolume('world', 400, 400, 400)
world.material = 'air'
world.mother = ''
world.invisible = 1
masterString = world.writeToString(masterString)

if tube_included:
    # sapphire tube
    sapphire_tube = GS.tubeVolume("sapphire_tube", tube_radius, tube_height, tube_radius - tube_wall_width)
    sapphire_tube.center = {'x':0, 'y':0, 'z':0}
    sapphire_tube.mother = 'world'
    sapphire_tube.material = 'sapphire'
    masterString = sapphire_tube.writeToString(masterString)

# sample
sample = GS.tubeVolume('sample', sample_radius, sample_thickness)
sample.center = {'x':0, 'y':0, 'z':0}
sample.rotation = [45, 90, 0]
sample.mother = 'world'
sample.material = "teflon"
masterString = sample.writeToString(masterString)

# vaccuum shell cylinder to check for reflected entering photons ?


print 'Saving file...'
geoOutFile = open(geoFileName,'w+')
geoOutFile.write(masterString)
geoOutFile.close()

