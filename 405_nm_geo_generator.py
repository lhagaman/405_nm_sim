import math
import geoShapes as GS
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

geoFileName = './405_nm.geo'

sample_included = True
tube_included = False
tube_caps_included = False
laser_included = False
table_included = False
post_included = False
center_included = False

sample_surface_centered = True

collecting_surfaces_included = False
num_collecting_surfaces = 180
collecting_surface_distance = 5.5
collecting_surface_thickness = 0.01
collecting_surface_height = 0.5

# 'air', 'water', 'mineraloil'
substance = "air"
# incident angle of beam with respect to sample in degrees
theta_i = 60

tube_radius = 1
tube_wall_width = 0.125
tube_height = 1.8

sample_radius = 0.5
sample_thickness = 0.2

tube_cap_radius = 2.25 / 2
upper_tube_cap_height = 0.7
lower_tube_cap_height = 0.9

laser_radius = 1.4 / 2
laser_length = 5
dist_from_laser_to_sample = 8

dist_from_table_to_sample = 8

post_radius = 0.5 / 2

masterString = ''

##### Create the world first
world = GS.boxVolume('world', 400, 400, 400)
world.material = 'air'
world.mother = ''
world.invisible = 1
masterString = world.writeToString(masterString)

if tube_included:
    sapphire_tube = GS.tubeVolume("sapphire_tube", tube_radius, tube_height, tube_radius - tube_wall_width)
    sapphire_tube.colorVect = [0.658954714849, 0.802189023832, 0.994216568893, 0.2]
    sapphire_tube.center = {'x': 0, 'y': 0, 'z': 0}
    sapphire_tube.mother = 'world'
    sapphire_tube.material = 'sapphire'
    masterString = sapphire_tube.writeToString(masterString)

if sample_included:
    sample = GS.tubeVolume('sample', sample_radius, sample_thickness)
    sample.colorVect = [0.976892196027, 0.408361008099, 0.504698048762, 0.8]
    if not sample_surface_centered:
        sample.center = {'x': 0, 'y': 0, 'z': 0}
    else:
        sample.center = {'x': sample_thickness / 2 * math.cos(theta_i * math.pi / 180), 'y': sample_thickness / 2 * math.sin(theta_i * math.pi / 180), 'z': 0}
    sample.rotation = [90, 90 + theta_i, 0]
    sample.material = 'stainless_steel'
    masterString = sample.writeToString(masterString)

if center_included:
    center = GS.tubeVolume('center', 0.02, 4)
    center.center = {'x': 0, 'y': 0, 'z': 0}
    center.material = 'air'
    center.colorVect = [1, 1, 1, 1]
    masterString = center.writeToString(masterString)

if collecting_surfaces_included:
    for i in range(num_collecting_surfaces):
        phi_start = 180.0 / num_collecting_surfaces * i + 180
        phi_delta = 180.0 / num_collecting_surfaces
        current_collecting_surface = GS.tubeVolume('collecting_surface_' + str(i),
                                                   collecting_surface_distance + collecting_surface_thickness,
                                                   collecting_surface_height, collecting_surface_distance, phi_start,
                                                   phi_delta)
        current_collecting_surface.material = 'air'
        current_collecting_surface.center = {'x': 0, 'y': 0, 'z': 0}
        if i == 0:
            current_collecting_surface.colorVect = [1,1,1,1]
        masterString = current_collecting_surface.writeToString(masterString)

if tube_caps_included:
    upper_tube_cap = GS.tubeVolume('upper_tube_cap', tube_cap_radius, upper_tube_cap_height)
    lower_tube_cap = GS.tubeVolume('lower_tube_cap', tube_cap_radius, lower_tube_cap_height)
    upper_tube_cap.center = {'x': 0, 'y': 0, 'z': (tube_height + upper_tube_cap_height) / 2}
    lower_tube_cap.center = {'x': 0, 'y': 0, 'z': -(tube_height + lower_tube_cap_height) / 2}
    upper_tube_cap.material = 'aluminum'
    lower_tube_cap.material = 'aluminum'
    upper_tube_cap.colorVect = [0.2, 0.8, 0.6, 0.2]
    lower_tube_cap.colorVect = [0.2, 0.8, 0.6, 0.2]
    masterString = upper_tube_cap.writeToString(masterString)
    masterString = lower_tube_cap.writeToString(masterString)

if laser_included:
    laser = GS.tubeVolume('laser', laser_radius, laser_length)
    laser.center = {'x': -(laser_length / 2. + dist_from_laser_to_sample), 'y': 0, 'z': 0}
    laser.rotation = [0, 90, 0]
    laser.mother = 'world'
    laser.material = 'stainless_steel'
    laser.colorVect = [0.5, 0.5, 0, 0.5]
    masterString = laser.writeToString(masterString)

if table_included:
    table = GS.boxVolume('table', 24, 24, 4)
    table.center = {'x': 0, 'y': 0, 'z': -dist_from_table_to_sample}
    table.mother = 'world'
    table.material = 'stainless_steel'
    table.colorVect = [0.6, 0.2, 0.6, 1]
    masterString = table.writeToString(masterString)

if post_included:
    post = GS.tubeVolume('post', post_radius, dist_from_table_to_sample - tube_height / 2 - lower_tube_cap_height)
    post.center = {'x': 0, 'y': 0, 'z': ((-tube_height / 2 - lower_tube_cap_height) + -dist_from_table_to_sample) / 2}
    post.mother = 'world'
    post.material = 'stainless_steel'
    post.colorVect = [0.4, 0.7, 0.3, 0.5]
    masterString = post.writeToString(masterString)


# vaccuum shell cylinder to check for reflected entering photons ?
# or maybe have to use particle tracks ecause we want exact positions, not just entered/didn't enter


print 'Saved file.'
geoOutFile = open(geoFileName, 'w+')
geoOutFile.write(masterString)
geoOutFile.close()

